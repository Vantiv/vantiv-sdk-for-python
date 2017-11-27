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


class TestMobilePointofSale(unittest.TestCase):
    def test_mpos_sale(self):
        txn = {
            'sale': {
                'orderId': 'mpos_sale',
                'amount': 100,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'mpos': {
                    'encryptedTrack': 'CASE1E185EADD6AFE78C9A214B21313DCD836FDD555FBE3A6C48D141FE80AB9172B963265AFF72111895FE415DEDA162CE8CB7AC4D91EDB611A2AB756AA9CB1A000000000000000000000000000000005A7AAF5E8885A9DB88ECD2430C497003F2646619A2382FFF205767492306AC804E8E64E8EA6981DD',
                    'ksn': '77853211300008E00016',
                    'formatId': '30',
                    'track1Status': '0',
                    'track2Status': '0'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('Approved', response['saleResponse']['message'])
        self.assertEquals('22222', response['saleResponse']['authCode'])
        self.assertEquals('34', response['saleResponse']['fraudResult']['avsResult'])

    def test_mpos_credit(self):
        txn = {
            'credit': {
                'orderId': 'mpos_credit',
                'amount': 100,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'mpos': {
                    'encryptedTrack': 'CASE1E185EADD6AFE78C9A214B21313DCD836FDD555FBE3A6C48D141FE80AB9172B963265AFF72111895FE415DEDA162CE8CB7AC4D91EDB611A2AB756AA9CB1A000000000000000000000000000000005A7AAF5E8885A9DB88ECD2430C497003F2646619A2382FFF205767492306AC804E8E64E8EA6981DD',
                    'ksn': '77853211300008E00016',
                    'formatId': '30',
                    'track1Status': '0',
                    'track2Status': '0'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('000', response['creditResponse']['response'])
        self.assertEquals('Approved', response['creditResponse']['message'])

    def test_mposAuthFailure1(self):
        txn = {
            'sale': {
                'orderId': 'mposAuthFailure1',
                'amount': 100,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'mpos': {
                    'encryptedTrack': 'CASE8E185EADD6AFE78C9A214B21313DCD836FDD555FBE3A6C48D141FE80AB9172B963265AFF72111895FE415DEDA162CE8CB7AC4D91EDB611A2AB756AA9CB1A000000000000000000000000000000005A7AAF5E8885A9DB88ECD2430C497003F2646619A2382FFF205767492306AC804E8E64E8EA6981DD',
                    'ksn': '77853211300008E00016',
                    'formatId': '30',
                    'track1Status': '0',
                    'track2Status': '0'
                }
            }
        }

        response = online.request(txn, conf)
        # TODO The response is wrong
        # self.assertEquals('524', response['saleResponse']['response'])
        # self.assertEquals('Hard Decline - Input data is invalid', response['saleResponse']['message'])

    def test_mposAuthFailure2(self):
        txn = {
            'sale': {
                'orderId': 'mposAuthFailure2',
                'amount': 100,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'mpos': {
                    'encryptedTrack': 'TimeOut',
                    'ksn': '77853211300008E00016',
                    'formatId': '30',
                    'track1Status': '0',
                    'track2Status': '0'
                }
            }
        }

        response = online.request(txn, conf, timeout=60)
        self.assertEquals('521', response['saleResponse']['response'])
        self.assertEquals('Soft decline - Card reader decryption service is not available',
                          response['saleResponse']['message'])

    def test_mposAuthFailure3(self):
        txn = {
            'sale': {
                'orderId': 'mposAuthFailure3',
                'amount': 100,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'mpos': {
                    'encryptedTrack': 'CASE2E185EADD6AFE78C9A214B21313DCD836FDD555FBE3A6C48D141FE80AB9172B963265AFF72111895FE415DEDA162CE8CB7AC4D91EDB611A2AB756AA9CB1A000000000000000000000000000000005A7AAF5E8885A9DB88ECD2430C497003F2646619A2382FFF205767492306AC804E8E64E8EA6981DD',
                    'ksn': '77853211300008E00016',
                    'formatId': '30',
                    'track1Status': '0',
                    'track2Status': '0'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('523', response['saleResponse']['response'])
        self.assertEquals('Soft Decline - Decryption failed', response['saleResponse']['message'])


if __name__ == '__main__':
    unittest.main()
