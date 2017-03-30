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

package_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, package_root)

import certification_test_conf

conf = certification_test_conf.conf


class TestCertEnhancedAuthsDict(unittest.TestCase):
    # response sample for orderId 14 through 20
    #
    # <litleOnlineResponse version="9.10" xmlns="http://www.litle.com/fields.
    #     response="0" message="Valid Format">
    #     <authorizationResponse reportGroup="Default Report Group">
    #         <litleTxnId>82919994154434833</litleTxnId>
    #         <orderId>14</orderId>
    #         <response>000</response>
    #         <responseTime>2017-02-21T16:14:39</responseTime>
    #         <postDate>2017-02-21</postDate>
    #         <message>Approved</message>
    #         <authCode>VIPREP</authCode>
    #         <fraudResult>
    #             <avsResult>00</avsResult>
    #         </fraudResult>
    #         <tokenResponse>
    #             <litleToken>1111000274230247</litleToken>
    #             <tokenResponseCode>801</tokenResponseCode>
    #             <tokenMessage>Account number was successfully registered</tokenMessage>
    #             <type>VI</type>
    #             <bin>445701</bin>
    #         </tokenResponse>
    #         <enhancedAuthResponse/>
    #         <networkTransactionId>000000000000000</networkTransactionId>
    #     </authorizationResponse>
    # </litleOnlineResponse>
    #
    # enhancedAuthResponse is empty
    # Following assertions can't pass.
    # self.assertEquals('PREPAID', response.transactionResponse.type)
    # self.assertEquals(2000, response.transactionResponse.availableBalance)
    # self.assertEquals('NO', response.transactionResponse.reloadable)
    # self.assertEquals('GIFT', response.transactionResponse.prepaidCardType)

    def test_table_2_1_14_auth(self):
        txn_dict = {
            'authorization': {
                'orderId': '14',
                'amount': 10010,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'number': '4457010200000247',
                    'expDate': '0821',
                    'type': 'VI',
                }
            }
        }

        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        # TODO enhancedAuthResponse is empty
        # self.assertEquals('PREPAID',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['type'])
        # self.assertEquals(2000,
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['availableBalance'])
        # self.assertEquals('NO',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['reloadable'])
        # self.assertEquals('GIFT',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['prepaidCardType'])

    def test_table_2_1_15_auth(self):
        txn_dict = {
            'authorization': {
                'orderId': '15',
                'amount': 10010,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'number': '5500000254444445',
                    'expDate': '0321',
                    'type': 'MC',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        # TODO enhancedAuthResponse is empty
        # self.assertEquals('PREPAID',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['type'])
        # self.assertEquals(2000,
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['availableBalance'])
        # self.assertEquals('YES',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['reloadable'])
        # self.assertEquals('PAYROLL',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['prepaidCardType'])

    def test_table_2_1_16_auth(self):
        txn_dict = {
            'authorization': {
                'orderId': '16',
                'amount': 10010,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'number': '5592106621450897',
                    'expDate': '0321',
                    'type': 'MC',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        # TODO enhancedAuthResponse is empty
        # self.assertEquals('PREPAID',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['type'])
        # self.assertEquals(0,
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['availableBalance'])
        # self.assertEquals('YES',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['reloadable'])
        # self.assertEquals('PAYROLL',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['prepaidCardType'])

    def test_table_2_1_17_auth(self):
        txn_dict = {
            'authorization': {
                'orderId': '17',
                'amount': 10010,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'number': '5590409551104142',
                    'expDate': '0321',
                    'type': 'MC',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        # TODO enhancedAuthResponse is empty
        # self.assertEquals('PREPAID',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['type'])
        # self.assertEquals(6500,
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['availableBalance'])
        # self.assertEquals('YES',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['reloadable'])
        # self.assertEquals('PAYROLL',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['prepaidCardType'])

    def test_table_2_1_18_auth(self):
        txn_dict = {
            'authorization': {
                'orderId': '18',
                'amount': 10010,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'number': '5587755665222179',
                    'expDate': '0321',
                    'type': 'MC',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        # TODO enhancedAuthResponse is empty
        # self.assertEquals('PREPAID',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['type'])
        # self.assertEquals(12200,
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['availableBalance'])
        # self.assertEquals('YES',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['reloadable'])
        # self.assertEquals('PAYROLL',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['prepaidCardType'])

    def test_table_2_1_19_auth(self):
        txn_dict = {
            'authorization': {
                'orderId': '19',
                'amount': 10010,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'number': '5445840176552850',
                    'expDate': '0321',
                    'type': 'MC',
                }
            }
        }
        response = online.request(txn_dict, conf)

        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        # TODO enhancedAuthResponse is empty
        # self.assertEquals('PREPAID',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['type'])
        # self.assertEquals(20000,
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['availableBalance'])
        # self.assertEquals('YES',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['reloadable'])
        # self.assertEquals('PAYROLL',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['prepaidCardType'])

    def test_table_2_1_20_auth(self):
        txn_dict = {
            'authorization': {
                'orderId': '20',
                'amount': 10010,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'number': '5390016478904678',
                    'expDate': '0321',
                    'type': 'MC',
                }
            }
        }
        response = online.request(txn_dict, conf)

        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        # TODO enhancedAuthResponse is empty
        # self.assertEquals('PREPAID',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['type'])
        # self.assertEquals(10050,
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['availableBalance'])
        # self.assertEquals('YES',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['reloadable'])
        # self.assertEquals('PAYROLL',
        #                   response['authorizationResponse']['enhancedAuthResponse']['fundingSource']['prepaidCardType'])

    # response sample for orderId 21 through 24
    #  <litleOnlineResponse version="9.10" xmlns="http://www.litle.com/fields.
    #     response="0" message="Valid Format">
    #     <authorizationResponse reportGroup="Default Report Group">
    #         <litleTxnId>82919994227425701</litleTxnId>
    #         <orderId>21</orderId>
    #         <response>000</response>
    #         <responseTime>2017-02-21T16:29:10</responseTime>
    #         <postDate>2017-02-21</postDate>
    #         <message>Approved</message>
    #         <authCode>VIAFF1</authCode>
    #         <fraudResult>
    #             <avsResult>00</avsResult>
    #         </fraudResult>
    #         <tokenResponse>
    #             <litleToken>1111000273442009</litleToken>
    #             <tokenResponseCode>801</tokenResponseCode>
    #             <tokenMessage>Account number was successfully registered</tokenMessage>
    #             <type>VI</type>
    #             <bin>410020</bin>
    #         </tokenResponse>
    #         <enhancedAuthResponse/>
    #         <networkTransactionId>000000000000000</networkTransactionId>
    #     </authorizationResponse>
    # </litleOnlineResponse>
    #
    # enhancedAuthResponse is empty
    # Can't test affluence, add test for authCode
    def test_table_2_1_21_auth(self):
        txn_dict = {
            'authorization': {
                'orderId': '21',
                'amount': 10010,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'number': '4100200300012009',
                    'expDate': '0921',
                    'type': 'VI',
                }
            }
        }
        response = online.request(txn_dict, conf)

        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        # TODO enhancedAuthResponse is empty
        # self.assertEquals('AFFLUENT', response['authorizationResponse']['enhancedAuthResponse']['affluence'])

    def test_table_2_1_22_auth(self):
        txn_dict = {
            'authorization': {
                'orderId': '22',
                'amount': 10010,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'number': '4100200300013007',
                    'expDate': '1121',
                    'type': 'VI',
                }
            }
        }
        response = online.request(txn_dict, conf)

        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        # TODO enhancedAuthResponse is empty
        # self.assertEquals('MASS AFFLUENT', response['authorizationResponse']['enhancedAuthResponse']['affluence'])

    def test_table_2_1_23_auth(self):
        txn_dict = {
            'authorization': {
                'orderId': '23',
                'amount': 10010,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'number': '5112010201000109',
                    'expDate': '0421',
                    'type': 'MC',
                }
            }
        }
        response = online.request(txn_dict, conf)

        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        # TODO enhancedAuthResponse is empty
        # self.assertEquals('AFFLUENT', response['authorizationResponse']['enhancedAuthResponse']['affluence'])

    def test_table_2_1_24_auth(self):
        txn_dict = {
            'authorization': {
                'orderId': '24',
                'amount': 10010,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'number': '5112010202000108',
                    'expDate': '0821',
                    'type': 'MC',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        # TODO enhancedAuthResponse is empty
        # self.assertEquals('MASS AFFLUENT', response['authorizationResponse']['enhancedAuthResponse']['affluence'])

    def test_table_2_1_25_auth(self):
        txn_dict = {
            'authorization': {
                'orderId': '25',
                'amount': 10010,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'number': '4100200310000002',
                    'expDate': '1121',
                    'type': 'VI',
                }
            }
        }
        response = online.request(txn_dict, conf)

        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        # TODO enhancedAuthResponse is empty
        # self.assertEquals('BRA', response['authorizationResponse']['enhancedAuthResponse']['issuerCountry'])


if __name__ == '__main__':
    unittest.main()
