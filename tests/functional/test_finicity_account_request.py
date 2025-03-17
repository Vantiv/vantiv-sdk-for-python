import os
import sys
import unittest

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

import pyxb

from vantivsdk import *

conf = utils.Configuration()

class TestFinicityAccountRequest(unittest.TestCase):

    def test_simple_finicity_account_req(self):
        transaction = fields.finicityAccountRequest()
        transaction.reportGroup = "ThisIsAGroup"
        transaction.echeckCustomerId = "ABC"
        transaction.setId = "url1"
        transaction.customerId = "154646587"
        transaction.id = "1234"

        response = online.request(transaction, conf)
        self.assertEqual('000', response['finicityAccountResponse']['response'])
        self.assertEqual('Approved', response['finicityAccountResponse']['message'])
        self.assertEqual('sandbox', response['finicityAccountResponse']['location'])
        self.assertEqual('Savings', response['finicityAccountResponse']['finicityAccount']['accType'])

if __name__ == '__main__':
    unittest.main()