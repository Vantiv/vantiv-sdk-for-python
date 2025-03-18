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

class TestBnplInquiry(unittest.TestCase):

    def test_simple_bnpl_inquiry(self):

        transaction = fields.BNPLInquiryRequest()
        transaction.orderId = "154646587"
        transaction.id = "1234"
        transaction.cnpTxnId = '123456789'

        response = online.request(transaction, conf)
        self.assertEqual('000', response['BNPLInquiryResponse']['response'])
        self.assertEqual('Approved', response['BNPLInquiryResponse']['message'])
        self.assertEqual('789', response['BNPLInquiryResponse']['inquiryResult']['response'])

if __name__ == '__main__':
    unittest.main()