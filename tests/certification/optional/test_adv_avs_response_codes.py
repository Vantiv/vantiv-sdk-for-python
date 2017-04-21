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

package_root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, package_root)

import certification_test_conf

conf = certification_test_conf.conf


class TestResponseReasonCodesandMessages(unittest.TestCase):
    def test_RRC_card(self):
        elements = [
            {
                'type': 'VI',
                'number': '4457000800000002',
                'response': '000',
                'message': 'Approved'
            },
            {
                'type': 'VI',
                'number': '4457000900000001',
                'response': '000',
                'message': 'Approved'
            },
            {
                'type': 'VI',
                'number': '4457001000000008',
                'response': '000',
                'message': 'Approved'
            },
            {
                'type': 'MC',
                'number': '5112000900000005',
                'response': '000',
                'message': 'Approved'
            },
            {
                'type': 'AX',
                'number': '375000030000001',
                'response': '120',
                'message': 'Call Issuer'
            },
            {
                'type': 'DI',
                'number': '6011000400000000',
                'response': '123',
                'message': 'Call Discover'
            },
            {
                'type': 'VI',
                'number': '4457001200000006',
                'response': '120',
                'message': 'Call Issuer'
            },
            {
                'type': 'VI',
                'number': '4457001300000005',
                'response': '120',
                'message': 'Call Issuer'
            },
            {
                'type': 'VI',
                'number': '4457001400000004',
                'response': '120',
                'message': 'Call Issuer'
            },
            {
                'type': 'MC',
                'number': '5112001000000002',
                'response': '101',
                'message': 'Issuer Unavailable'
            },
            {
                'type': 'VI',
                'number': '4457001900000009',
                'response': '321',
                'message': 'Invalid Merchant'
            },
            {
                'type': 'VI',
                'number': '4457002000000006',
                'response': '303',
                'message': 'Pick Up Card'
            },
            {
                'type': 'VI',
                'number': '4457002100000005',
                'response': '110',
                'message': 'Insufficient Funds'
            },
            {
                'type': 'VI',
                'number': '4457002200000004',
                'response': '120',
                'message': 'Call Issuer'
            },
            {
                'type': 'AX',
                'number': '375000050000006',
                'response': '350',
                'message': 'Generic Decline'
            },
            {
                'type': 'VI',
                'number': '4457002300000003',
                'response': '349',
                'message': 'Do Not Honor'
            },
            {
                'type': 'VI',
                'number': '4457002500000001',
                'response': '340',
                'message': 'Invalid Amount'
            },
            {
                'type': 'MC',
                'number': '5112001600000006',
                'response': '301',
                'message': 'Invalid Account Number'
            },
            {
                'type': 'MC',
                'number': '5112001700000005',
                'response': '301',
                'message': 'Invalid Account Number'
            },
            {
                'type': 'MC',
                'number': '5112001800000004',
                'response': '321',
                'message': 'Invalid Merchant'
            },
            {
                'type': 'VI',
                'number': '4457002700000009',
                'response': '101',
                'message': 'Issuer Unavailable'
            },
            {
                'type': 'MC',
                'number': '5112001900000003',
                'response': '305',
                'message': 'Expired Card'
            },
            {
                'type': 'VI',
                'number': '4457002800000008',
                'response': '322',
                'message': 'Invalid Transaction'
            },
            {
                'type': 'VI',
                'number': '4457002900000007',
                'response': '350',
                'message': 'Generic Decline'
            },
            {
                'type': 'VI',
                'number': '4457003000000004',
                'response': '101',
                'message': 'Issuer Unavailable'
            },
            {
                'type': 'MC',
                'number': '5112002000000000',
                'response': '101',
                'message': 'Issuer Unavailable'
            },
            {
                'type': 'VI',
                'number': '4457000100000000',
                'response': '301',
                'message': 'Invalid Account Number'
            },
        ]

        for element in elements:
            txn = {
                'authorization': {
                    'orderId': 'RRC-%s' % element['number'],
                    'amount': 12523,
                    'id': 'ids',
                    'reportGroup': 'Planets',
                    'orderSource': 'ecommerce',
                    'card': {
                        'number': element['number'],
                        'type': element['type']
                    },
                    'billToAddress': {
                        'name': 'John Doe',
                        'addressLine1': '95 Main St.',
                        'city': 'Palo Alto',
                        'state': 'CA',
                        'zip': '950221111',
                        'country': 'US',
                        'email': 'test@test.com',
                        'phone': '6178675309'
                    },
                }
            }

            response = online.request(txn, conf)
            self.assertEquals(element['response'], response['authorizationResponse']['response'])
            self.assertEquals(element['message'], response['authorizationResponse']['message'])


if __name__ == '__main__':
    unittest.main()
