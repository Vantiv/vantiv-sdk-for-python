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


class TestCertEcheckDict(unittest.TestCase):
    def test_table_2_2_32(self):
        txn_dict = {
            'authorization': {
                'orderId': '32',
                'amount': 10010,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'billToAddress': {
                    'name': 'John Smith',
                    'addressLine1': '1 Main St.',
                    'city': 'Burlington',
                    'state': 'MA',
                    'zip': '01803-3747',
                    'country': 'USA',
                },
                'card': {
                    'number': '4457010000000009',
                    'expDate': '0121',
                    'cardValidationNum': '349',
                    'type': 'VI',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('11111', response['authorizationResponse']['authCode'])
        self.assertEquals('01', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('M', response['authorizationResponse']['fraudResult']['cardValidationResult'])

        # orderId *A
        txn_dict = {
            'capture': {
                'cnpTxnId': response['authorizationResponse']['cnpTxnId'],
                'id': 'ThisIsID',
                'amount': 5050,
            }
        }
        captureresponse = online.request(txn_dict, conf)
        self.assertEquals('000', captureresponse['captureResponse']['response'])
        self.assertEquals('Approved', captureresponse['captureResponse']['message'])

        # orderId *B
        txn_dict = {
            'authReversal': {
                'cnpTxnId': response['authorizationResponse']['cnpTxnId'],
                'id': 'ThisIsID',
            }
        }
        authreversalresponse = online.request(txn_dict, conf)
        self.assertEquals('000', authreversalresponse['authReversalResponse']['response'])
        self.assertEquals('Approved', authreversalresponse['authReversalResponse']['message'])

    def test_table_2_2_33(self):
        txn_dict = {
            'authorization': {
                'orderId': '33',
                'amount': 20020,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'billToAddress': {
                    'name': 'Mike J. Hammer',
                    'addressLine1': '2 Main St.',
                    'addressLine2': 'Apt. 222',
                    'city': 'Riverside',
                    'state': 'RI',
                    'zip': '02915',
                    'country': 'USA',
                },
                'card': {
                    'number': '5112010000000003',
                    'expDate': '0221',
                    'cardValidationNum': '261',
                    'type': 'MC',
                },
                'cardholderAuthentication':{
                    'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('22222', response['authorizationResponse']['authCode'])
        self.assertEquals('10', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('M', response['authorizationResponse']['fraudResult']['cardValidationResult'])
        self.assertNotIn('authenticationResult', response['authorizationResponse']['fraudResult'])

        # orderId *A
        txn_dict = {
            'authReversal': {
                'cnpTxnId': response['authorizationResponse']['cnpTxnId'],
                'id': 'ThisIsID',
            }
        }
        authreversalresponse = online.request(txn_dict, conf)

        self.assertEquals('000', authreversalresponse['authReversalResponse']['response'])
        self.assertEquals('Approved', authreversalresponse['authReversalResponse']['message'])

    def test_table_2_2_34(self):
        txn_dict = {
            'authorization': {
                'orderId': '34',
                'amount': 10010,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'billToAddress': {
                    'name': 'Eileen Jones',
                    'addressLine1': '3 Main St.',
                    'city': 'Bloomfield',
                    'state': 'CT',
                    'zip': '06002',
                    'country': 'USA',
                },
                'card': {
                    'number': '6011010000000003',
                    'expDate': '0321',
                    'cardValidationNum': '758',
                    'type': 'DI',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('33333', response['authorizationResponse']['authCode'])
        self.assertEquals('10', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('M', response['authorizationResponse']['fraudResult']['cardValidationResult'])

        # orderId *A
        txn_dict = {
            'authReversal': {
                'cnpTxnId': response['authorizationResponse']['cnpTxnId'],
                'id': 'ThisIsID',
            }
        }
        authreversalresponse = online.request(txn_dict, conf)
        self.assertEquals('000', authreversalresponse['authReversalResponse']['response'])
        self.assertEquals('Approved', authreversalresponse['authReversalResponse']['message'])

    def test_table_2_2_35(self):
        txn_dict = {
            'authorization': {
                'orderId': '35',
                'amount': 10010,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'billToAddress': {
                    'name': 'Bob Black',
                    'addressLine1': '4 Main St.',
                    'city': 'Laurel',
                    'state': 'MD',
                    'zip': '20708',
                    'country': 'USA',
                },
                'card': {
                    'number': '375001000000005',
                    'expDate': '0421',
                    'type': 'AX',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('44444', response['authorizationResponse']['authCode'])
        self.assertEquals('13', response['authorizationResponse']['fraudResult']['avsResult'])

        # orderId *A
        txn_dict = {
            'capture': {
                'cnpTxnId': response['authorizationResponse']['cnpTxnId'],
                'id': 'ThisIsID',
                'amount': 5050,
            }
        }
        captureresponse = online.request(txn_dict, conf)
        self.assertEquals('000', captureresponse['captureResponse']['response'])
        self.assertEquals('Approved', captureresponse['captureResponse']['message'])

        # orderId *B
        txn_dict = {
            'authReversal': {
                'cnpTxnId': response['authorizationResponse']['cnpTxnId'],
                'id': 'ThisIsID',
                'amount': 5050,
            }
        }

        authreversalresponse = online.request(txn_dict, conf)

        self.assertEquals('000', authreversalresponse['authReversalResponse']['response'])
        self.assertEquals('Approved', authreversalresponse['authReversalResponse']['message'])

    def test_table_2_2_36(self):
        txn_dict = {
            'authorization': {
                'orderId': '36',
                'amount': 20500,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'number': '375000026600004',
                    'expDate': '0521',
                    'type': 'AX',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])

        # orderId *A
        txn_dict = {
            'authReversal': {
                'cnpTxnId': response['authorizationResponse']['cnpTxnId'],
                'id': 'ThisIsID',
                'amount': 10000,
            }
        }
        authreversalresponse = online.request(txn_dict, conf)
        self.assertEquals('000', authreversalresponse['authReversalResponse']['response'])
        self.assertEquals('Approved', authreversalresponse['authReversalResponse']['message'])


if __name__ == '__main__':
    unittest.main()
