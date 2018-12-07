from random import shuffle
import time
import datetime
from threading import Lock
lock = Lock()


class commManager(object):
    manager = None

    def instance(self, config):
        if commManager.manager is None:
            self.manager = _commManager(config)
        return self.manager

    def __init__(self,config):
        self.instance(config)

    def reset(self):
        self.manager = None


class _commManager:
    REQUEST_RESULT_RESPONSE_RECEIVED = 1
    REQUEST_RESULT_CONNECTION_FAILED = 2
    REQUEST_RESULT_RESPONSE_TIMEOUT = 3
    doMultiSite = False
    errorCount = 0
    currentMultiSiteUrlIndex = 0
    multiSiteThreshold = 5
    lastSiteSwitchTime = 0
    maxHoursWithoutSwitch = 48
    printDebug = False
    multiSiteUrls = []
    legacyUrl = ""

    def __init__(self,config):
        lock.acquire()
        try:
            self.legacyUrl = config.url
            if (config.multiSite is None):
                self.doMultiSite = False
            self.doMultiSite = bool(config.multiSite)

            if (config.printMultiSiteDebug is None):
                self.printDebug = False
            self.printDebug = bool(config.printMultiSiteDebug)

            if self.doMultiSite:
                for x in range(1, 3):
                    if x == 1:
                        siteUrl = config.multiSiteUrl1
                    if x == 2:
                        siteUrl = config.multiSiteUrl2
                    if siteUrl == None:
                        break
                    self.multiSiteUrls.append(siteUrl)
                if len(self.multiSiteUrls) == 0:
                    self.doMultiSite = False
                else:
                    shuffle(self.multiSiteUrls)  # shuffle to randomize which one is selected first
                    self.currentMultiSiteUrlIndex = 0
                    self.errorCount = 0
                    threshold = config.multiSiteErrorThreshold
                    if threshold is not None:
                        t = int(threshold)
                        if t > 0 and t < 100:
                            self.multiSiteThreshold = t
                    maxHours = config.maxHoursWithoutSwitch
                    if maxHours is not None:
                        t = int(maxHours)
                        if t >= 0 and t < 300:
                            self.maxHoursWithoutSwitch = t

                    self.lastSiteSwitchTime = int(round(time.time() * 1000))
        finally:
            lock.release()


    def findUrl(self):
        lock.acquire()
        try:
            url = self.legacyUrl
            if self.doMultiSite:
                switchSite = False
                switchReason = ""
                currentUrl = self.multiSiteUrls[self.currentMultiSiteUrlIndex]
                if self.errorCount < self.multiSiteThreshold:
                    if self.maxHoursWithoutSwitch > 0:
                        diffSinceSwitch = (int(round(time.time() * 1000)) - self.lastSiteSwitchTime) / 3600
                        if diffSinceSwitch > self.maxHoursWithoutSwitch:
                            switchReason = " more than " + str(self.maxHoursWithoutSwitch) + " hours since last switch"
                            switchSite = True
                else:
                    switchReason = " consecutive error count has reached threshold of " + str(self.multiSiteThreshold)
                    switchSite = True

                if switchSite:
                    self.currentMultiSiteUrlIndex = self.currentMultiSiteUrlIndex + 1
                    if self.currentMultiSiteUrlIndex >= len(self.multiSiteUrls):
                        self.currentMultiSiteUrlIndex = 0
                    url = self.multiSiteUrls[self.currentMultiSiteUrlIndex]
                    self.errorCount = 0
                    if self.printDebug:
                        switchDate = datetime.datetime.now()
                        self.lastSiteSwitchTime = switchDate
                        print(str(switchDate) + "  Switched to " + url + " because " + switchReason)
                else:
                    url = currentUrl
            if self.printDebug:
                print ("Selected URL: " + url)

            requestTarget = {'targetUrl':'',
                             'urlIndex' :'',
                             'requestTime' : ''}

            requestTarget["targetUrl"] = url
            requestTarget["urlIndex"] = self.currentMultiSiteUrlIndex
            requestTarget["requestTime"] = int(round(time.time() * 1000))
            return requestTarget
        finally:
            lock.release()

    def reportResult(self, target, result, statusCode):

        if target["requestTime"] < self.lastSiteSwitchTime or not self.doMultiSite:
            return

        if result == self.REQUEST_RESULT_RESPONSE_RECEIVED:
            if statusCode == 200:
                self.errorCount = 0
            elif statusCode >= 400:
                self.errorCount = self.errorCount + 1
            return

        if result == self.REQUEST_RESULT_CONNECTION_FAILED or result == self.REQUEST_RESULT_RESPONSE_TIMEOUT:
            self.errorCount = self.errorCount + 1
            return
