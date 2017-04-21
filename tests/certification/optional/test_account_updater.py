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


class TestAccountUpdater(unittest.TestCase):
    def test_100(self):
        txn = {
            'authorization': {
                'orderId': '100',
                'amount': 10000,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '4457000300000007',
                    'expDate': '0115',
                    'type': 'VI'
                },
            }
        }

        response = online.request(txn, conf)
        # TODO no accountUpdater in response
        # self.assertEquals('VI',
        #                   response['authorizationResponse']['accountUpdater']['originalCardInfo']['type'])
        # self.assertEquals('4457000300000007',
        #                   response['authorizationResponse']['accountUpdater']['originalCardInfo']['number'])
        # self.assertEquals('0115',
        #                   response['authorizationResponse']['accountUpdater']['originalCardInfo']['expDate'])
        # self.assertEquals('MC',
        #                   response['authorizationResponse']['accountUpdater']['newCardInfo']['type'])
        # self.assertEquals('5112000100000003',
        #                   response['authorizationResponse']['accountUpdater']['newCardInfo']['number'])
        # self.assertEquals('0115',
        #                   response['authorizationResponse']['accountUpdater']['newCardInfo']['expDate'])

    def test_101(self):
        txn = {
            'authorization': {
                'orderId': '101',
                'amount': 10000,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '6500102087026221',
                    'expDate': '0115',
                    'type': 'DI'
                },
            }
        }

        response = online.request(txn, conf)
        # TODO no accountUpdater in response
        # self.assertEquals('DI',
        #                   response['authorizationResponse']['accountUpdater']['originalCardInfo']['type'])
        # self.assertEquals('6500102087026221',
        #                   response['authorizationResponse']['accountUpdater']['originalCardInfo']['number'])
        # self.assertEquals('0115',
        #                   response['authorizationResponse']['accountUpdater']['originalCardInfo']['expDate'])
        # self.assertEquals('DI',
        #                   response['authorizationResponse']['accountUpdater']['newCardInfo']['type'])
        # self.assertEquals('6011102077026225',
        #                   response['authorizationResponse']['accountUpdater']['newCardInfo']['number'])
        # self.assertEquals('0115',
        #                   response['authorizationResponse']['accountUpdater']['newCardInfo']['expDate'])


if __name__ == '__main__':
    unittest.main()
