import time
import unittest
from multiprocessing.dummy import Pool as ThreadPool
import random
import traceback
from vantivsdk import utils, fields, online
from vantivsdk.commManager import commManager


class TestCommManagerMultiThreaded(unittest.TestCase):
    threadCount = 10
    cycleCount = 100
    config = utils.Configuration()
    config.multiSite = True
    successCount = 0
    failedCount = 0

    def multiThreadTests(self, threadId):
        startTime = (int(round(time.time() * 1000)))
        totalTransactionTime = 0
        requestCount = 0

        for i in range(1, self.cycleCount+1):
            requestCount += 1
            target = commManager(self.config).manager.findUrl()

            try:
                sleepTime = (100 + random.randint(0, 500)) / 1000
                totalTransactionTime += sleepTime
                time.sleep(sleepTime)
            except Exception:
                traceback.print_exc()
                target.reportResult(target, 1, 200)

        duration = (int(round(time.time() * 1000))) - startTime
        print("Thread " + str(threadId) + " completed. Total Requests:" + str(requestCount) + "  Elapsed Time:" + str(
            (duration / 1000)) + " secs    Average Txn Time:" + str((totalTransactionTime / requestCount)) + " ms")


    def test_multiThreaded_without_request(self):
        pool = ThreadPool(self.threadCount)
        id = list(range(1,self.threadCount+1))
        pool.map(self.multiThreadTests, id)



    def multiThreadTests_with_request(self, threadId):
        startTime = (int(round(time.time() * 1000)))
        totalTransactionTime = 0
        requestCount = 0
        self.successCount = 0
        self.failedCount = 0
        for i in range(1, self.cycleCount+1):
            requestCount += 1
            totalTransactionTime += self.doCycle(threadId)
            try:
                sleepTime = (random.randint(0, 50)) / 1000
                time.sleep(sleepTime)
            except Exception:
                traceback.print_exc()

        duration = (int(round(time.time() * 1000))) - startTime
        print("Thread " + str(threadId) + " completed. Total Requests:" + str(requestCount) + "  Success:" +
              str(self.successCount) + "  Failed:" + str(self.failedCount) + "  Elapsed Time:" + str((duration/1000)) +
              " secs    Average Txn Time:" + str((totalTransactionTime/requestCount)) + " ms")

    def doCycle(self,threadId):
        authorization = fields.authorization()
        authorization.reportGroup = '123456'
        authorization.orderId = str(threadId - (int(round(time.time() * 1000))))
        authorization.amount = '106'
        authorization.orderSource = 'ecommerce'
        authorization.id = 'id' + str(threadId)


        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        authorization.card = card
        startTime = (int(round(time.time() * 1000)))
        response = online.request(authorization, self.config)
        # print(response)
        responseTime = (int(round(time.time() * 1000))) - startTime
        self.assertEquals("123456", response['authorizationResponse']['@reportGroup'])
        if(response['authorizationResponse']['response'] == '000'):
            self.successCount +=1
        else:
            self.failedCount += 1
        return responseTime


    def test_multiThreaded_with_request(self):
        pool = ThreadPool(self.threadCount)
        id = list(range(1,self.threadCount+1))
        pool.map(self.multiThreadTests_with_request, id)


    def test_findUrl(self):
        target = commManager(self.config).manager

        doMultiSite_record = target.doMultiSite
        printDebug_record = target.printDebug
        currentMultiSiteUrlIndex_reCord = target.currentMultiSiteUrlIndex
        errorCount_record = target.errorCount
        lastSiteSwitchTime_record = target.lastSiteSwitchTime

        # condition1: doMultiSite as false
        target.doMultiSite = False

        url = target.legacyUrl
        self.assertEquals(url,target.findUrl()['targetUrl'])

        target.doMultiSite = doMultiSite_record
        # condition2
        target.doMultiSite = True
        target.printDebug = True
        target.currentMultiSiteUrlIndex = 0

        url = target.multiSiteUrls[0]
        self.assertEquals(url,target.findUrl()['targetUrl'])

        target.doMultiSite = doMultiSite_record
        target.printDebug = printDebug_record
        target.currentMultiSiteUrlIndex = currentMultiSiteUrlIndex_reCord

        # condition3
        target.doMultiSite = True
        target.printDebug = True
        target.errorCount = 100
        target.currentMultiSiteUrlIndex = 0

        url = target.multiSiteUrls[1]
        self.assertEquals(url, target.findUrl()['targetUrl'])

        target.doMultiSite = doMultiSite_record
        target.printDebug = printDebug_record
        target.errorCount= errorCount_record
        target.currentMultiSiteUrlIndex = currentMultiSiteUrlIndex_reCord
        target.lastSiteSwitchTime = lastSiteSwitchTime_record

        # condition4
        target.doMultiSite = True
        target.printDebug = True
        target.errorCount = 100
        target.currentMultiSiteUrlIndex = 1

        url = target.multiSiteUrls[0]
        self.assertEquals(url, target.findUrl()['targetUrl'])

        target.doMultiSite = doMultiSite_record
        target.printDebug = printDebug_record
        target.errorCount = errorCount_record
        target.currentMultiSiteUrlIndex = currentMultiSiteUrlIndex_reCord
        target.lastSiteSwitchTime = lastSiteSwitchTime_record
