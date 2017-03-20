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


class TestEcheckRedeposit(unittest.TestCase):
    def test_simple_echeck_redeposit(self):
        transaction = fields.echeckRedeposit()
        transaction.litleTxnId = 123456
        transaction.id = 'ThisIsID'

        response = online.request(transaction, conf)
        self.assertEquals('000', response['echeckRedepositResponse']['response'])

    def test_echeck_redeposit_with_echeck(self):
        transaction = fields.echeckRedeposit()
        transaction.litleTxnId = 123456
        transaction.id = 'ThisIsID'

        echeck = fields.echeck()
        echeck.accNum = '12345657890'
        echeck.routingNum = '123456789'
        echeck.checkNum = '123455'
        echeck.accType = 'Checking'
        transaction.echeck = echeck

        response = online.request(transaction, conf)
        self.assertEquals('000', response['echeckRedepositResponse']['response'])

    def test_echeck_redeposit_with_token(self):
        transaction = fields.echeckRedeposit()
        transaction.litleTxnId = 123456
        transaction.id = 'ThisIsID'

        token = fields.echeckToken()
        token.litleToken = '1234565789012'
        token.routingNum = '123456789'
        token.accType = 'Checking'
        transaction.echeckOrEcheckToken = token

        response = online.request(transaction, conf)
        self.assertEquals('000', response['echeckRedepositResponse']['response'])

if __name__ == '__main__':
    unittest.main()
