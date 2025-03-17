import os
import sys
import unittest
from calendar import Calendar
from enum import auto

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

import pyxb

from vantivsdk import *
import datetime

conf = utils.Configuration()

class TestBnplCancel(unittest.TestCase):

    def test_simple_bnpl_cancel(self):

        transaction = fields.BNPLCancelRequest()
        transaction.reportGroup = "ThisIsAGroup"
        transaction.amount = "5000"
        transaction.orderId = "154646587"
        transaction.id = "1234"
        transaction.cnpTxnId = '123456789'

        response = online.request(transaction, conf)
        self.assertEqual('000', response['BNPLCancelResponse']['response'])
        self.assertEqual('Approved', response['BNPLCancelResponse']['message'])


if __name__ == '__main__':
    unittest.main()