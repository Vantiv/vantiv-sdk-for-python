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


class TestForceCapture(unittest.TestCase):
    def test_force_capture_with_card(self):
        transaction = fields.forceCapture()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.processingType = 'accountFunding'
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '4100000000000001'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['forceCaptureResponse']['response'])
        self.assertEquals('sandbox', response['forceCaptureResponse']['location'])

    def test_force_capture_with_secondary_amount(self):
        transaction = fields.forceCapture()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.secondaryAmount = 20
        transaction.processingType = 'accountFunding'
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '4100000000000001'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['forceCaptureResponse']['response'])
        self.assertEquals('sandbox', response['forceCaptureResponse']['location'])

    def test_force_capture_with_token(self):
        transaction = fields.forceCapture()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.secondaryAmount = 20
        transaction.processingType = 'accountFunding'
        transaction.id = 'ThisIsID'

        token = fields.cardTokenType()
        token.cnpToken = '123456789101112'
        token.expDate = '1210'
        token.cardValidationNum = '555'
        token.type = 'VI'
        transaction.token = token

        response = online.request(transaction, conf)
        self.assertEquals('000', response['forceCaptureResponse']['response'])
        self.assertEquals('sandbox', response['forceCaptureResponse']['location'])


    def test_force_capture_with_business_indicator(self):
        transaction = fields.forceCapture()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.processingType = 'accountFunding'
        transaction.id = 'ThisIsID'
        transaction.businessIndicator = 'consumerBillPayment'

        card = fields.cardType()
        card.number = '4100000000000001'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['forceCaptureResponse']['response'])
        self.assertEquals('sandbox', response['forceCaptureResponse']['location'])

    def test_force_capture_with_business_indicator_different(self):
        transaction = fields.forceCapture()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.processingType = 'accountFunding'
        transaction.id = 'ThisIsID'
        transaction.businessIndicator = 'walletTransfer'

        card = fields.cardType()
        card.number = '4100000000000001'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['forceCaptureResponse']['response'])
        self.assertEquals('sandbox', response['forceCaptureResponse']['location'])

if __name__ == '__main__':
    unittest.main()
