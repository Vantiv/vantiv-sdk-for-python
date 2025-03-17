import os
import sys
import unittest

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

import pyxb

from vantivsdk import *

conf = utils.Configuration()

class TestFinicityUrlRequest(unittest.TestCase):

    def test_simple_finicity_url_req(self):
        transaction = fields.finicityUrlRequest()
        transaction.reportGroup = "ThisIsAGroup"
        transaction.customerId = "154646587"
        transaction.firstName = "John"
        transaction.lastName = "Smith"
        transaction.setId = "url1"
        transaction.phoneNumber = "1-801-984-4200"
        transaction.email = "myname@mycompany.com"
        transaction.id = "1234"

        response = online.request(transaction, conf)
        self.assertEqual('000', response['finicityUrlResponse']['response'])
        self.assertEqual('Approved', response['finicityUrlResponse']['message'])
        self.assertEqual('sandbox', response['finicityUrlResponse']['location'])


if __name__ == '__main__':
    unittest.main()