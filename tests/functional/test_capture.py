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


class TestCapture(unittest.TestCase):
    
    def test_simple_capture(self):
        transaction = fields.capture()
        transaction.cnpTxnId = 123456000
        transaction.amount = 106
        transaction.id = 'ThisIsID'

        response = online.request(transaction, conf)
        self.assertEquals('000', response['captureResponse']['response'])
        self.assertEquals('sandbox', response['captureResponse']['location'])

    def test_simple_capture_with_optional_order_id(self):
        transaction = fields.capture()
        transaction.cnpTxnId = 123456000
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.id = 'ThisIsID'

        response = online.request(transaction, conf)
        self.assertEquals('000', response['captureResponse']['response'])
        self.assertEquals('sandbox', response['captureResponse']['location'])

if __name__ == '__main__':
    unittest.main()

