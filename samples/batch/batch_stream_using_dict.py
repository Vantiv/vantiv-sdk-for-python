# -*- coding: utf-8 -*-
# Copyright (c) 2017 Vantiv eCommerce
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
from __future__ import print_function

import os
import sys

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

from vantivsdk import *

# Initial Configuration object. If you have saved configuration in '.vantiv_python_sdk.conf' at system environment
# variable: VANTIV_SDK_CONFIG or user home directory, the saved configuration will be automatically load.
conf_dict ={'print_xml': True}

conf = utils.Configuration(conf_dict)

txns_dict ={
    'authorization':[
        {
            'reportGroup': 'Planets',
            'orderId': '12344',
            'amount': '100',
            'orderSource': 'ecommerce',
            'id': 'thisisid',
            'card': {
                'expDate': '0121',
                'number': '4457010000000009',
                'type': 'VI',
                'cardValidationNum':'349'
            },
            'billToAddress':{
                'firstName': 'Mike',
                'middleInitial': 'J',
                'lastName': 'Hammer',
                'phone': '999-999-9999',
            }
        },
        {
            'reportGroup': 'Planets',
            'orderId': '12344',
            'amount': '100',
            'orderSource': 'ecommerce',
            'id': 'thisisid',
            'card': {
                'expDate': '0121',
                'number': '4457010000000009',
                'type': 'VI',
                'cardValidationNum':'349'
            },
            'billToAddress': {
                'firstName': 'Mike',
                'middleInitial': 'J',
                'lastName': 'Hammer',
                'phone': '999-999-9999',
            }
        },
    ],
    'sale':{
        'reportGroup': 'Planets',
        'orderId': '12344',
        'amount': '100',
        'orderSource': 'ecommerce',
        'id': 'thisisid',
        'card': {
            'expDate': '0121',
            'number': '4457010000000009',
            'type': 'VI',
            'cardValidationNum': '349'
        },
        'billToAddress': {
            'firstName': 'Mike',
            'middleInitial': 'J',
            'lastName': 'Hammer',
            'phone': '999-999-9999',
        }
    },
}

# stream to Vaitiv eCommerce and get object as response
response = batch.stream(txns_dict, conf)

# In your sample, you can ignore this
if response['@message'] != 'Valid Format':
    raise Exception('the example does not give the right response')

# Example for RFRRequest
RFRRequest = fields.RFRRequest()
RFRRequest.litleSessionId = response['@litleSessionId']

# Initial Transactions container, because RFRRequest and batchRequest cannot be in same session file
transactions = batch.Transactions()
transactions.add(RFRRequest)

# stream to Vaitiv eCommerce and get object as response
response = batch.stream(transactions, conf)

# In your sample, you can ignore this
if response['@message'] != 'Valid Format':
    raise Exception('the example does not give the right response')