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
from __future__ import print_function, absolute_import

import os
import sys
import unittest

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

package_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, package_root)

import certification_test_conf

conf = certification_test_conf.conf

from vantivsdk import *


class TestCertAuthsDict(unittest.TestCase):
    def test_table_2_1_1_auth(self):
        txn_dict = {
            'authorization' : {
                'orderId' : '1',
                'amount' : 10010,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'John & Mary Smith',
                    'addressLine1': '1 Main St.',
                    'city': 'Burlington',
                    'state': 'MA',
                    'zip': '01803-3747',
                    'country': 'USA',
                },
                'card': {
                    'number':'4457010000000009',
                    'expDate': '0121',
                    'cardValidationNum': '349',
                    'type': 'VI',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        # TODO response['authorizationResponse']['authCode'] include extra space
        self.assertEquals('11111', response['authorizationResponse']['authCode'])
        self.assertEquals('01', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('M', response['authorizationResponse']['fraudResult']['cardValidationResult'])

        # orderId *A
        txn_dict = {
            'capture' : {
                'litleTxnId': response['authorizationResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        captureresponse = online.request(txn_dict, conf)
        self.assertEquals('000', captureresponse['captureResponse']['response'])
        self.assertEquals('Approved', captureresponse['captureResponse']['message'])

        # orderId *B
        txn_dict = {
            'credit' : {
                'litleTxnId': captureresponse['captureResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        creditresponse = online.request(txn_dict, conf)
        self.assertEquals('000', creditresponse['creditResponse']['response'])
        self.assertEquals('Approved', creditresponse['creditResponse']['message'])

        # orderId *C
        txn_dict = {
            'void' : {
                'litleTxnId': creditresponse['creditResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        voidresponse = online.request(txn_dict, conf)
        self.assertEquals('000', voidresponse['voidResponse']['response'])
        self.assertEquals('Approved', voidresponse['voidResponse']['message'])

    def test_table_2_1_1_avs(self):

        txn_dict = {
            'authorization' : {
                'orderId' : '1',
                'amount' : '000',
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'John & Mary Smith',
                    'addressLine1': '1 Main St.',
                    'city': 'Burlington',
                    'state': 'MA',
                    'zip': '01803-3747',
                    'country': 'USA',
                },
                'card': {
                    'number':'4457010000000009',
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

    def test_table_2_1_1_sale(self):
        txn_dict = {
            'sale' : {
                'orderId' : '1',
                'amount' : 10010,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'John & Mary Smith',
                    'addressLine1': '1 Main St.',
                    'city': 'Burlington',
                    'state': 'MA',
                    'zip': '01803-3747',
                    'country': 'USA',
                },
                'card': {
                    'number':'4457010000000009',
                    'expDate': '0121',
                    'cardValidationNum': '349',
                    'type': 'VI',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('Approved', response['saleResponse']['message'])
        self.assertEquals('11111', response['saleResponse']['authCode'])
        self.assertEquals('01', response['saleResponse']['fraudResult']['avsResult'])
        self.assertEquals('M', response['saleResponse']['fraudResult']['cardValidationResult'])

        # orderId *B
        txn_dict = {
            'credit' : {
                'litleTxnId': response['saleResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        creditresponse = online.request(txn_dict, conf)
        self.assertEquals('000', creditresponse['creditResponse']['response'])
        self.assertEquals('Approved', creditresponse['creditResponse']['message'])

        # orderId *C
        txn_dict = {
            'void' : {
                'litleTxnId': creditresponse['creditResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        voidresponse = online.request(txn_dict, conf)
        self.assertEquals('000', voidresponse['voidResponse']['response'])
        self.assertEquals('Approved', voidresponse['voidResponse']['message'])

    def test_table_2_1_2_auth(self):
        # orderId 2
        txn_dict = {
            'authorization' : {
                'orderId' : '2',
                'amount' : 10010,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'Mike J. Hammer',
                    'addressLine1': '2 Main St.',
                    'addressLine2': 'Apt. 222',
                    'city': 'Riverside',
                    'state': 'RI',
                    'zip': '02915',
                    'country': 'USA',
                },
                'card': {
                    'number':'5112010000000003',
                    'expDate': '0221',
                    'cardValidationNum': '261',
                    'type': 'MC',
                },
                # 'cardholderAuthentication':{
                #     'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                # }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('22222', response['authorizationResponse']['authCode'])
        self.assertEquals('10', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('M', response['authorizationResponse']['fraudResult']['cardValidationResult'])
        # self.assertRaises(response['authorizationResponse']['fraudResult']['authenticationResult'])

        # orderId *A
        txn_dict = {
            'capture' : {
                'litleTxnId': response['authorizationResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        captureresponse = online.request(txn_dict, conf)
        self.assertEquals('000', captureresponse['captureResponse']['response'])
        self.assertEquals('Approved', captureresponse['captureResponse']['message'])

        # orderId *B
        txn_dict = {
            'credit' : {
                'litleTxnId': captureresponse['captureResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        creditresponse = online.request(txn_dict, conf)
        self.assertEquals('000', creditresponse['creditResponse']['response'])
        self.assertEquals('Approved', creditresponse['creditResponse']['message'])

        # orderId *C
        txn_dict = {
            'void' : {
                'litleTxnId': creditresponse['creditResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        voidresponse = online.request(txn_dict, conf)
        self.assertEquals('000', voidresponse['voidResponse']['response'])
        self.assertEquals('Approved', voidresponse['voidResponse']['message'])

    def test_table_2_1_2_avs(self):
        # orderId 2
        txn_dict = {
            'authorization' : {
                'orderId' : '2',
                'amount' : '000',
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'Mike J. Hammer',
                    'addressLine1': '2 Main St.',
                    'addressLine2': 'Apt. 222',
                    'city': 'Riverside',
                    'state': 'RI',
                    'zip': '02915',
                    'country': 'USA',
                },
                'card': {
                    'number':'5112010000000003',
                    'expDate': '0221',
                    'cardValidationNum': '261',
                    'type': 'MC',
                },
                # 'cardholderAuthentication':{
                #     'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                # }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('22222', response['authorizationResponse']['authCode'])
        self.assertEquals('10', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('M', response['authorizationResponse']['fraudResult']['cardValidationResult'])
        # self.assertRaises(response.transactionResponse.fraudResult.authenticationResult)

    def test_table_2_1_2_sale(self):
        txn_dict = {
            'sale' : {
                'orderId' : '2',
                'amount' : '000',
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'Mike J. Hammer',
                    'addressLine1': '2 Main St.',
                    'addressLine2': 'Apt. 222',
                    'city': 'Riverside',
                    'state': 'RI',
                    'zip': '02915',
                    'country': 'USA',
                },
                'card': {
                    'number':'5112010000000003',
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
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('Approved', response['saleResponse']['message'])
        self.assertEquals('22222', response['saleResponse']['authCode'])
        self.assertEquals('10', response['saleResponse']['fraudResult']['avsResult'])
        self.assertEquals('M', response['saleResponse']['fraudResult']['cardValidationResult'])
        # self.assertRaises(response.transactionResponse.fraudResult.authenticationResult)

        # orderId *A
        # capture = fields.capture()
        # capture.litleTxnId = response['authorizationResponse']['litleTxnId']
        # captureresponse = online.request(capture, conf)
        # self.assertEquals('000', captureresponse['authorizationResponse']['response'])
        # self.assertEquals('Approved', captureresponse['authorizationResponse']['message'])

        # orderId *B
        txn_dict = {
            'credit' : {
                'litleTxnId': response['saleResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        creditresponse = online.request(txn_dict, conf)
        self.assertEquals('000', creditresponse['creditResponse']['response'])
        self.assertEquals('Approved', creditresponse['creditResponse']['message'])

        # orderId *C
        txn_dict = {
            'void' : {
                'litleTxnId': creditresponse['creditResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        voidresponse = online.request(txn_dict, conf)
        self.assertEquals('000', voidresponse['voidResponse']['response'])
        self.assertEquals('Approved', voidresponse['voidResponse']['message'])

    def test_table_2_1_3_auth(self):
        txn_dict = {
            'authorization' : {
                'orderId' : '3',
                'amount' : 10010,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'Eileen Jones',
                    'addressLine1': '3 Main St.',
                    'city': 'Bloomfield',
                    'state': 'CT',
                    'zip': '06002',
                    'country': 'USA',
                },
                'card': {
                    'number':'6011010000000003',
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
            'capture' : {
                'litleTxnId': response['authorizationResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        captureresponse = online.request(txn_dict, conf)
        self.assertEquals('000', captureresponse['captureResponse']['response'])
        self.assertEquals('Approved', captureresponse['captureResponse']['message'])

        # orderId *B
        txn_dict = {
            'credit' : {
                'litleTxnId': captureresponse['captureResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        creditresponse = online.request(txn_dict, conf)
        self.assertEquals('000', creditresponse['creditResponse']['response'])
        self.assertEquals('Approved', creditresponse['creditResponse']['message'])

        # orderId *C
        txn_dict = {
            'void' : {
                'litleTxnId': creditresponse['creditResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        voidresponse = online.request(txn_dict, conf)
        self.assertEquals('000', voidresponse['voidResponse']['response'])
        self.assertEquals('Approved', voidresponse['voidResponse']['message'])

    def test_table_2_1_3_avs(self):
        txn_dict = {
            'authorization' : {
                'orderId' : '3',
                'amount' : 10010,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'Eileen Jones',
                    'addressLine1': '3 Main St.',
                    'city': 'Bloomfield',
                    'state': 'CT',
                    'zip': '06002',
                    'country': 'USA',
                },
                'card': {
                    'number':'6011010000000003',
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

    def test_table_2_1_3_sale(self):
        txn_dict = {
            'sale' : {
                'orderId' : '3',
                'amount' : 10010,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'Eileen Jones',
                    'addressLine1': '3 Main St.',
                    'city': 'Bloomfield',
                    'state': 'CT',
                    'zip': '06002',
                    'country': 'USA',
                },
                'card': {
                    'number':'6011010000000003',
                    'expDate': '0321',
                    'cardValidationNum': '758',
                    'type': 'DI',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('Approved', response['saleResponse']['message'])
        self.assertEquals('33333', response['saleResponse']['authCode'])
        self.assertEquals('10', response['saleResponse']['fraudResult']['avsResult'])
        self.assertEquals('M', response['saleResponse']['fraudResult']['cardValidationResult'])

        # orderId *A
        txn_dict = {
            'capture' : {
                'litleTxnId': response['saleResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        captureresponse = online.request(txn_dict, conf)
        self.assertEquals('000', captureresponse['captureResponse']['response'])
        self.assertEquals('Approved', captureresponse['captureResponse']['message'])

        # orderId *B
        txn_dict = {
            'credit' : {
                'litleTxnId': captureresponse['captureResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        creditresponse = online.request(txn_dict, conf)
        self.assertEquals('000', creditresponse['creditResponse']['response'])
        self.assertEquals('Approved', creditresponse['creditResponse']['message'])

        # orderId *C
        txn_dict = {
            'void' : {
                'litleTxnId': creditresponse['creditResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        voidresponse = online.request(txn_dict, conf)
        self.assertEquals('000', voidresponse['voidResponse']['response'])
        self.assertEquals('Approved', voidresponse['voidResponse']['message'])

    def test_table_2_1_4_auth(self):
        txn_dict = {
            'authorization' : {
                'orderId' : '4',
                'amount' : 10010,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'Bob Black',
                    'addressLine1': '4 Main St.',
                    'city': 'Laurel',
                    'state': 'MD',
                    'zip': '20708',
                    'country': 'USA',
                },
                'card': {
                    'number':'375001000000005',
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
            'capture' : {
                'litleTxnId': response['authorizationResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        captureresponse = online.request(txn_dict, conf)
        self.assertEquals('000', captureresponse['captureResponse']['response'])
        self.assertEquals('Approved', captureresponse['captureResponse']['message'])

        # orderId *B
        txn_dict = {
            'credit' : {
                'litleTxnId': captureresponse['captureResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        creditresponse = online.request(txn_dict, conf)
        self.assertEquals('000', creditresponse['creditResponse']['response'])
        self.assertEquals('Approved', creditresponse['creditResponse']['message'])

        # orderId *C
        txn_dict = {
            'void' : {
                'litleTxnId': creditresponse['creditResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        voidresponse = online.request(txn_dict, conf)
        self.assertEquals('000', voidresponse['voidResponse']['response'])
        self.assertEquals('Approved', voidresponse['voidResponse']['message'])

    def test_table_2_1_4_avs(self):
        # orderId *
        txn_dict = {
            'authorization' : {
                'orderId' : '4',
                'amount' : '000',
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'Bob Black',
                    'addressLine1': '4 Main St.',
                    'city': 'Laurel',
                    'state': 'MD',
                    'zip': '20708',
                    'country': 'USA',
                },
                'card': {
                    'number':'375001000000005',
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

    def test_table_2_1_4_sale(self):
        # orderId *
        txn_dict = {
            'sale' : {
                'orderId' : '4',
                'amount' : 10010,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'Bob Black',
                    'addressLine1': '4 Main St.',
                    'city': 'Laurel',
                    'state': 'MD',
                    'zip': '20708',
                    'country': 'USA',
                },
                'card': {
                    'number':'375001000000005',
                    'expDate': '0421',
                    'type': 'AX',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('Approved', response['saleResponse']['message'])
        self.assertEquals('44444', response['saleResponse']['authCode'])
        self.assertEquals('13', response['saleResponse']['fraudResult']['avsResult'])

        # orderId *A
        txn_dict = {
            'capture' : {
                'litleTxnId': response['saleResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        captureresponse = online.request(txn_dict, conf)
        self.assertEquals('000', captureresponse['captureResponse']['response'])
        self.assertEquals('Approved', captureresponse['captureResponse']['message'])

        # orderId *B
        txn_dict = {
            'credit' : {
                'litleTxnId': captureresponse['captureResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        creditresponse = online.request(txn_dict, conf)
        self.assertEquals('000', creditresponse['creditResponse']['response'])
        self.assertEquals('Approved', creditresponse['creditResponse']['message'])

    def test_table_2_1_5_auth(self):
        txn_dict = {
            'authorization' : {
                'orderId' : '5',
                'amount' : 10010,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                # 'cardholderAuthentication': {
                #     'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                # },
                'card': {
                    'number':'4100200300011001',
                    'expDate': '0521',
                    'cardValidationNum': '463',
                    'type': 'VI',
                },

            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('55555', response['authorizationResponse']['authCode'])
        self.assertEquals('32', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('M', response['authorizationResponse']['fraudResult']['cardValidationResult'])

        # orderId *A
        txn_dict = {
            'capture' : {
                'litleTxnId': response['authorizationResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        captureresponse = online.request(txn_dict, conf)
        self.assertEquals('000', captureresponse['captureResponse']['response'])
        self.assertEquals('Approved', captureresponse['captureResponse']['message'])

        # orderId *B
        txn_dict = {
            'credit' : {
                'litleTxnId': captureresponse['captureResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        creditresponse = online.request(txn_dict, conf)
        self.assertEquals('000', creditresponse['creditResponse']['response'])
        self.assertEquals('Approved', creditresponse['creditResponse']['message'])

        # orderId *C
        txn_dict = {
            'void' : {
                'litleTxnId': creditresponse['creditResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        voidresponse = online.request(txn_dict, conf)
        self.assertEquals('000', voidresponse['voidResponse']['response'])
        self.assertEquals('Approved', voidresponse['voidResponse']['message'])

    def test_table_2_1_5_avs(self):
        txn_dict = {
            'authorization' : {
                'orderId' : '5',
                'amount' : '000',
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                # 'cardholderAuthentication': {
                #     'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                # },
                'card': {
                    'number':'4100200300011001',
                    'expDate': '0521',
                    'cardValidationNum': '463',
                    'type': 'VI',
                },

            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('55555', response['authorizationResponse']['authCode'])
        self.assertEquals('32', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('M', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_table_2_1_5_sale(self):
        txn_dict = {
            'sale' : {
                'orderId' : '5',
                'amount' : 10010,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                # 'cardholderAuthentication': {
                #     'authenticationValue': 'BwABBJQ1AgAAAAAgJDUCAAAAAAA=',
                # },
                'card': {
                    'number':'4100200300011001',
                    'expDate': '0521',
                    'cardValidationNum': '463',
                    'type': 'VI',
                },

            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['saleResponse']['response'])
        self.assertEquals('Approved', response['saleResponse']['message'])
        self.assertEquals('55555', response['saleResponse']['authCode'])
        self.assertEquals('32', response['saleResponse']['fraudResult']['avsResult'])
        self.assertEquals('M', response['saleResponse']['fraudResult']['cardValidationResult'])

        # orderId *B
        txn_dict = {
            'credit': {
                'litleTxnId': response['saleResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        creditresponse = online.request(txn_dict, conf)
        self.assertEquals('000', creditresponse['creditResponse']['response'])
        self.assertEquals('Approved', creditresponse['creditResponse']['message'])

        # orderId *C
        txn_dict = {
            'void': {
                'litleTxnId': creditresponse['creditResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        voidresponse = online.request(txn_dict, conf)
        self.assertEquals('000', voidresponse['voidResponse']['response'])
        self.assertEquals('Approved', voidresponse['voidResponse']['message'])

    def test_table_2_1_6_auth(self):
        txn_dict = {
            'authorization' : {
                'orderId' : '6',
                'amount' : 10010,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'Joe Green',
                    'addressLine1': '6 Main St.',
                    'city': 'Derry',
                    'state': 'NH',
                    'zip': '03038',
                    'country': 'USA',
                },
                'card': {
                    'number':'4457010100000008',
                    'expDate': '0621',
                    'cardValidationNum': '992',
                    'type': 'VI',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('110', response['authorizationResponse']['response'])
        self.assertEquals('Insufficient Funds', response['authorizationResponse']['message'])
        self.assertEquals('34', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('P', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_table_2_1_6_sale(self):
        txn_dict = {
            'sale' : {
                'orderId' : '6',
                'amount' : 10010,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'Joe Green',
                    'addressLine1': '6 Main St.',
                    'city': 'Derry',
                    'state': 'NH',
                    'zip': '03038',
                    'country': 'USA',
                },
                'card': {
                    'number':'4457010100000008',
                    'expDate': '0621',
                    'cardValidationNum': '992',
                    'type': 'VI',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('110', response['saleResponse']['response'])
        self.assertEquals('Insufficient Funds', response['saleResponse']['message'])
        self.assertEquals('34', response['saleResponse']['fraudResult']['avsResult'])
        self.assertEquals('P', response['saleResponse']['fraudResult']['cardValidationResult'])

        # orderId *C
        txn_dict = {
            'void' : {
                'litleTxnId': response['saleResponse']['litleTxnId'],
                'id': 'ThisIsID'
            }
        }
        voidresponse = online.request(txn_dict, conf)
        self.assertEquals('360', voidresponse['voidResponse']['response'])
        self.assertEquals('No transaction found with specified litleTxnId', voidresponse['voidResponse']['message'])

    def test_table_2_1_7_auth(self):
        txn_dict = {
            'authorization' : {
                'orderId' : '7',
                'amount' : 10010,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'Jane Murray',
                    'addressLine1': '7 Main St.',
                    'city': 'Amesbury',
                    'state': 'MA',
                    'zip': '01913',
                    'country': 'USA',
                },
                'card': {
                    'number':'5112010100000002',
                    'expDate': '0721',
                    'cardValidationNum': '251',
                    'type': 'MC',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('301', response['authorizationResponse']['response'])
        self.assertEquals('Invalid Account Number', response['authorizationResponse']['message'])
        self.assertEquals('34', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('N', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_table_2_1_7_avs(self):
        txn_dict = {
            'authorization' : {
                'orderId' : '7',
                'amount' : '000',
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'Jane Murray',
                    'addressLine1': '7 Main St.',
                    'city': 'Amesbury',
                    'state': 'MA',
                    'zip': '01913',
                    'country': 'USA',
                },
                'card': {
                    'number':'5112010100000002',
                    'expDate': '0721',
                    'cardValidationNum': '251',
                    'type': 'MC',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('301', response['authorizationResponse']['response'])
        self.assertEquals('Invalid Account Number', response['authorizationResponse']['message'])
        self.assertEquals('34', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('N', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_table_2_1_7_sale(self):
        txn_dict = {
            'sale' : {
                'orderId' : '7',
                'amount' : 10010,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'Jane Murray',
                    'addressLine1': '7 Main St.',
                    'city': 'Amesbury',
                    'state': 'MA',
                    'zip': '01913',
                    'country': 'USA',
                },
                'card': {
                    'number':'5112010100000002',
                    'expDate': '0721',
                    'cardValidationNum': '251',
                    'type': 'MC',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('301', response['saleResponse']['response'])
        self.assertEquals('Invalid Account Number', response['saleResponse']['message'])
        self.assertEquals('34', response['saleResponse']['fraudResult']['avsResult'])
        self.assertEquals('N', response['saleResponse']['fraudResult']['cardValidationResult'])

    def test_table_2_1_8_auth(self):
        txn_dict = {
            'authorization' : {
                'orderId' : '8',
                'amount' : 10010,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'Mark Johnson',
                    'addressLine1': '8 Main St.',
                    'city': 'Manchester',
                    'state': 'NH',
                    'zip': '03101',
                    'country': 'USA',
                },
                'card': {
                    'number':'6011010100000002',
                    'expDate': '0821',
                    'cardValidationNum': '184',
                    'type': 'DI',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('123', response['authorizationResponse']['response'])
        self.assertEquals('Call Discover', response['authorizationResponse']['message'])
        self.assertEquals('34', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('P', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_table_2_1_8_avs(self):
        txn_dict = {
            'authorization' : {
                'orderId' : '8',
                'amount' : '000',
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'Mark Johnson',
                    'addressLine1': '8 Main St.',
                    'city': 'Manchester',
                    'state': 'NH',
                    'zip': '03101',
                    'country': 'USA',
                },
                'card': {
                    'number':'6011010100000002',
                    'expDate': '0821',
                    'cardValidationNum': '184',
                    'type': 'DI',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('123', response['authorizationResponse']['response'])
        self.assertEquals('Call Discover', response['authorizationResponse']['message'])
        self.assertEquals('34', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('P', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_table_2_1_8_sale(self):
        txn_dict = {
            'sale' : {
                'orderId' : '8',
                'amount' : 10010,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'Mark Johnson',
                    'addressLine1': '8 Main St.',
                    'city': 'Manchester',
                    'state': 'NH',
                    'zip': '03101',
                    'country': 'USA',
                },
                'card': {
                    'number':'6011010100000002',
                    'expDate': '0821',
                    'cardValidationNum': '184',
                    'type': 'DI',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('123', response['saleResponse']['response'])
        self.assertEquals('Call Discover', response['saleResponse']['message'])
        self.assertEquals('34', response['saleResponse']['fraudResult']['avsResult'])
        self.assertEquals('P', response['saleResponse']['fraudResult']['cardValidationResult'])

    def test_table_2_1_9_auth(self):
        txn_dict = {
            'authorization' : {
                'orderId' : '9',
                'amount' : 10010,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'James Miller',
                    'addressLine1': '9 Main St.',
                    'city': 'Boston',
                    'state': 'MA',
                    'zip': '02134',
                    'country': 'USA',
                },
                'card': {
                    'number':'375001010000003',
                    'expDate': '0921',
                    'cardValidationNum': '0421',
                    'type': 'AX',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('303', response['authorizationResponse']['response'])
        self.assertEquals('Pick Up Card', response['authorizationResponse']['message'])
        self.assertEquals('34', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('P', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_table_2_1_9_avs(self):
        txn_dict = {
            'authorization' : {
                'orderId' : '9',
                'amount' : '000',
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'James Miller',
                    'addressLine1': '9 Main St.',
                    'city': 'Boston',
                    'state': 'MA',
                    'zip': '02134',
                    'country': 'USA',
                },
                'card': {
                    'number':'375001010000003',
                    'expDate': '0921',
                    'cardValidationNum': '0421',
                    'type': 'AX',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('303', response['authorizationResponse']['response'])
        self.assertEquals('Pick Up Card', response['authorizationResponse']['message'])
        self.assertEquals('34', response['authorizationResponse']['fraudResult']['avsResult'])
        self.assertEquals('P', response['authorizationResponse']['fraudResult']['cardValidationResult'])

    def test_table_2_1_9_sale(self):
        txn_dict = {
            'sale' : {
                'orderId' : '9',
                'amount' : 10010,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'name': 'James Miller',
                    'addressLine1': '9 Main St.',
                    'city': 'Boston',
                    'state': 'MA',
                    'zip': '02134',
                    'country': 'USA',
                },
                'card': {
                    'number':'375001010000003',
                    'expDate': '0921',
                    'cardValidationNum': '0421',
                    'type': 'AX',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('303', response['saleResponse']['response'])
        self.assertEquals('Pick Up Card', response['saleResponse']['message'])
        self.assertEquals('34', response['saleResponse']['fraudResult']['avsResult'])
        self.assertEquals('P', response['saleResponse']['fraudResult']['cardValidationResult'])

    def test_table_2_1_10_auth(self):
        txn_dict = {
            'authorization' : {
                'orderId' : '10',
                'amount' : 40000,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'card': {
                    'number':'4457010140000141',
                    'expDate': '0921',
                    'type': 'VI',
                },
                'allowPartialAuth' : True,
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('010', response['authorizationResponse']['response'])
        self.assertEquals('Partially Approved', response['authorizationResponse']['message'])
        self.assertEquals('32000', response['authorizationResponse']['approvedAmount'])

    def test_table_2_1_11_auth(self):
        txn_dict = {
            'authorization' : {
                'orderId' : '11',
                'amount' : 60000,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'card': {
                    'number':'5112010140000004',
                    'expDate': '1121',
                    'type': 'MC',
                },
                'allowPartialAuth' : True,
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('010', response['authorizationResponse']['response'])
        self.assertEquals('Partially Approved', response['authorizationResponse']['message'])
        self.assertEquals('48000', response['authorizationResponse']['approvedAmount'])

    def test_table_2_1_12_auth(self):
        txn_dict = {
            'authorization' : {
                'orderId' : '12',
                'amount' : 50000,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'card': {
                    'number':'375001014000009',
                    'expDate': '0421',
                    'type': 'AX',
                },
                'allowPartialAuth' : True,
            }
        }
        response = online.request(txn_dict, conf)
        # self.assertEquals('010', response['authorizationResponse']['response'])
        self.assertEquals('Partially Approved', response['authorizationResponse']['message'])
        self.assertEquals('40000', response['authorizationResponse']['approvedAmount'])

    def test_table_2_1_13_auth(self):
        txn_dict = {
            'authorization' : {
                'orderId' : '13',
                'amount' : 15000,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'card': {
                    'number':'6011010140000004',
                    'expDate': '0821',
                    'type': 'DI',
                },
                'allowPartialAuth' : True,
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('010', response['authorizationResponse']['response'])
        self.assertEquals('Partially Approved', response['authorizationResponse']['message'])
        self.assertEquals('12000', response['authorizationResponse']['approvedAmount'])


if __name__ == '__main__':
    unittest.main()
