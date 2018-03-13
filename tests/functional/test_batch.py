# -*- coding: utf-8 -*-
# Copyright (c) 2017 Vantiv eCommerce
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the 'Software'), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import os
import sys
import unittest
import time

from subprocess import call

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

from vantivsdk import *

import datetime

conf = utils.Configuration()


class TestBatch(unittest.TestCase):

    def test_batch_submit_useEncryption(self):
        # Initial Transactions container
        transactions = batch.Transactions()
        # Transactions presented by dict
        txn_dict = {
            'authorization':{
                'reportGroup': 'Planets',
                'orderId': '12344',
                'amount': '106',
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'expDate': '1210',
                    'number': '4100000000000000',
                    'type': 'VI',
                }
            }
        }
        transactions.add(txn_dict)

        # Card
        card = fields.cardType()
        card.number = '4457010000000009'
        card.expDate = '0121'
        card.cardValidationNum = '349'
        card.type = 'VI'

        # eCheck
        # echeck = fields.echeck()
        # echeck.accType = 'Checking'
        # echeck.accNum = '4099999992'
        # echeck.routingNum = '011075150'

        # billtoaddress
        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Mike'
        billtoaddress.middleInitial = 'J'
        billtoaddress.lastName = 'Hammer'
        billtoaddress.phone = '999-999-9999'

        # Initial authorization
        authorization = fields.authorization()
        authorization.orderId = '1'
        authorization.amount = 10010
        authorization.reportGroup = 'Planets'
        authorization.orderSource = 'ecommerce'
        authorization.card = card
        authorization.billtoaddress = billtoaddress
        authorization.id = 'thisisid'
        # Add transaction to container
        transactions.add(authorization)

        # Initial authorization
        authorization2 = fields.authorization()
        authorization2.orderId = '2'
        authorization2.amount = 1001
        authorization2.reportGroup = 'Planets'
        authorization2.orderSource = 'ecommerce'
        authorization2.card = card
        authorization2.billtoaddress = billtoaddress
        authorization2.id = 'thisisid'
        # Add transaction to container
        transactions.add(authorization2)

        # Initial authorization
        sale = fields.sale()
        sale.orderId = '1'
        sale.amount = 10010
        sale.reportGroup = 'Planets'
        sale.orderSource = 'ecommerce'
        sale.card = card
        sale.billtoaddress = billtoaddress
        sale.id = 'thisisid'
        # Add transaction to container
        transactions.add(sale)

        ## >>> WITH ENCRYPTION

        conf.useEncryption = True
        conf.user = conf.test_pgp_user
        conf.password = conf.test_pgp_password
        conf.sftp_username = conf.test_pgp_sftp_username
        conf.sftp_password = conf.test_pgp_sftp_password
        withEncryptionFilename = 'batch_test_%s' % datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")


        # stream to Vaitiv eCommerce and get object as response
        response = batch.submit(transactions, conf, withEncryptionFilename)

        print(response)

        retry = True
        tried = 0
        withEncryptionReponseFilepath = ''
        while retry:
            tried += 1
            try:
                withEncryptionReponseFilepath = batch._get_file_from_sftp(response, conf, False, 60)
                retry = False
            except:
                # sleep 1 minute waiting for batch get processed
                print("sleep 30 seconds waiting for batch get processed")
                time.sleep(30)
            if tried > 20:
                self.fail("Timeout for retrieve batch response")
                break        

        #local_path = os.path.join(conf.batch_requests_path, '%s.xml' % withEncryptionFilename)
        # encryptionReader = open(withEncryptionReponseFilepath, 'r')
        # temp = open('localCopy', 'w')
        # temp.write(encryptionReader.read())
        # encryptionReader.close()
        # temp.close()   
        call(["cat", withEncryptionReponseFilepath])
        # Undo setting configuration.
        conf.user = conf.test_txn_user
        conf.password = conf.test_txn_password
        conf.sftp_username = conf.test_txn_sftp_username
        conf.sftp_password = conf.test_txn_sftp_password
        conf.userEncryption = False
        ### <<< WITH ENCRYPTION

        with open(withEncryptionReponseFilepath, 'r') as xml_file:
            obj = fields.CreateFromDocument(xml_file.read())
            self.assertEquals("Valid Format", obj.message)
            

    def test_batch_submit(self):
        # Initial Transactions container
        transactions = batch.Transactions()
        # Transactions presented by dict
        txn_dict = {
            'authorization':{
                'reportGroup': 'Planets',
                'orderId': '12344',
                'amount': '106',
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'expDate': '1210',
                    'number': '4100000000000000',
                    'type': 'VI',
                }
            }
        }
        transactions.add(txn_dict)

        # Card
        card = fields.cardType()
        card.number = '4457010000000009'
        card.expDate = '0121'
        card.cardValidationNum = '349'
        card.type = 'VI'

        # eCheck
        # echeck = fields.echeck()
        # echeck.accType = 'Checking'
        # echeck.accNum = '4099999992'
        # echeck.routingNum = '011075150'

        # billtoaddress
        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Mike'
        billtoaddress.middleInitial = 'J'
        billtoaddress.lastName = 'Hammer'
        billtoaddress.phone = '999-999-9999'

        # Initial authorization
        authorization = fields.authorization()
        authorization.orderId = '1'
        authorization.amount = 10010
        authorization.reportGroup = 'Planets'
        authorization.orderSource = 'ecommerce'
        authorization.card = card
        authorization.billtoaddress = billtoaddress
        authorization.id = 'thisisid'
        # Add transaction to container
        transactions.add(authorization)

        # Initial authorization
        authorization2 = fields.authorization()
        authorization2.orderId = '2'
        authorization2.amount = 1001
        authorization2.reportGroup = 'Planets'
        authorization2.orderSource = 'ecommerce'
        authorization2.card = card
        authorization2.billtoaddress = billtoaddress
        authorization2.id = 'thisisid'
        # Add transaction to container
        transactions.add(authorization2)

        # Initial authorization
        sale = fields.sale()
        sale.orderId = '1'
        sale.amount = 10010
        sale.reportGroup = 'Planets'
        sale.orderSource = 'ecommerce'
        sale.card = card
        sale.billtoaddress = billtoaddress
        sale.id = 'thisisid'
        # Add transaction to container
        transactions.add(sale)

        filename = 'batch_test_%s' % datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")

        # stream to Vaitiv eCommerce and get object as response
        response = batch.submit(transactions, conf, filename)

        with open(os.path.join(conf.batch_requests_path, '%s.xml' % filename), 'r') as xml_file:
            obj = fields.CreateFromDocument(xml_file.read())
            self.assertEquals(1, obj.numBatchRequests)
            self.assertEquals(11117, obj.batchRequest[0].authAmount)

        self.assertEquals('%s.xml.asc' % filename, response)

    def test_batch_rfr(self):
        # Initial Transactions container
        transactions = batch.Transactions()
        transactions.sameDayFunding = True

        # Card
        card = fields.cardType()
        card.number = '4457010000000009'
        card.expDate = '0121'
        card.cardValidationNum = '349'
        card.type = 'VI'

        # eCheck
        # echeck = fields.echeck()
        # echeck.accType = 'Checking'
        # echeck.accNum = '4099999992'
        # echeck.routingNum = '011075150'

        # billtoaddress
        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Mike'
        billtoaddress.middleInitial = 'J'
        billtoaddress.lastName = 'Hammer'
        billtoaddress.phone = '999-999-9999'

        # Initial authorization
        authorization = fields.authorization()
        authorization.orderId = '1'
        authorization.amount = 10010
        authorization.reportGroup = u'русский中文'
        authorization.orderSource = 'ecommerce'
        authorization.card = card
        authorization.billtoaddress = billtoaddress
        authorization.id = 'thisisid'
        # Add transaction to container
        transactions.add(authorization)

        # Initial authorization
        authorization2 = fields.authorization()
        authorization2.orderId = '2'
        authorization2.amount = 1001
        authorization2.reportGroup = 'Planets'
        authorization2.orderSource = 'ecommerce'
        authorization2.card = card
        authorization2.billtoaddress = billtoaddress
        authorization2.id = 'thisisid'
        # Add transaction to container
        transactions.add(authorization2)

        # Initial authorization
        sale = fields.sale()
        sale.orderId = '1'
        sale.amount = 10010
        sale.reportGroup = 'Planets'
        sale.orderSource = 'ecommerce'
        sale.card = card
        sale.billtoaddress = billtoaddress
        sale.id = 'thisisid'
        # Add transaction to container
        transactions.add(sale)

        filename = 'batch_test_%s' % datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")

        # stream to Vaitiv eCommerce and get object as response
        response_filename = batch.submit(transactions, conf, filename)
        self.assertEquals('%s.xml.asc' % filename, response_filename)

        response = {}


        # Example for RFRRequest
        RFRRequest = fields.RFRRequest()

        retry = True
        tried = 0
        while retry:
            tried += 1
            try:
                response = batch.retrieve(response_filename, conf)
                retry = False
                RFRRequest.litleSessionId = response['@litleSessionId']
            except:
                # sleep 1 minute waiting for batch get processed
                print("sleep 30 seconds waiting for batch get processed")
                time.sleep(30)
            if tried > 20:
                self.fail("Timeout for retrieve batch response")
                break

        transactions = batch.Transactions()
        transactions.add(RFRRequest)

        # submit batch request
        response_rfr_filename = batch.submit(transactions, conf)

        retry = True
        tried = 0
        while retry:
            tried += 1
            try:
                # retrieve rfr batch request
                response_rfr = batch.retrieve(response_rfr_filename, conf)
                retry = False
                self.assertIn('batchResponse', response_rfr)
                self.assertEquals(response_rfr['batchResponse']['authorizationResponse'][0]['litleTxnId'],
                                  response['batchResponse']['authorizationResponse'][0]['litleTxnId'])
            except:
                # sleep 1 minute waiting for batch get processed
                print("sleep 30 seconds waiting for rfr batch get processed")
                time.sleep(30)
            if tried > 20:
                self.fail("Timeout for retrieve rfr batch response")
                break

    def test_batch_dict(self):
        txn_dict = {
            'authorization':[
                {
                    'reportGroup': 'Planets',
                    'orderId': '12344',
                    'amount': '100',
                    'orderSource': 'ecommerce',
                    'id': 'thisisid',
                    'card': {
                        'expDate': '1210',
                        'number': '4100000000000000',
                        'type': 'VI',
                    }
                },
                {
                    'reportGroup': 'Planets',
                    'orderId': '12345',
                    'amount': '200',
                    'orderSource': 'ecommerce',
                    'id': 'thisisid',
                    'card': {
                        'expDate': '1210',
                        'number': '4100000000000000',
                        'type': 'VI',
                    }
                },
                {
                    'reportGroup': 'Planets',
                    'orderId': '12346',
                    'amount': '300',
                    'orderSource': 'ecommerce',
                    'id': 'thisisid',
                    'card': {
                        'expDate': '1210',
                        'number': '4100000000000000',
                        'type': 'VI',
                    }
                }
            ],
            'sale': {
                'reportGroup': 'Planets',
                'orderId': '12344',
                'amount': '106',
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'expDate': '1210',
                    'number': '4100000000000000',
                    'type': 'VI',
                }
            }
        }

        filename = 'batch_test_%s' % datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")

        # stream to Vaitiv eCommerce and get object as response
        response_filename = batch.submit(txn_dict, conf, filename)
        self.assertEquals('%s.xml.asc' % filename, response_filename)

        response = {}


        # Example for RFRRequest
        RFRRequest = fields.RFRRequest()

        retry = True
        tried = 0
        while retry:
            tried += 1
            try:
                response = batch.retrieve(response_filename, conf)
                retry = False
                RFRRequest.litleSessionId = response['@litleSessionId']
            except:
                # sleep 1 minute waiting for batch get processed
                print("sleep 30 seconds waiting for batch get processed")
                time.sleep(30)
            if tried > 20:
                self.fail("Timeout for retrieve batch response")
                break

        transactions = batch.Transactions()
        transactions.add(RFRRequest)

        # submit batch request
        response_rfr_filename = batch.submit(transactions, conf)

        retry = True
        tried = 0
        while retry:
            tried += 1
            try:
                # retrieve rfr batch request
                response_rfr = batch.retrieve(response_rfr_filename, conf)
                retry = False
                self.assertIn('batchResponse', response_rfr)
                self.assertEquals(response_rfr['batchResponse']['authorizationResponse'][0]['litleTxnId'],
                                  response['batchResponse']['authorizationResponse'][0]['litleTxnId'])
            except:
                # sleep 1 minute waiting for batch get processed
                print("sleep 30 seconds waiting for rfr batch get processed")
                time.sleep(30)
            if tried > 20:
                self.fail("Timeout for retrieve rfr batch response")
                break

    def test_batch_mix_transaction_recurringtransaction(self):
        txn_dict = {
            'sameDayFunding': 0,
            'authorization':[
                {
                    'reportGroup': 'Planets',
                    'orderId': '12344',
                    'amount': '100',
                    'orderSource': 'ecommerce',
                    'id': 'thisisid',
                    'card': {
                        'expDate': '1210',
                        'number': '4100000000000000',
                        'type': 'VI',
                    }
                },
                {
                    'reportGroup': 'Planets',
                    'orderId': '12345',
                    'amount': '200',
                    'orderSource': 'ecommerce',
                    'id': 'thisisid',
                    'card': {
                        'expDate': '1210',
                        'number': '4100000000000000',
                        'type': 'VI',
                    }
                },
                {
                    'reportGroup': 'Planets',
                    'orderId': '12346',
                    'amount': '300',
                    'orderSource': 'ecommerce',
                    'id': 'thisisid',
                    'card': {
                        'expDate': '1210',
                        'number': '4100000000000000',
                        'type': 'VI',
                    }
                }
            ],
            'sale': {
                'reportGroup': 'Planets',
                'orderId': '12344',
                'amount': '106',
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'expDate': '1210',
                    'number': '4100000000000000',
                    'type': 'VI',
                }
            },
            'createPlan': {
                'amount': '106',
                'planCode': '1',
                'name': 'plan name',
                'description': 'plan description',
                'intervalType': 'ANNUAL'
            }
        }

        filename = 'batch_test_%s' % datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")

        # stream to Vaitiv eCommerce and get object as response
        response_filename = batch.submit(txn_dict, conf, filename)
        self.assertEquals('%s.xml.asc' % filename, response_filename)

        response = {}


        # Example for RFRRequest
        RFRRequest = fields.RFRRequest()

        retry = True
        tried = 0
        while retry:
            tried += 1
            try:
                response = batch.retrieve(response_filename, conf)
                retry = False
                RFRRequest.litleSessionId = response['@litleSessionId']
            except:
                # sleep 1 minute waiting for batch get processed
                print("sleep 30 seconds waiting for batch get processed")
                time.sleep(30)
            if tried > 20:
                self.fail("Timeout for retrieve batch response")
                break

        transactions = batch.Transactions()
        transactions.sameDayFunding = True
        transactions.add(RFRRequest)

        # submit batch request
        response_rfr_filename = batch.submit(transactions, conf)

        retry = True
        tried = 0
        while retry:
            tried += 1
            try:
                # retrieve rfr batch request
                response_rfr = batch.retrieve(response_rfr_filename, conf)
                retry = False
                self.assertIn('batchResponse', response_rfr)
                self.assertEquals(response_rfr['batchResponse'][0]['authorizationResponse'][0]['litleTxnId'],
                                  response['batchResponse'][0]['authorizationResponse'][0]['litleTxnId'])
                self.assertEquals(response_rfr['batchResponse'][1]['createPlanResponse']['litleTxnId'],
                                  response['batchResponse'][1]['createPlanResponse']['litleTxnId'])
            except:
                # sleep 1 minute waiting for batch get processed
                print("sleep 30 seconds waiting for rfr batch get processed")
                time.sleep(30)
            if tried > 20:
                self.fail("Timeout for retrieve rfr batch response")
                break



if __name__ == '__main__':
    unittest.main()
