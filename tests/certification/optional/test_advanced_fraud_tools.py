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


class TestAdvancedFraudTools(unittest.TestCase):
    def test_tmx_pass_order_id(self):
        txn = {
            'authorization': {
                'orderId': 'tmx_pass_order_id',
                'amount': 150,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '4111111111111111',
                    'expDate': '1230',
                    'type': 'VI',
                },
                'advancedFraudChecks': {
                    'threatMetrixSessionId': 'YourPrefix-A980A93LP2O3-KNP0050'
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
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        # TODO need to change 'threatMetrixSessionId': 'YourPrefix*'
        # self.assertEquals('pass',
        #                   response['authorizationResponse']['fraudResult']['advancedFraudResults']['deviceReviewStatus'])
        # self.assertEquals('50',
        #                   response['authorizationResponse']['fraudResult']['advancedFraudResults']['deviceReputationScore'])
        # self.assertEquals('FlashDisabled',
        #                   response['authorizationResponse']['fraudResult']['advancedFraudResults']['triggeredRule'])

    def test_tmx_review_order_id(self):
        txn = {
            'authorization': {
                'orderId': 'tmx_pass_order_id',
                'amount': 150,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '4111111111111111',
                    'expDate': '1230',
                    'type': 'VI',
                },
                'advancedFraudChecks': {
                    'threatMetrixSessionId': 'YourPrefix-A0S9D8F7G6H5J4-KMR-020'
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
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        # TODO need to change 'threatMetrixSessionId': 'YourPrefix*'
        # self.assertEquals('review',
        #                   response['authorizationResponse']['fraudResult']['advancedFraudResults']['deviceReviewStatus'])
        # self.assertEquals('-20',
        #                   response['authorizationResponse']['fraudResult']['advancedFraudResults']['deviceReputationScore'])
        # self.assertEquals('PossibleVPNConnection',
        #                   response['authorizationResponse']['fraudResult']['advancedFraudResults']['triggeredRule'][0])
        # self.assertEquals('PossibleCookieWipingWeek',
        #                   response['authorizationResponse']['fraudResult']['advancedFraudResults']['triggeredRule'][1])

    def test_tmx_fail_order_id(self):
        txn = {
            'authorization': {
                'orderId': 'tmx_fail_order_id',
                'amount': 150,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '4111111111111111',
                    'expDate': '1230',
                    'type': 'VI',
                },
                'advancedFraudChecks': {
                    'threatMetrixSessionId': 'YourPrefix-Q1W2E3R4T5Y6U7I8-KHF-100'
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
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        # TODO need to change 'threatMetrixSessionId': 'YourPrefix*'
        # self.assertEquals('fail',
        #                   response['authorizationResponse']['fraudResult']['advancedFraudResults']['deviceReviewStatus'])
        # self.assertEquals('-100',
        #                   response['authorizationResponse']['fraudResult']['advancedFraudResults']['deviceReputationScore'])
        # self.assertEquals('5PaymentsOnExactDevice',
        #                   response['authorizationResponse']['fraudResult']['advancedFraudResults']['triggeredRule'][0])
        # self.assertEquals('ProxyHasNegativeReputation',
        #                   response['authorizationResponse']['fraudResult']['advancedFraudResults']['triggeredRule'][1])
        # self.assertEquals('TrueIPProxyIPCityMismatch',
        #                   response['authorizationResponse']['fraudResult']['advancedFraudResults']['triggeredRule'][2])

    def test_tmx_unavail_order_id(self):
        txn = {
            'authorization': {
                'orderId': 'tmx_unavail_order_id',
                'amount': 150,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '4111111111111111',
                    'expDate': '1230',
                    'type': 'VI',
                },
                'advancedFraudChecks': {
                    'threatMetrixSessionId': 'YourPrefix-Q1W2E3R4T5Y6U7I8-XLP0050'
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
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        # TODO need to change 'threatMetrixSessionId': 'YourPrefix*'
        # self.assertEquals('unavailable',
        #                   response['authorizationResponse']['fraudResult']['advancedFraudResults']['deviceReviewStatus'])


if __name__ == '__main__':
    unittest.main()
