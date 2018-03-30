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

print('Testing agaisnt: ' + conf.url)
class TestCertEcheckDict(unittest.TestCase):
    def test_table_2_3_37(self):
        txn_dict = {
            'echeckVerification': {
                'orderId': '37',
                'amount': 3001,
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'billToAddress': {
                    'firstName': 'Tom',
                    'lastName': 'Black',
                    'phone': '999-999-9999',
                },
                'echeck': {
                    'accNum': '10@BC99999',
                    'accType': 'Checking',
                    'routingNum': '053100300',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('301', response['echeckVerificationResponse']['response'])
        self.assertEquals('Invalid Account Number', response['echeckVerificationResponse']['message'])


    def test_table_2_3_38(self):
        txn_dict = {
            'echeckVerification': {
                'orderId': '38',
                'amount': 3002,
                'orderSource': 'telephone',
                'id': 'thisisid',
                'billToAddress': {
                    'firstName': 'John',
                    'lastName': 'Smith',
                    'phone': '999-999-9999',
                },
                'echeck': {
                    'accNum': '1099999999',
                    'accType': 'Checking',
                    'routingNum': '011075150',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['echeckVerificationResponse']['response'])
        self.assertEquals('Approved', response['echeckVerificationResponse']['message'])


    def test_table_2_3_39(self):
        txn_dict = {
            'echeckVerification': {
                'orderId': '39',
                'amount': 3003,
                'orderSource': 'telephone',
                'id': 'thisisid',
                'billToAddress': {
                    'firstName': 'Robert',
                    'lastName': 'Jones',
                    'companyName': 'Good Goods Inc',
                    'phone': '999-999-9999',
                },
                'echeck': {
                    'accNum': '3099999999',
                    'accType': 'Corporate',
                    'routingNum': '053100300',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('950', response['echeckVerificationResponse']['response'])
        self.assertEquals('Decline - Negative Information on File', response['echeckVerificationResponse']['message'])


    def test_table_2_3_40(self):
        txn_dict = {
            'echeckVerification': {
                'orderId': '40',
                'amount': 3004,
                'orderSource': 'telephone',
                'id': 'thisisid',
                'billToAddress': {
                    'firstName': 'Peter',
                    'lastName': 'Green',
                    'companyName': 'Green Co',
                    'phone': '999-999-9999',
                },
                'echeck': {
                    'accNum': '8099999999',
                    'accType': 'Corporate',
                    'routingNum': '011075150',
                }
            }
        }
        response = online.request(txn_dict, conf)

        self.assertEquals('951', response['echeckVerificationResponse']['response'])
        self.assertEquals('Absolute Decline', response['echeckVerificationResponse']['message'])


    def test_table_2_5_41(self):
        txn_dict = {
            'echeckSale': {
                'orderId': '41',
                'amount': 2008,
                'orderSource': 'telephone',
                'id': 'thisisid',
                'billToAddress': {
                    'firstName': 'Mike',
                    'lastName': 'Hammer',
                    'middleInitial': 'J',
                    'phone': '999-999-9999',
                },
                'echeck': {
                    'accNum': '10@BC99999',
                    'accType': 'Checking',
                    'routingNum': '053100300',
                }
            }
        }
        response = online.request(txn_dict, conf)

        self.assertEquals('301', response['echeckSalesResponse']['response'])
        self.assertEquals('Invalid Account Number', response['echeckSalesResponse']['message'])


    def test_table_2_5_42(self):
        txn_dict = {
            'echeckSale': {
                'orderId': '42',
                'amount': 2004,
                'orderSource': 'telephone',
                'id': 'thisisid',
                'billToAddress': {
                    'firstName': 'Tom',
                    'lastName': 'Black',
                    'phone': '999-999-9999',
                },
                'echeck': {
                    'accNum': '4099999992',
                    'accType': 'Checking',
                    'routingNum': '011075150',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['echeckSalesResponse']['response'])
        self.assertEquals('Approved', response['echeckSalesResponse']['message'])

        # eCheck Void
        txn_dict = {
            'echeckVoid': {
                'cnpTxnId': response['echeckSalesResponse']['cnpTxnId'],
                'id': 'thisisid',
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['echeckVoidResponse']['response'])
        self.assertEquals('Approved', response['echeckVoidResponse']['message'])



    def test_table_2_5_43(self):
        txn_dict = {
            'echeckSale': {
                'orderId': '43',
                'amount': 2007,
                'orderSource': 'telephone',
                'id': 'thisisid',
                'billToAddress': {
                    'firstName': 'Peter',
                    'lastName': 'Green',
                    'companyName': 'Green Co',
                    'phone': '999-999-9999',
                },
                'echeck': {
                    'accNum': '6099999992',
                    'accType': 'Corporate',
                    'routingNum': '011075150',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['echeckSalesResponse']['response'])
        self.assertEquals('Approved', response['echeckSalesResponse']['message'])
        #TODO no accountUpdater element.


    def test_table_2_5_44(self):
        txn_dict = {
            'echeckSale': {
                'orderId': '44',
                'amount': 2009,
                'orderSource': 'telephone',
                'id': 'thisisid',
                'billToAddress': {
                    'firstName': 'Peter',
                    'lastName': 'Green',
                    'companyName': 'Green Co',
                    'phone': '999-999-9999',
                },
                'echeck': {
                    'accNum': '6099999992',
                    'accType': 'Corporate',
                    'routingNum': '053133052',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('900', response['echeckSalesResponse']['response'])
        self.assertEquals('Invalid Bank Routing Number', response['echeckSalesResponse']['message'])


    def test_table_2_6_45(self):
        txn_dict = {
            'echeckCredit': {
                'orderId': '45',
                'amount': 1001,
                'orderSource': 'telephone',
                'id': 'thisisid',
                'billToAddress': {
                    'firstName': 'John',
                    'lastName': 'John',
                    'phone': '999-999-9999',
                },
                'echeck': {
                    'accNum': '10@BC99999',
                    'accType': 'Checking',
                    'routingNum': '053100300',
                }
            }
        }
        response = online.request(txn_dict, conf)
        # TODO response is wrong.
        # self.assertEquals('301', response['echeckCreditResponse']['response'])
        # self.assertEquals('Invalid Account Number', response['echeckCreditResponse']['message'])


    def test_table_2_6_46(self):
        txn_dict = {
            'echeckCredit': {
                'orderId': '46',
                'amount': 1003,
                'orderSource': 'telephone',
                'id': 'thisisid',
                'billToAddress': {
                    'firstName': 'Robert',
                    'lastName': 'Jones',
                    'companyName': 'Good Goods Inc',
                    'phone': '999-999-9999',
                },
                'echeck': {
                    'accNum': '3099999999',
                    'accType': 'Corporate',
                    'routingNum': '053100300',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['echeckCreditResponse']['response'])
        self.assertEquals('Approved', response['echeckCreditResponse']['message'])

        # eCheck Void
        txn_dict = {
            'echeckVoid': {
                'cnpTxnId': response['echeckCreditResponse']['cnpTxnId'],
                'id': 'thisisid',
            }
        }
        response = online.request(txn_dict, conf)

        self.assertEquals('000', response['echeckVoidResponse']['response'])
        self.assertEquals('Approved', response['echeckVoidResponse']['message'])


    def test_table_2_6_47(self):
        txn_dict = {
            'echeckCredit': {
                'orderId': '47',
                'amount': 1007,
                'orderSource': 'telephone',
                'id': 'thisisid',
                'billToAddress': {
                    'firstName': 'Peter',
                    'lastName': 'Green',
                    'companyName': 'Green Co',
                    'phone': '999-999-9999',
                },
                'echeck': {
                    'accNum': '6099999993',
                    'accType': 'Corporate',
                    'routingNum': '211370545',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['echeckCreditResponse']['response'])
        self.assertEquals('Approved', response['echeckCreditResponse']['message'])
        # TODO no accountUpdater element.

    def test_table_2_6_48(self):
        txn_dict = {
            'echeckSale': {
                'orderId': '48',
                'amount': 2007,
                'orderSource': 'telephone',
                'id': 'thisisid',
                'billToAddress': {
                    'firstName': 'Peter',
                    'lastName': 'Green',
                    'companyName': 'Green Co',
                    'phone': '999-999-9999',
                },
                'echeck': {
                    'accNum': '6099999992',
                    'accType': 'Corporate',
                    'routingNum': '011075150',
                }
            }
        }
        response = online.request(txn_dict, conf)
        txn_dict = {
            'echeckCredit': {
                'cnpTxnId': response['echeckSalesResponse']['cnpTxnId'],
                'id': 'thisisid',
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['echeckCreditResponse']['response'])
        self.assertEquals('Approved', response['echeckCreditResponse']['message'])


    def test_table_2_6_49(self):
        # orderId *
        txn_dict = {
            'echeckCredit': {
                'cnpTxnId': '2',
                'id': 'thisisid',
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['echeckCreditResponse']['response'])
        self.assertEquals('Approved', response['echeckCreditResponse']['message'])

    def test_echeck_void_2_6(self):
        txn_dict = {
            'echeckVoid': {
                'cnpTxnId': '2',
                'id': 'thisisid',
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['echeckVoidResponse']['response'])


if __name__ == '__main__':
    unittest.main()
