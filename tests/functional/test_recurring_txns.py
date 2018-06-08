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
from datetime import datetime

import os
import sys
import unittest

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

from vantivsdk import *

conf = utils.Configuration()


class TestRecurringTxns(unittest.TestCase):
    def test_simple_auth_with_recurring(self):
        transaction = fields.sale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'recurring'
        transaction.id = 'ThisIsID'

        # Must have a mop
        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card

        subscription = fields.recurringSubscriptionType()
        subscription.planCode = '111'
        subscription.startDate = datetime.today()

        recurring = fields.recurringRequestType()
        recurring.subscription = subscription

        transaction.recurringRequest = recurring

        response = online.request(transaction, conf)
        self.assertEquals('000', response['saleResponse']['response'])



if __name__ == '__main__':
    unittest.main()
