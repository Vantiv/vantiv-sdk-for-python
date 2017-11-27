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


class TestAddressResponse(unittest.TestCase):
    def test_AVS1(self):
        txn = {
            'authorization': {
                'orderId': 'AVS1',
                'amount': 0,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'type': 'VI',
                    'number': '4457000600000004',
                },
                'billToAddress': {
                    'addressLine1': '95 Main St.',
                    'zip': '95022',
                },
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('00', response['authorizationResponse']['fraudResult']['avsResult'])

    def test_AVS2(self):
        txn = {
            'authorization': {
                'orderId': 'AVS2',
                'amount': 0,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'type': 'VI',
                    'number': '4457000600000004',
                },
                'billToAddress': {
                    'addressLine1': '95 Main St.',
                    'zip': '950221111',
                },
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('01', response['authorizationResponse']['fraudResult']['avsResult'])

    def test_AVS3(self):
        txn = {
            'authorization': {
                'orderId': 'AVS3',
                'amount': 0,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'type': 'VI',
                    'number': '4457000600000004',
                },
                'billToAddress': {
                    'addressLine1': '100 Main St.',
                    'zip': '95022',
                },
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('10', response['authorizationResponse']['fraudResult']['avsResult'])

    def test_AVS4(self):
        txn = {
            'authorization': {
                'orderId': 'AVS4',
                'amount': 0,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'type': 'VI',
                    'number': '4457000600000004',
                },
                'billToAddress': {
                    'addressLine1': '100 Main St.',
                    'zip': '02134',
                },
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('20', response['authorizationResponse']['fraudResult']['avsResult'])


if __name__ == '__main__':
    unittest.main()
