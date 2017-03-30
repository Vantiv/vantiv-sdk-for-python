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
from __future__ import unicode_literals

import os
import sys
import unittest


package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

from vantivsdk import dict2obj

class TestUtils(unittest.TestCase):
    def test_map_dict(self):
        txn_dict = {
            'activate':{
                'amount': 1000,
                'card':{
                    'cardValidationNum':'123',
                    'expDate': '1212',
                    'number': '1',
                    'pin': '1',
                    'track': '1',
                    'type': 'VI',
                }
            }
        }
        obj = dict2obj.tofileds(txn_dict)
        self.assertEqual(1000, obj.amount)
        self.assertEqual('123', obj.card.cardValidationNum)


    def test_map_abs_group(self):
        txn_dict = {
            'accountUpdate':{
                'cardOrToken':{
                    'card':{
                        'cardValidationNum': '123',
                        'expDate': '1212',
                        'number': '1',
                        'pin': '1',
                        'track': '1',
                        'type': 'VI',
                    }
                }
            }
        }
        obj = dict2obj.tofileds(txn_dict)
        self.assertEqual('123', obj.cardOrToken.cardValidationNum)

    def test_map_multi_bind(self):
        txn_dict = {
            'authorization': {
                'enhancedData': {
                    'detailTax': [
                        {
                            'taxAmount': 100
                        },
                        {
                            'taxAmount': 200
                        },
                    ]
                }
            }
        }
        obj = dict2obj.tofileds(txn_dict)
        self.assertEqual(2, len(obj.enhancedData.detailTax))
        self.assertEqual(300, obj.enhancedData.detailTax[0].taxAmount + obj.enhancedData.detailTax[1].taxAmount)

if __name__ == '__main__':
    unittest.main()
