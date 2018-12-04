from multiprocessing.sharedctypes import synchronized
from random import shuffle
import time
import datetime


class commManager(object):
    REQUEST_RESULT_RESPONSE_RECEIVED = 1
    REQUEST_RESULT_CONNECTION_FAILED = 2
    REQUEST_RESULT_RESPONSE_TIMEOUT = 3

    manager = None

    doMultiSite = False
    errorCount = 0
    currentMultiSiteUrlIndex = 0
    multiSiteThreshold = 5
    lastSiteSwitchTime = 0
    maxHoursWithoutSwitch = 48
    printDebug = False
    multiSiteUrls = []
    legacyUrl = ""

    @staticmethod
    def instance(config):
        if commManager.manager is None:
            commManager.manager = commManager(config)
        return commManager.manager

    def __init__(self,config):
        if commManager.manager != None:
            raise Exception("This is a singleton class")
        else:
            commManager.manager = self.commManager(config)

    def reset(self):
        self.manager = None

    def commManager(self, config):
        self.legacyUrl = config.url
        if (config.multisite is None):
            self.doMultiSite = False
        self.doMultiSite = bool(config.multiSite)

        if (config.printMultiSiteDebug is None):
            self.printDebug = False
        self.printDebug = bool(config.printMultiSiteDebug)

        if self.doMultiSite:
            for x in range(1, 2):
                siteUrl = config.multiSiteUrl + x
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

    @synchronized
    def findUrl(self):
        url = self.legacyUrl
        if self.doMultiSite:
            switchSite = False
            switchReason = ""
            currentUrl = self.multiSiteUrls[self.currentMultiSiteUrlIndex]
            if self.errorCount < self.multiSiteThreshold:
                if self.maxHoursWithoutSwitch > 0:
                    diffSinceSwitch = (int(round(time.time() * 1000)) - self.lastSiteSwitchTime) / 3600000
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
                self.url = currentUrl
        if self.printDebug:
            print "Selected URL: " + url

        requestTarget = []
        requestTarget["targetUrl"] = self.url
        requestTarget["urlIndex"] = self.currentMultiSiteUrlIndex
        requestTarget["requestTime"] = int(round(time.time() * 1000))
        return requestTarget

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
