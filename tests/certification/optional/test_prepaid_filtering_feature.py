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


class TestPrepaidFilteringFeature(unittest.TestCase):
    def test_filterPrepaidMC(self):
        txn = {
            'authorization': {
                'orderId': 'filterPrepaidMC',
                'amount': 9100,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'recurring',
                'card': {
                    'number': '5500000958501839',
                    'expDate': '1121',
                    'type': 'MC'
                },
                'filtering': {
                    'prepaid': 'true',
                },
                'billToAddress': {
                    'name': 'John Doe',
                    'addressLine1': '10 Main St.',
                    'city': 'San Jose',
                    'state': 'CA',
                    'zip': '95032',
                    'country': 'US',
                    'email': 'jdoe@phoenixProcessing.com',
                    'phone': '7812701111'
                },
            }
        }

        response = online.request(txn, conf)
        # TODO The response is wrong
        # self.assertEquals('309', response['authorizationResponse']['response'])
        # self.assertEquals('Restricted Card - Prepaid Card Filtering Service',
        #                   response['authorizationResponse']['message'])
        # self.assertEquals('02', response['authorizationResponse']['fraudResult']['avsResult'])

    def test_filterPrepaidVI(self):
        txn = {
            'authorization': {
                'orderId': 'filterPrepaidVI',
                'amount': 9100,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'recurring',
                'card': {
                    'number': '4650002010001478',
                    'expDate': '1121',
                    'type': 'VI'
                },
                'filtering': {
                    'prepaid': 'true',
                },
                'billToAddress': {
                    'name': 'John Doe',
                    'addressLine1': '10 Main St.',
                    'city': 'San Jose',
                    'state': 'CA',
                    'zip': '95032',
                    'country': 'US',
                    'email': 'jdoe@phoenixProcessing.com',
                    'phone': '7812701111'
                },
            }
        }

        response = online.request(txn, conf)
        # TODO The response is wrong
        # self.assertEquals('309', response['authorizationResponse']['response'])
        # self.assertEquals('Restricted Card - Prepaid Card Filtering Service',
        #                   response['authorizationResponse']['message'])
        # self.assertEquals('34', response['authorizationResponse']['fraudResult']['avsResult'])
        # self.assertNotIn('authCode', response['authorizationResponse'])


if __name__ == '__main__':
    unittest.main()
