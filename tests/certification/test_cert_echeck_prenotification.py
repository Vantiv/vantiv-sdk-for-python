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
from vantivsdk import (utils, batch, fields)

# package_root = os.path.abspath(os.path.dirname(__file__))
# sys.path.insert(0, package_root)
#
# import certification_test_conf

conf = utils.Configuration()


class TestCertEcheck(unittest.TestCase):
    def test_table_2_5_ECPreNoteSale(self):
        # orderId *
        transactions = batch.Transactions()

        transaction = fields.echeckPreNoteSale()
        transaction.orderId = 'ECPreNoteSale'
        transaction.amount = 3001
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        billtoaddress = fields.contact()
        billtoaddress.name = 'PreNote Sale Corp'
        transaction.billToAddress = billtoaddress

        echeck = fields.echeckType()
        echeck.accType = 'Corporate'
        echeck.accNum = '1092969901'
        echeck.routingNum = '011075150'
        transaction.echeck = echeck

        transactions.add(transaction)

        response = batch.stream(transactions, conf)
        self.assertEquals('000', response['batchResponse']['echeckPreNoteSaleResponse']['response'])
        self.assertEquals('Approved', response['batchResponse']['echeckPreNoteSaleResponse']['message'])

    def test_table_2_5_ECPreNoteCredit(self):
        # orderId *
        transactions = batch.Transactions()

        transaction = fields.echeckPreNoteCredit()
        transaction.orderId = 'ECPreNoteCredit'
        transaction.amount = 3001
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        billtoaddress = fields.contact()
        billtoaddress.name = 'PreNote Credit Corp'
        transaction.billToAddress = billtoaddress

        echeck = fields.echeckType()
        echeck.accType = 'Corporate'
        echeck.accNum = '1099339999'
        echeck.routingNum = '011075150'
        transaction.echeck = echeck

        transactions.add(transaction)

        response = batch.stream(transactions, conf)
        self.assertEquals('000', response['batchResponse']['echeckPreNoteCreditResponse']['response'])
        self.assertEquals('Approved', response['batchResponse']['echeckPreNoteCreditResponse']['message'])

    def test_table_2_5_PreNoteSaleAccNumErr(self):
        # orderId *
        transactions = batch.Transactions()

        transaction = fields.echeckPreNoteSale()
        transaction.orderId = 'PreNoteSaleAccNumErr'
        transaction.amount = 3001
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        billtoaddress = fields.contact()
        billtoaddress.name = 'PreNote Sale Corp'
        transaction.billToAddress = billtoaddress

        echeck = fields.echeckType()
        echeck.accType = 'Corporate'
        echeck.accNum = '10@2969901'
        echeck.routingNum = '011100012'
        transaction.echeck = echeck

        transactions.add(transaction)

        response = batch.stream(transactions, conf)
        self.assertEquals('301', response['batchResponse']['echeckPreNoteSaleResponse']['response'])
        # self.assertEquals('Approved', response['batchResponse']['echeckPreNoteSaleResponse']['message'])

    def test_table_2_5_PreNoteCreditAccNumErr(self):
        # orderId *
        transactions = batch.Transactions()

        transaction = fields.echeckPreNoteCredit()
        transaction.orderId = 'PreNoteCreditAccNumErr'
        transaction.amount = 3001
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        billtoaddress = fields.contact()
        billtoaddress.name = 'PreNote Credit Personal'
        transaction.billToAddress = billtoaddress

        echeck = fields.echeckType()
        echeck.accType = 'Savings'
        echeck.accNum = '10@2969901'
        echeck.routingNum = '011100012'
        transaction.echeck = echeck

        transactions.add(transaction)

        response = batch.stream(transactions, conf)
        self.assertEquals('301', response['batchResponse']['echeckPreNoteCreditResponse']['response'])
        # self.assertEquals('Approved', response['batchResponse']['echeckPreNoteCreditResponse']['message'])

    def test_table_2_5_PreNoteSaleRoutNumErr(self):
        # orderId *
        transactions = batch.Transactions()

        transaction = fields.echeckPreNoteSale()
        transaction.orderId = 'PreNoteSaleRoutNumErr'
        transaction.amount = 3001
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        billtoaddress = fields.contact()
        billtoaddress.name = 'PreNote Sale Personal'
        transaction.billToAddress = billtoaddress

        echeck = fields.echeckType()
        echeck.accType = 'Checking'
        echeck.accNum = '6099999992'
        echeck.routingNum = '053133052'
        transaction.echeck = echeck

        transactions.add(transaction)

        response = batch.stream(transactions, conf)
        self.assertEquals('900', response['batchResponse']['echeckPreNoteSaleResponse']['response'])
        # self.assertEquals('Approved', response['batchResponse']['echeckPreNoteSaleResponse']['message'])

    def test_table_2_5_PreNoteCreditRoutNumErr(self):
        # orderId *
        transactions = batch.Transactions()

        transaction = fields.echeckPreNoteCredit()
        transaction.orderId = 'PreNoteCreditRoutNumErr'
        transaction.amount = 3001
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        billtoaddress = fields.contact()
        billtoaddress.name = 'PreNote Credit Personal'
        transaction.billToAddress = billtoaddress

        echeck = fields.echeckType()
        echeck.accType = 'Checking'
        echeck.accNum = '6099999992'
        echeck.routingNum = '053133052'
        transaction.echeck = echeck

        transactions.add(transaction)

        response = batch.stream(transactions, conf)
        self.assertEquals('900', response['batchResponse']['echeckPreNoteCreditResponse']['response'])
        # self.assertEquals('Approved', response['batchResponse']['echeckPreNoteCreditResponse']['message'])


if __name__ == '__main__':
    unittest.main()
