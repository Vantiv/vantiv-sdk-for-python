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

import pyxb

from vantivsdk import *

conf = utils.Configuration()


class TestCapture(unittest.TestCase):
    def test_simple_capture(self):
        transactions = fields.capture()
        transactions.reportGroup = 'Planets'
        transactions.cnpTxnId= '123456000'
        transactions.amount = 106
        transactions.payPalNotes='Notes'
        transactions.orderSource = 'ecommerce'
        transactions.pin = '1234'
        transactions.id = 'ThisIsID'

        response = online.request(transactions, conf)
        self.assertEquals('000', response['captureResponse']['response'])


    def test_simple_capture_with_partial(self):
        transactions = fields.capture()
        transactions.reportGroup = 'Planets'
        transactions.cnpTxnId= '123456000'
        transactions.amount = 106
        transactions.payPalNotes='Notes'
        transactions.orderSource = 'ecommerce'
        transactions.partial = True
        transactions.id = 'ThisIsID'

        response = online.request(transactions, conf)
        self.assertEquals('000', response['captureResponse']['response'])

    def test_complex_capture(self):
        transactions = fields.capture()
        transactions.reportGroup = 'Planets'
        transactions.cnpTxnId= '123456000'
        transactions.amount = 106
        transactions.payPalNotes='Notes'
        transactions.orderSource = 'ecommerce'
        transactions.id = 'ThisIsID'

        enhancedData = fields.enhancedData()
        enhancedData.customerReference = 'Litle'
        enhancedData.deliveryType = 'TBD'
        detailTax = fields.detailTax()
        detailTax.taxAmount = 100
        detailTax2 = fields.detailTax()
        detailTax2.taxAmount = 200
        # pyxb cannot bind multi occurs item, have to use pyxb.BIND
        enhancedData = pyxb.BIND(enhancedData.customerReference, enhancedData.deliveryType, detailTax, detailTax2)

        transactions.enhancedData = enhancedData

        response = online.request(transactions, conf)
        self.assertEquals('000', response['captureResponse']['response'])


if __name__ == '__main__':
    unittest.main()
