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

class TestBnplAuth(unittest.TestCase):

    def test_simple_bnpl_auth(self):

        transaction = fields.BNPLAuthorizationRequest()
        transaction.reportGroup = "ThisIsAGroup"
        transaction.amount = "5000"
        transaction.orderId = "154646587"
        transaction.id = "1234"
        transaction.provider = 'AFFIRM'
        transaction.postCheckoutRedirectUrl = 'http://www.vantivcnp.com/schema'

        customerInfo = fields.customerInfo()
        customerInfo.accountUserName = 'Jack'
        customerInfo.userAccountNumber = '1234'
        customerInfo.userAccountEmail = 'gmail@gmail.com'
        customerInfo.membershipId = '11111'
        customerInfo.membershipPhone = '123456'
        customerInfo.membershipEmail = 'gmail@gmail.com'
        customerInfo.membershipName = 'fran'
        customerInfo.accountCreatedDate = datetime.datetime.now().strftime("%Y-%m-%d")
        customerInfo.userAccountPhone = '000461223'
        transaction.customerInfo = customerInfo

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Peter'
        billtoaddress.lastName = 'Green'
        billtoaddress.companyName = 'Green Co'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress
        transaction.shipToAddress = billtoaddress

        detailTaxList = list()
        detailTax = fields.detailTax()
        detailTax.taxAmount = 100
        detailTax2 = fields.detailTax()
        detailTax2.taxAmount = 200
        detailTaxList.append(detailTax)
        detailTaxList.append(detailTax2)

        enhancedData = fields.enhancedData()
        enhancedData.detailTax = detailTaxList
        transaction.enhancedData = enhancedData

        response = online.request(transaction, conf)
        self.assertEqual('000', response['BNPLAuthResponse']['response'])
        self.assertEqual('Approved', response['BNPLAuthResponse']['message'])


if __name__ == '__main__':
    unittest.main()