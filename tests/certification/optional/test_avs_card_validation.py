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


class TestAVSandCardValidation(unittest.TestCase):
    def test_65(self):
        txn = {
            'authorization': {
                'orderId': '65',
                'amount': 0,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '4457000300000007',
                    'cardValidationNum': '123',
                    # 'pin': '3230',
                    'expDate': '1220',
                    'type': 'VI'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('00', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('U', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_66(self):
        txn = {
            'authorization': {
                'orderId': '66',
                'amount': 0,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '4457000100000009',
                    'cardValidationNum': '123',
                    # 'pin': '3230',
                    'expDate': '1220',
                    'type': 'VI'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('01', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('M', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_67(self):
        txn = {
            'authorization': {
                'orderId': '67',
                'amount': 0,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '4457003100000003',
                    'cardValidationNum': '123',
                    # 'pin': '3230',
                    'expDate': '1220',
                    'type': 'VI'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('02', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('M', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_68(self):
        txn = {
            'authorization': {
                'orderId': '68',
                'amount': 0,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '4457000400000006',
                    'cardValidationNum': '123',
                    # 'pin': '3230',
                    'expDate': '1220',
                    'type': 'VI'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('10', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('S', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_69(self):
        txn = {
            'authorization': {
                'orderId': '69',
                'amount': 0,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '4457000200000008',
                    'cardValidationNum': '123',
                    # 'pin': '3230',
                    'expDate': '1220',
                    'type': 'VI'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('11', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('M', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_70(self):
        txn = {
            'authorization': {
                'orderId': '70',
                'amount': 0,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '5112000100000003',
                    'cardValidationNum': '123',
                    # 'pin': '3230',
                    'expDate': '1220',
                    'type': 'MC'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('12', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('M', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_71(self):
        txn = {
            'authorization': {
                'orderId': '71',
                'amount': 0,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '5112002100000009',
                    'cardValidationNum': '123',
                    # 'pin': '3230',
                    'expDate': '1220',
                    'type': 'MC'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('13', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('M', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_72(self):
        txn = {
            'authorization': {
                'orderId': '72',
                'amount': 0,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '5112002200000008',
                    'cardValidationNum': '123',
                    # 'pin': '3230',
                    'expDate': '1220',
                    'type': 'MC'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('14', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('N', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_73(self):
        txn = {
            'authorization': {
                'orderId': '73',
                'amount': 0,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '5112000200000002',
                    'cardValidationNum': '123',
                    # 'pin': '3230',
                    'expDate': '1220',
                    'type': 'MC'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('20', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('N', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_74(self):
        txn = {
            'authorization': {
                'orderId': '74',
                'amount': 0,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '5112000300000001',
                    'cardValidationNum': '123',
                    # 'pin': '3230',
                    'expDate': '1220',
                    'type': 'MC'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('30', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('P', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_75(self):
        txn = {
            'authorization': {
                'orderId': '75',
                'amount': 0,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '5112000400000000',
                    'cardValidationNum': '123',
                    # 'pin': '3230',
                    'expDate': '1220',
                    'type': 'MC'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('31', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('U', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_76(self):
        txn = {
            'authorization': {
                'orderId': '76',
                'amount': 0,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '5112010400000009',
                    'cardValidationNum': '123',
                    # 'pin': '3230',
                    'expDate': '1220',
                    'type': 'MC'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('32', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('S', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_78(self):
        txn = {
            'authorization': {
                'orderId': '78',
                'amount': 0,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '5112000600000008',
                    'cardValidationNum': '123',
                    # 'pin': '3230',
                    'expDate': '1220',
                    'type': 'MC'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('34', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('P', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_80(self):
        txn = {
            'authorization': {
                'orderId': '80',
                'amount': 0,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'ecommerce',
                'card': {
                    'number': '374313304211118',
                    'cardValidationNum': '123',
                    # 'pin': '3230',
                    'expDate': '1220',
                    'type': 'AX'
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('352', response['authorizationResponse']['response'])
        self.assertEquals('Decline CVV2/CID Fail', response['authorizationResponse']['message'])
        self.assertEquals('N', response['authorizationResponse']['fraudResult']['cardValidationResult'])


if __name__ == '__main__':
    unittest.main()
