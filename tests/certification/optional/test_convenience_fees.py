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

from vantivsdk import *

package_root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, package_root)

import certification_test_conf

conf = certification_test_conf.conf


class TestConvenienceFees(unittest.TestCase):
    def test_Visa_secondaryAmount(self):
        txn = {
            'authorization': {
                'orderId': 'Visa_secondaryAmount',
                'amount': 10500,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'secondaryAmount': '10000',
                'card': {
                    'number': '4457010200000247',
                    'expDate': '1121',
                    'type': 'VI'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])

    def test_SecondaryAmt_Higher(self):
        txn = {
            'authorization': {
                'orderId': 'SecondaryAmt_Higher',
                'amount': 2500,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'secondaryAmount': '3000',
                'card': {
                    'number': '4111111111111111',
                    'expDate': '1230',
                    'type': 'VI'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('380', response['authorizationResponse']['response'])
        self.assertEquals('Secondary amount cannot exceed the sale amount',
                          response['authorizationResponse']['message'])

    def test_MOP_Unsupported(self):
        txn = {
            'authorization': {
                'orderId': 'MOP_Unsupported',
                'amount': 6002,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'secondaryAmount': '1100',
                'card': {
                    'number': '375001010000003',
                    'expDate': '0421',
                    'type': 'AX'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('381', response['authorizationResponse']['response'])
        self.assertEquals('This method of payment does not support secondary amount',
                          response['authorizationResponse']['message'])

    def test_Negative_Secondary(self):
        txn = {
            'authorization': {
                'orderId': 'Negative_Secondary',
                'amount': 1000,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'secondaryAmount': '-500',
                'card': {
                    'number': '4457010200000247',
                    'expDate': '1121',
                    'type': 'VI'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('382', response['authorizationResponse']['response'])
        self.assertEquals('Secondary amount cannot be less than zero',
                          response['authorizationResponse']['message'])

    def test_Partial_Not_Allowed(self):
        txn = {
            'authorization': {
                'orderId': 'Partial_Not_Allowed',
                'amount': 2500,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'secondaryAmount': '3000',
                'allowPartialAuth': 'true',
                'card': {
                    'number': '4111111111111111',
                    'expDate': '1230',
                    'type': 'VI'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('383', response['authorizationResponse']['response'])
        self.assertEquals('Partial transaction is not supported when including a secondary amount',
                          response['authorizationResponse']['message'])

    def test_SaleWOSecondary(self):
        txn = {
            'sale': {
                'orderId': 'SaleWOSecondary',
                'amount': 1000,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '5112010140000004',
                    'expDate': '1121',
                    'type': 'MC'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('Approved', response['saleResponse']['message'])

        txn = {
            'credit': {
                'litleTxnId': response['saleResponse']['litleTxnId'],
                'amount': 1000,
                'secondaryAmount': 400,
                'id': 'ids',
                # 'reportGroup': 'Planets',
                # 'orderSource' : 'ecommerce',
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('000', response['creditResponse']['response'])
        self.assertEquals('Approved', response['creditResponse']['message'])


if __name__ == '__main__':
    unittest.main()
