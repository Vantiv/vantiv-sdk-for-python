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


class TestCredit(unittest.TestCase):
    def test_simple_credit_with_card(self):
        transaction = fields.credit()
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
        self.assertEquals('000', response['creditResponse']['response'])
        self.assertEquals('sandbox', response['creditResponse']['location'])

    def test_simple_credit_with_paypal(self):
        transaction = fields.credit()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        paypal = fields.payPal()
        paypal.payerId = '1234'
        transaction.paypal = paypal

        response = online.request(transaction, conf)
        self.assertEquals('000', response['creditResponse']['response'])
        self.assertEquals('sandbox', response['creditResponse']['location'])

    def test_simple_credit_with_card_and_secondary_amount(self):
        transaction = fields.credit()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.secondaryAmount = 20
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['creditResponse']['response'])
        self.assertEquals('sandbox', response['creditResponse']['location'])

    def test_simple_credit_paypal_notes(self):
        transaction = fields.credit()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.payPalNotes = 'Hello'
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['creditResponse']['response'])
        self.assertEquals('sandbox', response['creditResponse']['location'])


    def test_processing_instruction_and_amex(self):
        transaction = fields.credit()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        processingInstructions = fields.processingInstructions()
        processingInstructions.bypassVelocityCheck = True
        transaction.processingInstructions = processingInstructions

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['creditResponse']['response'])
        self.assertEquals('sandbox', response['creditResponse']['location'])


    def test_simple_credit_with_litletxn_and_pin(self):
        transaction = fields.credit()
        transaction.cnpTxnId = '1234'
        transaction.amount = 106
        transaction.secondaryAmount = 20
        transaction.pin = '3333'
        transaction.id = 'ThisIsID'

        response = online.request(transaction, conf)
        self.assertEquals('000', response['creditResponse']['response'])
        self.assertEquals('sandbox', response['creditResponse']['location'])

if __name__ == '__main__':
    unittest.main()
