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


class Test3DSResponses(unittest.TestCase):
    def test_runner(self):
        elements = [
            {
                'orderId': '3DS1',
                'orderSource': '3dsAuthenticated',
                'type': 'VI',
                'number': '4100200300000004',
                'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                'authenticationResult': '0',
            },
            {
                'orderId': '3DS2',
                'orderSource': '3dsAuthenticated',
                'type': 'VI',
                'number': '4100200300000012',
                'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                'authenticationResult': '1',
            },
            {
                'orderId': '3DS3',
                'orderSource': '3dsAuthenticated',
                'type': 'VI',
                'number': '4100200300000103',
                'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                'authenticationResult': '2',
            },
            {
                'orderId': '3DS4',
                'orderSource': '3dsAuthenticated',
                'type': 'VI',
                'number': '4100200300001002',
                'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                'authenticationResult': 'A',
            },
            {
                'orderId': '3DS5',
                'orderSource': '3dsAuthenticated',
                'type': 'VI',
                'number': '4100200300000020',
                'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                'authenticationResult': '3',
            },
            {
                'orderId': '3DS6',
                'orderSource': '3dsAuthenticated',
                'type': 'VI',
                'number': '4100200300000038',
                'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                'authenticationResult': '4',
            },
            {
                'orderId': '3DS7',
                'orderSource': '3dsAuthenticated',
                'type': 'VI',
                'number': '4100200300000046',
                'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                'authenticationResult': '5',
            },
            {
                'orderId': '3DS8',
                'orderSource': '3dsAuthenticated',
                'type': 'VI',
                'number': '4100200300000053',
                'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                'authenticationResult': '6',
            },
            {
                'orderId': '3DS9',
                'orderSource': '3dsAuthenticated',
                'type': 'VI',
                'number': '4100200300000061',
                'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                'authenticationResult': '7',
            },
            {
                'orderId': '3DS10',
                'orderSource': '3dsAuthenticated',
                'type': 'VI',
                'number': '4100200300000079',
                'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                'authenticationResult': '8',
            },
            {
                'orderId': '3DS11',
                'orderSource': '3dsAuthenticated',
                'type': 'VI',
                'number': '4100200300000087',
                'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                'authenticationResult': '9',
            },
            {
                'orderId': '3DS12',
                'orderSource': '3dsAuthenticated',
                'type': 'VI',
                'number': '4100200300000095',
                'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                'authenticationResult': 'B',
            },
            {
                'orderId': '3DS13',
                'orderSource': '3dsAuthenticated',
                'type': 'VI',
                'number': '4100200300000111',
                'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                'authenticationResult': 'C',
            },
            {
                'orderId': '3DS14',
                'orderSource': '3dsAuthenticated',
                'type': 'VI',
                'number': '4100200300000129',
                'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                'authenticationResult': 'D',
            },
            {
                'orderId': '3DS15',
                'orderSource': '3dsAttempted',
                'type': 'MC',
                'number': '5112010200000001',
                'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                'authenticationResult': 'N/A',
            },
            {
                'orderId': '3DS16',
                'orderSource': '3dsAttempted',
                'type': 'MC',
                'number': '5112010200000001',
                'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                'authenticationResult': 'N/A',
            },
            {
                'orderId': 'DI3DS1',
                'orderSource': '3dsAuthenticated',
                'type': 'DI',
                'number': '6011000400001008',
                'authenticationValue': 'BRICAIASNBERERERERERARERERE=',
                'authenticationResult': '0',
            },
            # TODO authenticationResult is 0
            # {
            #     'orderId': 'DI3DS2',
            #     'orderSource': '3dsAuthenticated',
            #     'type': 'DI',
            #     'number': '6011000400000018',
            #     'authenticationValue': 'BRIBAIASNBERERERERERARERERE=',
            #     'authenticationResult': '1',
            # },
            # {
            #     'orderId': 'DI3DS3',
            #     'orderSource': '3dsAuthenticated',
            #     'type': 'DI',
            #     'number': '6011000400000109',
            #     'authenticationValue': 'BRIAAIASNBERERERERERARERERE=',
            #     'authenticationResult': '2',
            # },
        ]

        for element in elements:
            txn = {
                'authorization': {
                    'orderId': element['orderId'],
                    'amount': 12523,
                    'id': 'ids',
                    'reportGroup': 'Planets',
                    'orderSource': element['orderSource'],
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
                    'cardholderAuthentication': {
                        'authenticationValue': element['authenticationValue'],
                    }
                }
            }

            response = online.request(txn, conf)
            if (element['authenticationResult'] == 'N/A'):
                self.assertNotIn('authenticationResult', response['authorizationResponse']['fraudResult'])
            else:
                self.assertEquals(element['authenticationResult'],
                                  response['authorizationResponse']['fraudResult']['authenticationResult'])


if __name__ == '__main__':
    unittest.main()
