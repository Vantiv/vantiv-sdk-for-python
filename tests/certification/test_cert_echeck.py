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

package_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, package_root)

import certification_test_conf

conf = certification_test_conf.conf

class TestCertEcheck(unittest.TestCase):
    def test_table_2_4_37(self):
        # orderId 37
        transaction = fields.echeckVerification()
        transaction.orderId = '37'
        transaction.amount = 3001
        transaction.orderSource = 'telephone'
        transaction.id = 'thisisid'

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Tom'
        billtoaddress.lastName = 'Black'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = fields.echeck()
        echeck.accNum = '10@BC99999'
        echeck.accType = 'Checking'
        echeck.routingNum = '053100300'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('301', response['echeckVerificationResponse']['response'])
        self.assertEquals('Invalid Account Number', response['echeckVerificationResponse']['message'])


    def test_table_2_4_38(self):
        # orderId *
        transaction = fields.echeckVerification()
        transaction.orderId = '38'
        transaction.amount = 3002
        transaction.orderSource = 'telephone'
        transaction.id = 'thisisid'

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'John'
        billtoaddress.lastName = 'Smith'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = fields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '1099999999'
        echeck.routingNum = '011075150'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('000', response['echeckVerificationResponse']['response'])
        self.assertEquals('Approved', response['echeckVerificationResponse']['message'])


    def test_table_2_4_39(self):
        # orderId *
        transaction = fields.echeckVerification()
        transaction.orderId = '39'
        transaction.amount = 3003
        transaction.orderSource = 'telephone'
        transaction.id = 'thisisid'

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Robert'
        billtoaddress.lastName = 'Jones'
        billtoaddress.companyName = 'Good Goods Inc'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = fields.echeck()
        echeck.accType = 'Corporate'
        echeck.accNum = '3099999999'
        echeck.routingNum = '053100300'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('950', response['echeckVerificationResponse']['response'])
        self.assertEquals('Decline - Negative Information on File', response['echeckVerificationResponse']['message'])


    def test_table_2_4_40(self):
        # orderId *
        transaction = fields.echeckVerification()
        transaction.orderId = '40'
        transaction.amount = 3004
        transaction.orderSource = 'telephone'
        transaction.id = 'thisisid'

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Peter'
        billtoaddress.lastName = 'Green'
        billtoaddress.companyName = 'Green Co'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = fields.echeck()
        echeck.accType = 'Corporate'
        echeck.accNum = '8099999999'
        echeck.routingNum = '011075150'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('951', response['echeckVerificationResponse']['response'])
        self.assertEquals('Absolute Decline', response['echeckVerificationResponse']['message'])


    def test_table_2_6_41(self):
        # orderId *
        transaction = fields.echeckSale()
        transaction.orderId = '41'
        transaction.amount = 2008
        transaction.orderSource = 'telephone'
        transaction.id = 'thisisid'

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Mike'
        billtoaddress.middleInitial = 'J'
        billtoaddress.lastName = 'Hammer'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = fields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '10@BC99999'
        echeck.routingNum = '053100300'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('301', response['echeckSalesResponse']['response'])
        self.assertEquals('Invalid Account Number', response['echeckSalesResponse']['message'])


    def test_table_2_6_42(self):
        # orderId *
        transaction = fields.echeckSale()
        transaction.orderId = '42'
        transaction.amount = 2004
        transaction.orderSource = 'telephone'
        transaction.id = 'thisisid'

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Tom'
        billtoaddress.lastName = 'Black'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = fields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '4099999992'
        echeck.routingNum = '011075150'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('000', response['echeckSalesResponse']['response'])
        self.assertEquals('Approved', response['echeckSalesResponse']['message'])

        # eCheck Void
        transaction = fields.echeckVoid()
        transaction.id = 'thisisid'
        transaction.litleTxnId = response['echeckSalesResponse']['litleTxnId']

        response = online.request(transaction, conf)
        self.assertEquals('000', response['echeckVoidResponse']['response'])
        self.assertEquals('Approved', response['echeckVoidResponse']['message'])



    def test_table_2_6_43(self):
        # orderId *
        transaction = fields.echeckSale()
        transaction.orderId = '43'
        transaction.amount = 2007
        transaction.orderSource = 'telephone'
        transaction.id = 'thisisid'

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Peter'
        billtoaddress.lastName = 'Green'
        billtoaddress.companyName = 'Green Co'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = fields.echeck()
        echeck.accType = 'Corporate'
        echeck.accNum = '6099999992'
        echeck.routingNum = '011075150'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('000', response['echeckSalesResponse']['response'])
        self.assertEquals('Approved', response['echeckSalesResponse']['message'])
        #TODO no accountUpdater element.


    def test_table_2_6_44(self):
        # orderId *
        transaction = fields.echeckSale()
        transaction.orderId = '44'
        transaction.amount = 2009
        transaction.orderSource = 'telephone'
        transaction.id = 'thisisid'

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Peter'
        billtoaddress.lastName = 'Green'
        billtoaddress.companyName = 'Green Co'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = fields.echeck()
        echeck.accType = 'Corporate'
        echeck.accNum = '6099999992'
        echeck.routingNum = '053133052'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('900', response['echeckSalesResponse']['response'])
        self.assertEquals('Invalid Bank Routing Number', response['echeckSalesResponse']['message'])


    def test_table_2_7_45(self):
        # orderId *
        transaction = fields.echeckCredit()
        transaction.orderId = '45'
        transaction.amount = 1001
        transaction.orderSource = 'telephone'
        transaction.id = 'thisisid'

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'John'
        billtoaddress.lastName = 'Smith'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = fields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '10@BC99999'
        echeck.routingNum = '053100300'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('301', response['echeckCreditResponse']['response'])
        self.assertEquals('Invalid Account Number', response['echeckCreditResponse']['message'])


    def test_table_2_7_46(self):
        # orderId *
        transaction = fields.echeckCredit()
        transaction.orderId = '46'
        transaction.amount = 1003
        transaction.orderSource = 'telephone'
        transaction.id = 'thisisid'

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Robert'
        billtoaddress.lastName = 'Jones'
        billtoaddress.companyName = 'Widget Inc'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = fields.echeck()
        echeck.accType = 'Corporate'
        echeck.accNum = '3099999999'
        echeck.routingNum = '011075150'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('000', response['echeckCreditResponse']['response'])
        self.assertEquals('Approved', response['echeckCreditResponse']['message'])

        # eCheck Void
        transaction = fields.echeckVoid()
        transaction.id = 'thisisid'
        transaction.litleTxnId = response['echeckCreditResponse']['litleTxnId']

        response = online.request(transaction, conf)
        self.assertEquals('000', response['echeckVoidResponse']['response'])
        self.assertEquals('Approved', response['echeckVoidResponse']['message'])


    def test_table_2_7_47(self):
        # orderId *
        transaction = fields.echeckCredit()
        transaction.orderId = '47'
        transaction.amount = 1007
        transaction.orderSource = 'telephone'
        transaction.id = 'thisisid'

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Peter'
        billtoaddress.lastName = 'Green'
        billtoaddress.companyName = 'Green Co'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = fields.echeck()
        echeck.accType = 'Corporate'
        echeck.accNum = '6099999993'
        echeck.routingNum = '211370545'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('000', response['echeckCreditResponse']['response'])
        self.assertEquals('Approved', response['echeckCreditResponse']['message'])

    def test_table_2_6_48(self):
        # orderId *
        transaction = fields.echeckSale()
        transaction.orderId = '43'
        transaction.amount = 2007
        transaction.orderSource = 'telephone'
        transaction.id = 'thisisid'

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Peter'
        billtoaddress.lastName = 'Green'
        billtoaddress.companyName = 'Green Co'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = fields.echeck()
        echeck.accType = 'Corporate'
        echeck.accNum = '6099999992'
        echeck.routingNum = '011075150'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)

        transaction = fields.echeckCredit()
        transaction.id = 'thisisid'
        transaction.litleTxnId = response['echeckSalesResponse']['litleTxnId']

        response = online.request(transaction, conf)
        self.assertEquals('000', response['echeckCreditResponse']['response'])
        self.assertEquals('Approved', response['echeckCreditResponse']['message'])


    def test_table_2_6_49(self):
        # orderId *
        transaction = fields.echeckCredit()
        transaction.litleTxnId = '2'
        transaction.id = 'thisisid'

        response = online.request(transaction, conf)
        self.assertEquals('360', response['echeckCreditResponse']['response'])
        self.assertEquals('No transaction found with specified litleTxnId', response['echeckCreditResponse']['message'])

    def test_echeck_void_2_7(self):
        # orderId *
        transaction = fields.echeckVoid()
        transaction.litleTxnId = '2'
        transaction.id = 'thisisid'

        response = online.request(transaction, conf)
        self.assertEquals('000', response['echeckVoidResponse']['response'])


if __name__ == '__main__':
    unittest.main()
