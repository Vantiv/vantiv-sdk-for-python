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

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

from vantivsdk import *

package_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, package_root)

import certification_test_conf

conf = certification_test_conf.conf

class TestCertEnhancedAuths(unittest.TestCase):

    # response sample for orderId 14 through 20
    #
    # <litleOnlineResponse version="9.10" xmlns="http://www.litle.com/fields.
    #     response="0" message="Valid Format">
    #     <authorizationResponse reportGroup="Default Report Group">
    #         <litleTxnId>82919994154434833</litleTxnId>
    #         <orderId>14</orderId>
    #         <response>000</response>
    #         <responseTime>2017-02-21T16:14:39</responseTime>
    #         <postDate>2017-02-21</postDate>
    #         <message>Approved</message>
    #         <authCode>VIPREP</authCode>
    #         <fraudResult>
    #             <avsResult>00</avsResult>
    #         </fraudResult>
    #         <tokenResponse>
    #             <litleToken>1111000274230247</litleToken>
    #             <tokenResponseCode>801</tokenResponseCode>
    #             <tokenMessage>Account number was successfully registered</tokenMessage>
    #             <type>VI</type>
    #             <bin>445701</bin>
    #         </tokenResponse>
    #         <enhancedAuthResponse/>
    #         <networkTransactionId>000000000000000</networkTransactionId>
    #     </authorizationResponse>
    # </litleOnlineResponse>
    #
    # enhancedAuthResponse is empty
    # Following assertions can't pass.
    # self.assertEquals('PREPAID', response.transactionResponse.type)
    # self.assertEquals(2000, response.transactionResponse.availableBalance)
    # self.assertEquals('NO', response.transactionResponse.reloadable)
    # self.assertEquals('GIFT', response.transactionResponse.prepaidCardType)

    def test_table_2_1_14_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '14'
        transaction.amount = 10100
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4457010200000247'
        card.expDate = '0821'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('VIPREP', response['authorizationResponse']['authCode'])


    def test_table_2_1_15_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '15'
        transaction.amount = 10100
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'MC'
        card.number = '5500000254444445'
        card.expDate = '0321'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('MCPREP', response['authorizationResponse']['authCode'])

    def test_table_2_1_16_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '16'
        transaction.amount = 10100
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'MC'
        card.number = '5592106621450897'
        card.expDate = '0321'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('MCPREP', response['authorizationResponse']['authCode'])

    def test_table_2_1_17_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '17'
        transaction.amount = 10100
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'MC'
        card.number = '5590409551104142'
        card.expDate = '0321'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('MCPREP', response['authorizationResponse']['authCode'])

    def test_table_2_1_18_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '18'
        transaction.amount = 10100
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'MC'
        card.number = '5587755665222179'
        card.expDate = '0321'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('MCPREP', response['authorizationResponse']['authCode'])


    def test_table_2_1_19_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '19'
        transaction.amount = 10100
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'MC'
        card.number = '5445840176552850'
        card.expDate = '0321'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('MCPREP', response['authorizationResponse']['authCode'])

    def test_table_2_1_20_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '20'
        transaction.amount = 10100
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'MC'
        card.number = '5390016478904678'
        card.expDate = '0321'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('MCPREP', response['authorizationResponse']['authCode'])

    # response sample for orderId 21 through 24
    #  <litleOnlineResponse version="9.10" xmlns="http://www.litle.com/fields.
    #     response="0" message="Valid Format">
    #     <authorizationResponse reportGroup="Default Report Group">
    #         <litleTxnId>82919994227425701</litleTxnId>
    #         <orderId>21</orderId>
    #         <response>000</response>
    #         <responseTime>2017-02-21T16:29:10</responseTime>
    #         <postDate>2017-02-21</postDate>
    #         <message>Approved</message>
    #         <authCode>VIAFF1</authCode>
    #         <fraudResult>
    #             <avsResult>00</avsResult>
    #         </fraudResult>
    #         <tokenResponse>
    #             <litleToken>1111000273442009</litleToken>
    #             <tokenResponseCode>801</tokenResponseCode>
    #             <tokenMessage>Account number was successfully registered</tokenMessage>
    #             <type>VI</type>
    #             <bin>410020</bin>
    #         </tokenResponse>
    #         <enhancedAuthResponse/>
    #         <networkTransactionId>000000000000000</networkTransactionId>
    #     </authorizationResponse>
    # </litleOnlineResponse>
    #
    # enhancedAuthResponse is empty
    # Can't test affluence, add test for authCode
    def test_table_2_1_21_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '21'
        transaction.amount = 10100
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4100200300012009'
        card.expDate = '0921'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('VIAFF1', response['authorizationResponse']['authCode'])

    def test_table_2_1_22_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '22'
        transaction.amount = 10100
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4100200300013007'
        card.expDate = '1121'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('VIAFF2', response['authorizationResponse']['authCode'])


    def test_table_2_1_23_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '23'
        transaction.amount = 10100
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'MC'
        card.number = '5112010201000109'
        card.expDate = '0421'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('MCAFF1', response['authorizationResponse']['authCode'])

    def test_table_2_1_24_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '24'
        transaction.amount = 10100
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'MC'
        card.number = '5112010202000108'
        card.expDate = '0821'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('MCAFF2', response['authorizationResponse']['authCode'])

    def test_table_2_1_25_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '25'
        transaction.amount = 10100
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4100200310000002'
        card.expDate = '1121'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        # TODO Didn't return issuerCountry
        # enhancedAuthResponse is empty
        self.assertEquals('BRA', response['authorizationResponse']['enhancedAuthResponse']['issuerCountry'])


    # Can't pass 26 - 31, <message>Merchant not certified/enabled for IIAS</message>
    def test_table_2_1_26_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '26'
        transaction.amount = 18698
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'MC'
        card.number = '5194560012341234'
        card.expDate = '1221'
        transaction.card = card

        transaction.allowPartialAuth = True

        healthcareiias = fields.healthcareIIAS()
        healthcareAmounts = fields.healthcareAmounts()
        healthcareAmounts.totalHealthcareAmount = 20000
        healthcareiias.healthcareAmounts = healthcareAmounts
        healthcareiias.IIASFlag ='Y'
        transaction.healthcareIIAS = healthcareiias

        response = online.request(transaction, conf)
        self.assertEquals('341', response['authorizationResponse']['response'])
        self.assertEquals('Invalid healthcare amounts', response['authorizationResponse']['message'])

    def test_table_2_1_27_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '27'
        transaction.amount = 18698
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'MC'
        card.number = '5194560012341234'
        card.expDate = '1221'
        transaction.card = card

        transaction.allowPartialAuth = True

        healthcareiias = fields.healthcareIIAS()
        healthcareAmounts = fields.healthcareAmounts()
        healthcareAmounts.totalHealthcareAmount = 15000
        healthcareAmounts.RxAmount = 16000
        healthcareiias.healthcareAmounts = healthcareAmounts
        healthcareiias.IIASFlag ='Y'
        transaction.healthcareIIAS = healthcareiias

        response = online.request(transaction, conf)
        self.assertEquals('341', response['authorizationResponse']['response'])
        self.assertEquals('Invalid healthcare amounts', response['authorizationResponse']['message'])

    def test_table_2_1_28_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '28'
        transaction.amount = 15000
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'MC'
        card.number = '5194560012341234'
        card.expDate = '1221'
        transaction.card = card

        transaction.allowPartialAuth = True

        healthcareiias = fields.healthcareIIAS()
        healthcareAmounts = fields.healthcareAmounts()
        healthcareAmounts.totalHealthcareAmount = 15000
        healthcareAmounts.RxAmount = 3698
        healthcareiias.healthcareAmounts = healthcareAmounts
        healthcareiias.IIASFlag ='Y'
        transaction.healthcareIIAS = healthcareiias

        response = online.request(transaction, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])


    def test_table_2_1_29_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '29'
        transaction.amount = 18699
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4024720001231239'
        card.expDate = '1221'
        transaction.card = card

        transaction.allowPartialAuth = True

        healthcareiias = fields.healthcareIIAS()
        healthcareAmounts = fields.healthcareAmounts()
        healthcareAmounts.totalHealthcareAmount = 31000
        healthcareAmounts.RxAmount = 1000
        healthcareAmounts.visionAmount = 19901
        healthcareAmounts.clinicOtherAmount = 9050
        healthcareAmounts.dentalAmount = 1049
        healthcareiias.healthcareAmounts = healthcareAmounts
        healthcareiias.IIASFlag ='Y'
        transaction.healthcareIIAS = healthcareiias

        response = online.request(transaction, conf)
        self.assertEquals('341', response['authorizationResponse']['response'])
        self.assertEquals('Invalid healthcare amounts', response['authorizationResponse']['message'])

    def test_table_2_1_30_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '30'
        transaction.amount = 20000
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4024720001231239'
        card.expDate = '1221'
        transaction.card = card

        transaction.allowPartialAuth = True

        healthcareiias = fields.healthcareIIAS()
        healthcareAmounts = fields.healthcareAmounts()
        healthcareAmounts.totalHealthcareAmount = 20000
        healthcareAmounts.RxAmount = 1000
        healthcareAmounts.visionAmount = 19901
        healthcareAmounts.clinicOtherAmount = 9050
        healthcareAmounts.dentalAmount = 1049
        healthcareiias.healthcareAmounts = healthcareAmounts
        healthcareiias.IIASFlag ='Y'
        transaction.healthcareIIAS = healthcareiias

        response = online.request(transaction, conf)
        self.assertEquals('341', response['authorizationResponse']['response'])
        self.assertEquals('Invalid healthcare amounts', response['authorizationResponse']['message'])


    def test_table_2_1_31_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '31'
        transaction.amount = 25000
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4024720001231239'
        card.expDate = '1221'
        transaction.card = card

        transaction.allowPartialAuth = True

        healthcareiias = fields.healthcareIIAS()
        healthcareAmounts = fields.healthcareAmounts()
        healthcareAmounts.totalHealthcareAmount = 18699
        healthcareAmounts.RxAmount = 1000
        healthcareAmounts.visionAmount = 15099
        healthcareiias.healthcareAmounts = healthcareAmounts
        healthcareiias.IIASFlag ='Y'
        transaction.healthcareIIAS = healthcareiias

        response = online.request(transaction, conf)
        self.assertEquals('010', response['authorizationResponse']['response'])
        self.assertEquals('Partially Approved', response['authorizationResponse']['message'])
        self.assertEquals('18699', response['authorizationResponse']['approvedAmount'])


if __name__ == '__main__':
    unittest.main()
