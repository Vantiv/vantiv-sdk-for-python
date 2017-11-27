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

package_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
sys.path.insert(0, package_root)
from vantivsdk import (utils, batch, fields)

# package_root = os.path.abspath(os.path.dirname(__file__))
# sys.path.insert(0, package_root)
#
# import certification_test_conf

conf = utils.Configuration()


class TestCertEcheckPrenotificationDict(unittest.TestCase):
    def test_table_2_5_ECPreNoteSale(self):
        txn_dict = {
            'echeckPreNoteSale' :
            [
                {
                    'orderId' : 'ECPreNoteSale',
                    'orderSource' : 'ecommerce',
                    'id' : 'thisisid',
                    'billToAddress' : {
                        'name': 'PreNote Sale Corp',
                    },
                    'echeck': {
                        'accType':'Corporate',
                        'accNum': '1092969901',
                        'routingNum': '011075150',
                    }
                }
            ],
        }
        response = batch.stream(txn_dict, conf)
        self.assertEquals('000', response['batchResponse']['echeckPreNoteSaleResponse']['response'])
        self.assertEquals('Approved', response['batchResponse']['echeckPreNoteSaleResponse']['message'])

    def test_table_2_5_ECPreNoteCredit(self):
        txn_dict = {
            'echeckPreNoteCredit' :
            [
                {
                    'orderId' : 'ECPreNoteCredit',
                    'orderSource' : 'ecommerce',
                    'id' : 'thisisid',
                    'billToAddress' : {
                        'name': 'PreNote Credit Corp',
                    },
                    'echeck': {
                        'accType':'Corporate',
                        'accNum': '1099339999',
                        'routingNum': '011075150',
                    }
                }
            ],
        }
        response = batch.stream(txn_dict, conf)
        self.assertEquals('000', response['batchResponse']['echeckPreNoteCreditResponse']['response'])
        self.assertEquals('Approved', response['batchResponse']['echeckPreNoteCreditResponse']['message'])

    def test_table_2_5_PreNoteSaleAccNumErr(self):
        txn_dict = {
            'echeckPreNoteSale' :
            [
                {
                    'orderId' : 'PreNoteSaleAccNumErr',
                    'orderSource' : 'ecommerce',
                    'id' : 'thisisid',
                    'billToAddress' : {
                        'name': 'PreNote Sale Corp',
                    },
                    'echeck': {
                        'accType':'Corporate',
                        'accNum': '10@2969901',
                        'routingNum': '011100012',
                    }
                }
            ],
        }
        response = batch.stream(txn_dict, conf)

        self.assertEquals('301', response['batchResponse']['echeckPreNoteSaleResponse']['response'])
        # self.assertEquals('Approved', response['batchResponse']['echeckPreNoteSaleResponse']['message'])

    def test_table_2_5_PreNoteCreditAccNumErr(self):
        txn_dict = {
            'echeckPreNoteCredit' :
            [
                {
                    'orderId' : 'PreNoteCreditAccNumErr',
                    'orderSource' : 'ecommerce',
                    'id' : 'thisisid',
                    'billToAddress' : {
                        'name': 'PreNote Credit Personal',
                    },
                    'echeck': {
                        'accType':'Savings',
                        'accNum': '10@2969901',
                        'routingNum': '011100012',
                    }
                }
            ],
        }
        response = batch.stream(txn_dict, conf)
        self.assertEquals('301', response['batchResponse']['echeckPreNoteCreditResponse']['response'])
        # self.assertEquals('Approved', response['batchResponse']['echeckPreNoteCreditResponse']['message'])

    def test_table_2_5_PreNoteSaleRoutNumErr(self):
        txn_dict = {
            'echeckPreNoteSale' :
            [
                {
                    'orderId' : 'PreNoteSaleRoutNumErr',
                    'orderSource' : 'ecommerce',
                    'id' : 'thisisid',
                    'billToAddress' : {
                        'name': 'PreNote Sale Personal',
                    },
                    'echeck': {
                        'accType':'Checking',
                        'accNum': '6099999992',
                        'routingNum': '053133052',
                    }
                }
            ],
        }
        response = batch.stream(txn_dict, conf)
        self.assertEquals('900', response['batchResponse']['echeckPreNoteSaleResponse']['response'])
        # self.assertEquals('Approved', response['batchResponse']['echeckPreNoteSaleResponse']['message'])

    def test_table_2_5_PreNoteCreditRoutNumErr(self):
        txn_dict = {
            'echeckPreNoteCredit' :
            [
                {
                    'orderId' : 'PreNoteCreditRoutNumErr',
                    'orderSource' : 'ecommerce',
                    'id' : 'thisisid',
                    'billToAddress' : {
                        'name': 'PreNote Credit Personal',
                    },
                    'echeck': {
                        'accType':'Checking',
                        'accNum': '6099999992',
                        'routingNum': '053133052',
                    }
                }
            ],
        }
        response = batch.stream(txn_dict, conf)
        self.assertEquals('900', response['batchResponse']['echeckPreNoteCreditResponse']['response'])
        # self.assertEquals('Approved', response['batchResponse']['echeckPreNoteCreditResponse']['message'])


if __name__ == '__main__':
    unittest.main()
