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


class TestGiftCardTxns(unittest.TestCase):
    def test_2_27_gc1(self):
        txn = {
            'activate': {
                'orderId': 'GC1',
                'amount': 15000,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '5896299633000001135',
                    'cardValidationNum': '123',
                    # 'pin': '3230',
                    'expDate': '1220',
                    'type': 'GC'
                }
            }
        }

        response = online.request(txn, conf)
        # TODO Processing Network Unavailable
        # self.assertEquals('000', response['activateResponse']['response'])
        # self.assertEquals('Approved', response['activateResponse']['message'])
        # self.assertEquals('M', response['activateResponse']['fraudResult']['cardValidationResult'])
        # self.assertEquals('15000', response['activateResponse']['giftCardResponse']['availableBalance'])

    def test_2_27_gc1a(self):
        txn = {
            'activate': {
                'orderId': 'GC1A',
                'amount': 8000,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'virtualGiftCard': {
                    'accountNumberLength': 16,
                    'giftCardBin': '123',
                }
            }
        }

        response = online.request(txn, conf)
        # TODO Processing Network Unavailable+
        # self.assertEquals('000', response['activateResponse']['response'])
        # self.assertEquals('Approved', response['activateResponse']['message'])
        # self.assertEquals('8000', response['activateResponse']['virtualGiftCardResponse']['availableBalance'])
        # self.assertIn('603571', response['activateResponse']['virtualGiftCardResponse']['accountNumber'])

    def test_2_27_gc2(self):
        txn = {
            'authorization': {
                'orderId': 'GC2',
                'amount': 1500,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '5896299633000001135',
                    'cardValidationNum': '123',
                    # 'pin': '3230',
                    'expDate': '1220',
                    'type': 'GC'
                }
            }
        }

        response = online.request(txn, conf)
        # TODO Processing Network Unavailable
        # self.assertEquals('000', response['authorizationResponse']['response'])
        # self.assertEquals('Approved', response['authorizationResponse']['message'])
        # self.assertEquals('11111', response['authorizationResponse']['authCode'])
        # self.assertEquals('M', response['authorizationResponse']['fraudResult']['cardValidationResult'])
        # self.assertEquals('13500', response['authorizationResponse']['giftCardResponse']['availableBalance'])
        # # GC2A Gift Card Capture
        # txn = {
        #     'giftCardCapture': {
        #         'orderId': 'GC2A',
        #         'id': 'ids',
        #         'reportGroup': 'Planets',
        #         'orderSource': 'ecommerce',
        #         'cnpTxnId': response['authorizationResponse']['cnpTxnId'],
        #         'captureAmount': 1500,
        #         'card': {
        #             'number': '5896299633000001135',
        #             'cardValidationNum': '123',
        #             # 'pin': '3230',
        #             'expDate': '1220',
        #             'type': 'GC'
        #         },
        #         'originalRefCode': response['authorizationResponse']['giftCardResponse']['refCode'],
        #         'originalAmount': 1500,
        #         'originalTxnTime': response['authorizationResponse']['giftCardResponse']['txnTime'],
        #     }
        # }
        # response_gc2a = online.request(txn, conf)
        # self.assertEquals('000', response_gc2a['giftCardCaptureResponse']['response'])
        # self.assertEquals('Approved', response_gc2a['giftCardCaptureResponse']['message'])
        # # GC2B Gift Card Credit
        # txn = {
        #     'giftCardCredit': {
        #         'orderId': 'GC2A',
        #         'id': 'ids',
        #         'reportGroup': 'Planets',
        #         'orderSource': 'ecommerce',
        #         'cnpTxnId': response_gc2a['giftCardCaptureResponse']['cnpTxnId'],
        #         'creditAmount': 500,
        #         'card': {
        #             'number': '5896299633000001135',
        #             'expDate': '1220',
        #             'type': 'GC'
        #         },
        #     }
        # }
        # response_gc2b = online.request(txn, conf)
        # TODO Processing Network Unavailable
        # self.assertEquals('000', response_gc2b['giftCardCreditResponse']['response'])
        # self.assertEquals('Approved', response_gc2b['giftCardCreditResponse']['message'])

    def test_2_27_gc3(self):
        txn = {
            'deactivate': {
                'orderId': 'CG3',
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '5896299633000001135',
                    'type': 'GC'
                }
            }
        }

        response = online.request(txn, conf)
        # TODO Processing Network Unavailable
        # self.assertEquals('000', response['deactivateResponse']['response'])
        # self.assertEquals('Approved', response['deactivateResponse']['message'])
        # self.assertEquals('0', response['deactivateResponse']['giftCardResponse']['availableBalance'])


if __name__ == '__main__':
    unittest.main()
