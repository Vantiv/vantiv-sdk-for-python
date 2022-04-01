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
import datetime
conf = utils.Configuration()


class TestCaptureGivenAuth(unittest.TestCase):
    
    def test_simple_capture_given_auth_with_card(self):
        transaction = fields.captureGivenAuth()
        transaction.orderId= '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        # Create authInformation
        authInformation = fields.authInformation()
        authInformation.authDate = datetime.datetime.now().strftime("%Y-%m-%d")
        authInformation.authCode = '543216'
        authInformation.authAmount = 12345
        transaction.authInformation = authInformation

        # Create cardType object
        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        # The type of card is cardType
        transaction.card = card

        # Create contact object
        contact = fields.contact()
        contact.name = 'John & Mary Smith'
        contact.addressLine1 = '1 Main St.'
        contact.city = 'Burlington'
        contact.state = 'MA'
        contact.zip = '01803-3747'
        contact.country = 'USA'
        contact.sellerID = '123'
        contact.url = 'http://tax.xom'
        # The type of retailerAddress is contact
        transaction.retailerAddress = contact

        additionalCOFData = fields.additionalCOFData()
        additionalCOFData.totalPaymentCount = '35'
        additionalCOFData.paymentType = 'Fixed Amount'
        additionalCOFData.uniqueId = '12345wereew233'
        additionalCOFData.frequencyOfMIT = 'BiWeekly'
        additionalCOFData.validationReference = 're3298rhriw4wrw'
        additionalCOFData.sequenceIndicator = '2'

        transaction.additionalCOFData = additionalCOFData

        transaction.crypto = False


        response = online.request(transaction, conf)
        self.assertEquals('000', response['captureGivenAuthResponse']['response'])
        self.assertEquals('sandbox', response['captureGivenAuthResponse']['location'])


    def test_simple_capture_given_auth_with_token(self):
        transaction = fields.captureGivenAuth()
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        # Create authInformation
        authInformation = fields.authInformation()
        authInformation.authDate = datetime.datetime.now().strftime("%Y-%m-%d")
        authInformation.authCode = '543216'
        authInformation.authAmount = 12345
        transaction.authInformation = authInformation

        token = fields.cardTokenType()
        token.cnpToken = '123456789101112'
        token.expDate = '1210'
        token.type = 'VI'
        token.CardValidationNum = '555'
        transaction.token = token
        response = online.request(transaction, conf)
        self.assertEquals('000', response['captureGivenAuthResponse']['response'])
        self.assertEquals('sandbox', response['captureGivenAuthResponse']['location'])

    def test_simple_capture_given_auth_with_tokenURL(self):
        transaction = fields.captureGivenAuth()
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'
    
        # Create authInformation
        authInformation = fields.authInformation()
        authInformation.authDate = datetime.datetime.now().strftime("%Y-%m-%d")
        authInformation.authCode = '543216'
        authInformation.authAmount = 12345
        transaction.authInformation = authInformation
    
        token = fields.cardTokenType()
        token.tokenURL = "http://token.com/sales"
        token.expDate = '1210'
        token.type = 'VI'
        token.CardValidationNum = '555'
        transaction.token = token
        response = online.request(transaction, conf)
        self.assertEquals('000', response['captureGivenAuthResponse']['response'])
        self.assertEquals('sandbox', response['captureGivenAuthResponse']['location'])

    def test_complex_capture_given_auth(self):
        transaction = fields.captureGivenAuth()
        transaction.orderId= '12344'
        transaction.amount = 106
        transaction.secondaryAmount = 20
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        # Create authInformation
        authInformation = fields.authInformation()
        authInformation.authDate = datetime.datetime.now().strftime("%Y-%m-%d")
        authInformation.authCode = '543216'
        authInformation.authAmount = 12345
        transaction.authInformation = authInformation

        # Create contact object
        contact = fields.contact()
        contact.name = 'John & Mary Smith'
        contact.addressLine1 = '1 Main St.'
        contact.city = 'Burlington'
        contact.state = 'MA'
        contact.zip = '01803-3747'
        contact.country = 'USA'
        # The type of billToAddress is contact
        transaction.billToAddress = contact

        processingInstructions = fields.processingInstructions()
        processingInstructions.bypassVelocityCheck = True
        transaction.processingInstructions = processingInstructions

        # Create cardType object
        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        # The type of card is cardType
        transaction.card = card
        response = online.request(transaction, conf)
        self.assertEquals('000', response['captureGivenAuthResponse']['response'])
        self.assertEquals('sandbox', response['captureGivenAuthResponse']['location'])

    def test_auth_info(self):
        transaction = fields.captureGivenAuth()
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.secondaryAmount = 20
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        fraudResult = fields.fraudResult()
        fraudResult.avsResult = '12'
        fraudResult.cardValidationResult = '123'
        fraudResult.authenticationResult = '1'
        fraudResult.advancedAVSResult = '123'

        # Create authInformation
        authInformation = fields.authInformation()
        authInformation.authDate = datetime.datetime.now().strftime("%Y-%m-%d")
        authInformation.authCode = '543216'
        authInformation.authAmount = 12345
        authInformation.fraudResult = fraudResult
        transaction.authInformation = authInformation

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['captureGivenAuthResponse']['response'])
        self.assertEquals('sandbox', response['captureGivenAuthResponse']['location'])
    
    def test_simple_capture_given_auth_with_processing_type(self):
        transaction = fields.captureGivenAuth()
        transaction.orderId= '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.processingType = 'initialInstallment'
        transaction.id = 'ThisIsID'

        # Create authInformation
        authInformation = fields.authInformation()
        authInformation.authDate = datetime.datetime.now().strftime("%Y-%m-%d")
        authInformation.authCode = '543216'
        authInformation.authAmount = 12345
        transaction.authInformation = authInformation

        # Create cardType object
        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        # The type of card is cardType
        transaction.card = card
        response = online.request(transaction, conf)
        self.assertEquals('000', response['captureGivenAuthResponse']['response'])
        self.assertEquals('sandbox', response['captureGivenAuthResponse']['location'])

    def test_simple_capture_given_auth_with_processing_type_COF(self):
        transaction = fields.captureGivenAuth()
        transaction.orderId= '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.processingType = 'initialCOF'
        transaction.id = 'ThisIsID'

        # Create authInformation
        authInformation = fields.authInformation()
        authInformation.authDate = datetime.datetime.now().strftime("%Y-%m-%d")
        authInformation.authCode = '543216'
        authInformation.authAmount = 12345
        transaction.authInformation = authInformation

        # Create cardType object
        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        # The type of card is cardType
        transaction.card = card
        response = online.request(transaction, conf)
        self.assertEquals('000', response['captureGivenAuthResponse']['response'])

        transaction.processingType = 'merchantInitiatedCOF'
        response = online.request(transaction, conf)
        self.assertEquals('000', response['captureGivenAuthResponse']['response'])

        transaction.processingType = 'cardholderInitiatedCOF'
        response = online.request(transaction, conf)
        self.assertEquals('000', response['captureGivenAuthResponse']['response'])

        self.assertEquals('sandbox', response['captureGivenAuthResponse']['location'])

    def test_simple_capture_given_auth_with_original_network_transaction_id(self):
        transaction = fields.captureGivenAuth()
        transaction.orderId= '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.originalNetworkTransactionId = '987654321098765432109876543210'
        transaction.originalTransactionAmount = 1066
        transaction.id = 'ThisIsID'

        # Create authInformation
        authInformation = fields.authInformation()
        authInformation.authDate = datetime.datetime.now().strftime("%Y-%m-%d")
        authInformation.authCode = '543216'
        authInformation.authAmount = 12345
        transaction.authInformation = authInformation

        # Create cardType object
        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        # The type of card is cardType
        transaction.card = card
        response = online.request(transaction, conf)
        self.assertEquals('000', response['captureGivenAuthResponse']['response'])
        self.assertEquals('sandbox', response['captureGivenAuthResponse']['location'])


    def test_capture_given_auth_with_business_indicator(self):
        transaction = fields.captureGivenAuth()
        transaction.orderId= '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'
        transaction.businessIndicator = 'consumerBillPayment'

        # Create authInformation
        authInformation = fields.authInformation()
        authInformation.authDate = datetime.datetime.now().strftime("%Y-%m-%d")
        authInformation.authCode = '543216'
        authInformation.authAmount = 12345
        transaction.authInformation = authInformation

        # Create cardType object
        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        # The type of card is cardType
        transaction.card = card
        response = online.request(transaction, conf)
        self.assertEquals('000', response['captureGivenAuthResponse']['response'])
        self.assertEquals('sandbox', response['captureGivenAuthResponse']['location'])
    
if __name__ == '__main__':
    unittest.main()

