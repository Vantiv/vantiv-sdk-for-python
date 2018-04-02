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
import xmltodict

package_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
sys.path.insert(0, package_root)

from vantivsdk import *

package_root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, package_root)

import certification_test_conf

conf = certification_test_conf.conf


class TestCertTokenDict(unittest.TestCase):
    
    def test_table_2_7_50(self):

        txn_dict = {
            'registerTokenRequest' : {
                'orderId' : '50',
                'accountNumber' : '4457119922390123',
                'id' : 'thisisid',
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('0123', response['registerTokenResponse']['cnpToken'][-4:])
        self.assertEquals('445711', response['registerTokenResponse']['bin'])
        self.assertEquals('VI', response['registerTokenResponse']['type'])
        # TODO run twice get 802
        # self.assertEquals('801', response['registerTokenResponse']['response'])
        # self.assertEquals('Account number was successfully registered', response['registerTokenResponse']['message'])
    
    def test_table_2_7_51(self):        

        txn_dict = {
            'registerTokenRequest' : {
                'orderId' : '51',
                'accountNumber' : '4457119999999999',
                'id' : 'thisisid',
            }
        }
        response = online.request(txn_dict, conf)
        self.assertNotIn('cnpToken', response['registerTokenResponse'])
        self.assertEquals('820', response['registerTokenResponse']['response'])
        self.assertEquals('Credit card number was invalid', response['registerTokenResponse']['message'])
        

    def test_table_2_7_52(self):


        txn_dict = {
            'registerTokenRequest' : {
                'orderId' : '52',
                'accountNumber' : '4457119922390123',
                'id' : 'thisisid',
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('0123', response['registerTokenResponse']['cnpToken'][-4:])
        self.assertEquals('445711', response['registerTokenResponse']['bin'])
        self.assertEquals('VI', response['registerTokenResponse']['type'])
        self.assertEquals('802', response['registerTokenResponse']['response'])
        self.assertEquals('Account number was previously registered', response['registerTokenResponse']['message'])

    def test_table_2_7_53(self):
        # This test only works for regular test credentials, not pgp test credentials.

        txn_dict = {
            'registerTokenRequest' : {
                'orderId' : '53',
                'echeckForToken' : {
                    'accNum' : '1099999998',
                    'routingNum': '011100012'
                },
                'id' : 'thisisid',
            }
        }
        response = online.request(txn_dict, conf)
        self.assertIsNotNone(response['registerTokenResponse']['cnpToken'])
        self.assertEquals('EC', response['registerTokenResponse']['type'])
        self.assertEquals('998', response['registerTokenResponse']['eCheckAccountSuffix'])
        # TODO run twice get 802
        # self.assertEquals('801', response['registerTokenResponse']['response'])
        # self.assertEquals('Account number was successfully registered', response['registerTokenResponse']['message'])

    def test_table_2_7_54(self):
        txn_dict = {
            'registerTokenRequest': {
                'orderId': '54',
                'echeckForToken': {
                    'accNum': '1022222102',
                    'routingNum': '1145_7895'
                },
                'id': 'thisisid',
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('900', response['registerTokenResponse']['response'])
        self.assertEquals('Invalid Bank Routing Number', response['registerTokenResponse']['message'])

    def test_table_2_8_55(self):
        # This test only works for regular test credentials, not pgp test credentials.
        txn_dict = {
            'authorization' : {
                'orderId' : '55',
                'amount' : 15000,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'card': {
                    'number':'5435101234510196',
                    'expDate': '1121',
                    'cardValidationNum': '987',
                    'type': 'MC',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('0196', response['authorizationResponse']['tokenResponse']['cnpToken'][-4:])
        # TODO run twice get 802
        # self.assertEquals('801', response['authorizationResponse']['tokenResponse']['tokenResponseCode'])
        # self.assertEquals('Account number was successfully registered',
        #                   response['authorizationResponse']['tokenResponse']['tokenMessage'])
        self.assertEquals('MC', response['authorizationResponse']['tokenResponse']['type'])
        self.assertEquals('543510', response['authorizationResponse']['tokenResponse']['bin'])

    def test_table_2_8_56(self):
        txn_dict = {
            'authorization': {
                'orderId': '56',
                'amount': 15000,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'number': '5435109999999999',
                    'expDate': '1121',
                    'cardValidationNum': '987',
                    'type': 'MC',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('301', response['authorizationResponse']['response'])
        self.assertEquals('Invalid account number'.lower(), response['authorizationResponse']['message'].lower())

    def test_table_2_8_57_58(self):
        # orderId 57
        txn_dict = {
            'authorization': {
                'orderId': '57',
                'amount': 15000,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'number': '5435101234510196',
                    'expDate': '1121',
                    'cardValidationNum': '987',
                    'type': 'MC',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('0196', response['authorizationResponse']['tokenResponse']['cnpToken'][-4:])
        self.assertEquals('802', response['authorizationResponse']['tokenResponse']['tokenResponseCode'])
        self.assertEquals('Account number was previously registered',
                          response['authorizationResponse']['tokenResponse']['tokenMessage'])
        self.assertEquals('MC', response['authorizationResponse']['tokenResponse']['type'])
        self.assertEquals('543510', response['authorizationResponse']['tokenResponse']['bin'])

        # orderId 58
        txn_dict = {
            'authorization': {
                'orderId': '58',
                'amount': 15000,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'token': {
                    'cnpToken': response['authorizationResponse']['tokenResponse']['cnpToken'],
                    'expDate': '1121',
                    'cardValidationNum': '987',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
    
    def test_table_2_8_59(self):

        txn_dict = {
            'authorization': {
                'orderId': '59',
                'amount': 15000,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'token': {
                    'cnpToken':'1111000100092332',
                    'expDate': '1121',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('822', response['authorizationResponse']['response'])
        self.assertEquals('Token was not found', response['authorizationResponse']['message'])

    
    def test_table_2_8_60(self):
        txn_dict = {
            'authorization': {
                'orderId': '60',
                'amount': 15000,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'token': {
                    'cnpToken':'1112000100000085',
                    'expDate': '1121',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('823', response['authorizationResponse']['response'])
        self.assertEquals('Token was invalid', response['authorizationResponse']['message'])
    
    def test_table_2_8_61(self):

        txn_dict = {
            'echeckSale' : {
                'orderId' : '61',
                'amount' : 15000,
                'orderSource' : 'ecommerce',
                'id' : 'thisisid',
                'billToAddress' : {
                    'firstName': 'Tom',
                    'lastName': 'Black',
                    'phone': '999-999-9999',
                },
                'echeck': {                    
                    'accType': 'Checking',
                    'accNum': '1099999003',
                    'routingNum': '011100012',
                }
            }
        }
        response = online.request(txn_dict, conf)
        # print('Sent to: ' + conf.url)
        # xmltodict.parse(response)['cnpOnlineResponse']
        # # TODO no tokenResponse
        # self.assertIsNotNone(response['echeckSalesResponse']['tokenResponse']['cnpToken'])
        # self.assertEquals('801', response['echeckSalesResponse']['tokenResponse']['tokenResponseCode'])
        # self.assertEquals('Account number was successfully registered',
        #                   response['echeckSalesResponse']['tokenResponse']['tokenMessage'])
        # self.assertEquals('EC', response['echeckSalesResponse']['tokenResponse']['type'])
        # self.assertEquals('003', response['echeckSalesResponse']['tokenResponse']['eCheckAccountSuffix'])
        
    
    def test_table_2_8_62(self):
        txn_dict = {
            'echeckSale': {
                'orderId': '62',
                'amount': 15000,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'billToAddress': {
                    'firstName': 'Tom',
                    'lastName': 'Black',
                    'phone': '999-999-9999',
                },
                'echeck': {
                    'accType': 'Checking',
                    'accNum': '1099999999',
                    'routingNum': '011100012',
                }
            }
        }
        response = online.request(txn_dict, conf)
        # TODO no tokenResponse
        # self.assertIsNotNone(response['echeckSalesResponse']['tokenResponse']['cnpToken'])
        # self.assertEquals('801', response['echeckSalesResponse']['tokenResponse']['tokenResponseCode'])
        # self.assertEquals('Account number was successfully registered',
        #                   response['echeckSalesResponse']['tokenResponse']['tokenMessage'])
        # self.assertEquals('EC', response['echeckSalesResponse']['tokenResponse']['type'])
        # self.assertEquals('999', response['echeckSalesResponse']['tokenResponse']['eCheckAccountSuffix'])

    def test_table_2_8_63(self):
        txn_dict = {
            'echeckCredit': {
                'orderId': '63',
                'amount': 15000,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'billToAddress': {
                    'firstName': 'Tom',
                    'lastName': 'Black',
                    'phone': '999-999-9999',
                },
                'echeck': {
                    'accType': 'Checking',
                    'accNum': '1099999999',
                    'routingNum': '011100012',
                }
            }
        }
        response = online.request(txn_dict, conf)
        # TODO no tokenResponse
        # self.assertIsNotNone(response['echeckCreditResponse']['tokenResponse']['cnpToken'])
        # self.assertEquals('801', response['echeckCreditResponse']['tokenResponse']['tokenResponseCode'])
        # self.assertEquals('Account number was successfully registered',
        #                   response['echeckCreditResponse']['tokenResponse']['tokenMessage'])
        # self.assertEquals('EC', response['echeckCreditResponse']['tokenResponse']['type'])
        # self.assertEquals('999', response['echeckCreditResponse']['tokenResponse']['eCheckAccountSuffix'])

    def test_table_2_8_64(self):
        txn_dict = {
            'echeckSale': {
                'orderId': '64',
                'amount': 15000,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'billToAddress': {
                    'firstName': 'Tom',
                    'lastName': 'Black',
                    'phone': '999-999-9999',
                },
                'echeck': {
                    'accType': 'Corporate',
                    'accNum': '6099999993',
                    'routingNum': '211370545',
                }
            }
        }
        response = online.request(txn_dict, conf)
        # TODO no accountUpdater in response
        # self.assertEquals('Checking',
        #                   response['echeckCreditResponse']['accountUpdater']['originalTokenInfo']['accType'])
        # self.assertEquals('11190000001003001',
        #                   response['echeckCreditResponse']['accountUpdater']['originalTokenInfo']['cnpToken'])
        # self.assertEquals('211370545',
        #                   response['echeckCreditResponse']['accountUpdater']['originalTokenInfo']['routingNum'])
        #
        # self.assertEquals('Checking', response['echeckCreditResponse']['accountUpdater']['newTokenInfo']['accType'])
        # self.assertEquals('11190000001003001',
        #                   response['echeckCreditResponse']['accountUpdater']['newTokenInfo']['cnpToken'])
        # self.assertEquals('211370545', response['echeckCreditResponse']['accountUpdater']['newTokenInfo']['routingNum'])
        #
        # self.assertIsNotNone(response['echeckCreditResponse']['accountUpdater']['newTokenInfo']['cnpToken'])
        # self.assertEquals('801',
        #                   response['echeckCreditResponse']['accountUpdater']['newTokenInfo']['tokenResponseCode'])
        # self.assertEquals('Account number was successfully registered',
        #                   response['echeckCreditResponse']['accountUpdater']['tokenMessage'])
        # self.assertEquals('EC', response['echeckCreditResponse']['accountUpdater']['type'])
        # self.assertEquals('999', response['echeckCreditResponse']['accountUpdater']['eCheckAccountSuffix'])
    

if __name__ == '__main__':
    unittest.main()
