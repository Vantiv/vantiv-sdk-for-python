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

conf = utils.Configuration()


class TestSale(unittest.TestCase):

    def test_simple_sale_with_card(self):
        transaction = fields.sale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('sandbox', response['saleResponse']['location'])

    def test_simple_sale_with_fraud_check(self):
        transaction = fields.sale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        cardholder_authentication = fields.fraudCheckType()
        # base64 value for dummy number '123456789012345678901234567890123456789012345678901234567890'
        # System should accept the request with length 60 of authenticationValueType
        cardholder_authentication.authenticationValue = "MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkw"

        transaction.card = card
        transaction.cardholderAuthentication = cardholder_authentication

        response = online.request(transaction, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('sandbox', response['saleResponse']['location'])

    def test_simple_sale_with_paypal(self):
        transaction = fields.sale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        paypal = fields.payPal()
        paypal.payerId = '1234'
        paypal.token = '1234'
        paypal.transactionId = '123456'
        transaction.paypal = paypal

        response = online.request(transaction, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('sandbox', response['saleResponse']['location'])

    def test_simple_sale_with_applepay_and_secondary_amount(self):
        transaction = fields.sale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.secondaryAmount = 50
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        applepayHeaderType = fields.applepayHeaderType()
        applepayHeaderType.applicationData = '454657413164'
        applepayHeaderType.ephemeralPublicKey = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        applepayHeaderType.publicKeyHash = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        applepayHeaderType.transactionId = '1234'
        applepay = fields.applepayType()
        applepay.header = applepayHeaderType
        applepay.data = 'user'
        applepay.signature = 'sign'
        applepay.version = '12345'
        transaction.applepay = applepay

        response = online.request(transaction, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('sandbox', response['saleResponse']['location'])
        # vvv
        # self.assertEquals('106', response['saleResponse']['applepayResponse']['transactionAmount'])

    def test_simple_sale_with_android_pay(self):
        transaction = fields.sale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'androidpay'
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ0K',
                          response['saleResponse']['androidpayResponse']['cryptogram'])
        self.assertEquals('sandbox', response['saleResponse']['location'])


    def test_simple_sale_with_token(self):
        transaction = fields.sale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        token = fields.cardTokenType()
        token.cnpToken = '1111222233334000'
        token.expDate = '1210'
        token.cardValidationNum = '555'
        token.type = 'VI'
        token.checkoutId = 'checkoutId'
        transaction.token = token

        response = online.request(transaction, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('sandbox', response['saleResponse']['location'])


    def test_simple_sale_with_token(self):
        txn_dict = {
            'sale': {
                'orderId': '6',
                'amount': 10000,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'billToAddress': {
                    'name': 'Joe Green',
                    'addressLine1': '6 Main St.',
                    'city': 'Derry',
                    'state': 'NH',
                    'zip': '03038',
                    'country': 'USA',
                },
                'token': {
                    'cnpToken': '1111222233334000',
                    'expDate': '1210',
                    'cardValidationNum': '555',
                    'type': 'VI',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['saleResponse']['response'])

    def test_sale_with_wallet(self):
        transaction = fields.sale()
        transaction.id = '12345'
        transaction.reportGroup = 'Default'
        transaction.orderId = '67890'
        transaction.amount = 10000
        transaction.orderSource = 'ecommerce'
        transaction.processingType = 'initialInstallment'
        transaction.originalNetworkTransactionId = '9876543210'
        transaction.originalTransactionAmount = 53698
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card

        wallet = fields.wallet()
        wallet.walletSourceTypeId = '1'
        wallet.walletSourceType = 'VisaCheckout'
        transaction.wallet = wallet

        response = online.request(transaction, conf)
        # TODO response without networkTransactionId
        # self.assertEquals('63225578415568556365452427825', response['saleResponse']['networkTransactionId'])

    def test_sale_with_wallet_and_card_suffix_response(self):
        transaction = fields.sale()
        transaction.id = '12345'
        transaction.reportGroup = 'Default'
        transaction.orderId = '67890'
        transaction.amount = 10000
        transaction.orderSource = 'ecommerce'
        transaction.processingType = 'initialInstallment'
        transaction.originalNetworkTransactionId = '9876543210'
        transaction.originalTransactionAmount = 53698
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '5400700000000000'
        card.expDate = '1215'
        card.type = 'MC'
        transaction.card = card

        wallet = fields.wallet()
        wallet.walletSourceTypeId = '1'
        wallet.walletSourceType = 'MasterPass'
        transaction.wallet = wallet

        # response = online.request(transaction, conf)
        # self.assertEquals('000', response['saleResponse']['response'])
        # self.assertNotIn('networkTransactionId', response['saleResponse'])

    def test_sale_with_processing_type(self):
        transaction = fields.sale()
        transaction.id = '12345'
        transaction.reportGroup = 'Default'
        transaction.orderId = '67890'
        transaction.amount = 10000
        transaction.orderSource = 'ecommerce'
        transaction.processingType = 'initialInstallment'
        transaction.originalNetworkTransactionId = '9876543210'
        transaction.originalTransactionAmount = 53698
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('sandbox', response['saleResponse']['location'])

    def test_sale_with_processing_type_COF(self):
        transaction = fields.sale()
        transaction.id = '12345'
        transaction.reportGroup = 'Default'
        transaction.orderId = '67890'
        transaction.amount = 10000
        transaction.orderSource = 'ecommerce'
        transaction.processingType = 'initialCOF'
        transaction.originalNetworkTransactionId = '9876543210'
        transaction.originalTransactionAmount = 53698
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['saleResponse']['response'])

        transaction.processingType = 'merchantInitiatedCOF'
        response = online.request(transaction, conf)
        self.assertEquals('000', response['saleResponse']['response'])

        transaction.processingType = 'cardholderInitiatedCOF'
        response = online.request(transaction, conf)
        self.assertEquals('000', response['saleResponse']['response'])

        self.assertEquals('sandbox', response['saleResponse']['location'])


    def test_sale_with_sepa_direct_debit(self):
        transaction = fields.sale()
        transaction.id = '12345'
        transaction.reportGroup = 'Default'
        transaction.orderId = '67890'
        transaction.amount = 10000
        transaction.orderSource = 'ecommerce'
        transaction.processingType = 'initialInstallment'
        transaction.originalNetworkTransactionId = '9876543210'
        transaction.originalTransactionAmount = 53698
        transaction.id = 'ThisIsID'

        sepaDirectDebit = fields.sepaDirectDebitType()
        sepaDirectDebit.iban = 'SepaDirectDebit Iban'
        sepaDirectDebit.mandateProvider = 'Merchant'
        sepaDirectDebit.sequenceType = 'OneTime'
        transaction.sepaDirectDebit = sepaDirectDebit

        response = online.request(transaction, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('http://redirect.url.vantiv.com',
                          response['saleResponse']['sepaDirectDebitResponse']['redirectUrl'])
        self.assertEquals('sandbox', response['saleResponse']['location'])

    def test_sale_with_ideal(self):
        transaction = fields.sale()
        transaction.id = '12345'
        transaction.reportGroup = 'Default'
        transaction.orderId = '67890'
        transaction.amount = 10000
        transaction.orderSource = 'ecommerce'
        transaction.processingType = 'initialInstallment'
        transaction.originalNetworkTransactionId = '9876543210'
        transaction.originalTransactionAmount = 53698
        transaction.id = 'ThisIsID'

        ideal = fields.idealType()
        ideal.preferredLanguage = 'AD'
        transaction.ideal = ideal

        response = online.request(transaction, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('http://redirect.url.vantiv.com',
                          response['saleResponse']['idealResponse']['redirectUrl'])
        self.assertEquals('sandbox', response['saleResponse']['location'])

    def test_sale_with_giropay(self):
        transaction = fields.sale()
        transaction.id = '12345'
        transaction.reportGroup = 'Default'
        transaction.orderId = '67890'
        transaction.amount = 10000
        transaction.orderSource = 'ecommerce'
        transaction.processingType = 'initialInstallment'
        transaction.originalNetworkTransactionId = '9876543210'
        transaction.originalTransactionAmount = 53698
        transaction.id = 'ThisIsID'

        giropay = fields.giropayType()
        giropay.preferredLanguage = 'DE'
        transaction.giropay = giropay

        response = online.request(transaction, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('http://redirect.url.vantiv.com',
                          response['saleResponse']['giropayResponse']['redirectUrl'])
        self.assertEquals('sandbox', response['saleResponse']['location'])

    def test_sale_with_sofort(self):
        transaction = fields.sale()
        transaction.id = '12345'
        transaction.reportGroup = 'Default'
        transaction.orderId = '67890'
        transaction.amount = 10000
        transaction.orderSource = 'ecommerce'
        transaction.processingType = 'initialInstallment'
        transaction.originalNetworkTransactionId = '9876543210'
        transaction.originalTransactionAmount = 53698
        transaction.id = 'ThisIsID'

        sofort = fields.sofortType()
        sofort.preferredLanguage = 'NL'
        transaction.sofort = sofort

        response = online.request(transaction, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('http://redirect.url.vantiv.com',
                          response['saleResponse']['sofortResponse']['redirectUrl'])
        self.assertEquals('sandbox', response['saleResponse']['location'])

    def test_simple_sale_with_card_skipRealtimeAU_null(self):
        transaction = fields.sale()
        transaction.amount = 106
        transaction.cnpTxnId = 123456
        transaction.orderId = '12344'
        transaction.orderSource = 'ecommerce'

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4100000000000000'
        card.expDate = '1210'
        transaction.card = card
        transaction.id = 'id'

        response = online.request(transaction, conf)
        self.assertEquals('Approved', response['saleResponse']['message'])
        self.assertEquals('sandbox', response['saleResponse']['location'])

    def test_simple_sale_with_card_skipRealtimeAU_true(self):
        transaction = fields.sale()
        transaction.amount = 106
        transaction.cnpTxnId = 123456
        transaction.orderId = '12344'
        transaction.orderSource = 'ecommerce'
        transaction.skipRealtimeAU = True

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4100000000000000'
        card.expDate = '1210'
        transaction.card = card
        transaction.id = 'id'

        response = online.request(transaction, conf)
        self.assertEquals('Approved', response['saleResponse']['message'])
        self.assertEquals('sandbox', response['saleResponse']['location'])

    def test_simple_sale_with_card_skipRealtimeAU_false(self):
        transaction = fields.sale()
        transaction.amount = 106
        transaction.cnpTxnId = 123456
        transaction.orderId = '12344'
        transaction.orderSource = 'ecommerce'
        transaction.skipRealtimeAU = False

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4100000000000000'
        card.expDate = '1210'
        transaction.card = card
        transaction.id = 'id'

        response = online.request(transaction, conf)
        self.assertEquals('Approved', response['saleResponse']['message'])
        self.assertEquals('sandbox', response['saleResponse']['location'])

    def test_simple_sale_with_authenticated_shopper_id(self):
        transaction = fields.sale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        token = fields.cardTokenType()
        token.cnpToken = '1111222233334000'
        token.expDate = '1210'
        token.cardValidationNum = '555'
        token.type = 'VI'
        token.checkoutId = 'checkoutId12345678'
        token.authenticatedShopperID = '123456'
        transaction.token = token

        response = online.request(transaction, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('sandbox', response['saleResponse']['location'])

    def test_sale_with_business_indicator(self):
        transaction = fields.sale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'
        transaction.businessIndicator = 'consumerBillPayment'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('sandbox', response['saleResponse']['location'])

    def test_sale_with_retaileraddress_additionalcof(self):
        transaction = fields.sale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'
        transaction.crypto = False
        transaction.businessIndicator = 'consumerBillPayment'
        transaction.orderChannelEnum = 'PHONE'

        transaction.fraudCheckStatus = 'not approved'

        additioncof = fields.additionalCOFData()
        additioncof.totalPaymentCount = 'dfvd'
        additioncof.paymentType = 'Fixed Amount'
        additioncof.uniqueId = '12345wereew233'
        additioncof.frequencyOfMIT = 'BiWeekly'
        additioncof.validationReference = 're3298rhriw4wrw'
        additioncof.sequenceIndicator = '2'

        transaction.additioncof = additioncof

        contact = fields.contact()
        contact.name = 'john & Mary Smith'
        contact.addressLine1 = '1st Main Street'
        contact.city = 'Burlington'
        contact.state = 'MA'
        contact.zip = '01867-4456'
        contact.country = 'USA'

        transaction.retailerAddress = contact

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('sandbox', response['saleResponse']['location'])


if __name__ == '__main__':
    unittest.main()
