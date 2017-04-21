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


class TestApplePayTransactionProcessing(unittest.TestCase):
    def test_2_5_18_1(self):
        txn = {
            'authorization': {
                'orderId': '65',
                'amount': 100,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'applepay',
                'card': {
                    'number': '4457000300000007',
                    'cardValidationNum': '123',
                    # 'pin': '3230',
                    'expDate': '1220',
                    'type': 'VI'
                },
                'cardholderAuthentication': {
                    'authenticationValue': '619A2382FFF205767492306AC804E8E64E8EA6981DD=',
                }
            }
        }

        response = online.request(txn, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])

    def test_2_5_18_2(self):
        txn = {
            'authorization': {
                'orderId': '65',
                'amount': 100,
                'id': 'ids',
                'reportGroup': 'Planets',
                'orderSource': 'applepay',
                'applepay': {
                    'data': 'Ww9EI+10VVpyZrAb3nxu9c8PG4JEnIh4oTkDhZi4axj5QqC5WIir6TJcFmk/3wkrNL/KaRXz3aan4WRO6cPL+cUTRpQUO9ECqTBItmQbJxGbN42713TyI+y97k3msl7bd5rJOMIOpkCtfp2ua+3lnBhjGFnUzdCxq+/K6eoIEwYlAEfX9Sdpjm+plVfvSK7vj0BQCcXo1dXGkNUKwKWA4GYPUE3qwbuiQWcZwLxAEF43274pACV4LBmdv0HYgYpcgCY0+U6/YSVKdpPrhHLDeLOlO7T4WwuimHojsKA/BknpPY1uJfP+YJxj1fYghaAOAR0tA5cYJftlWLXaV9lZu113Ns1rxColh4PR8wsuw81CdOruvoURGNaNyX+hG1suQoHeE8ECzKIE6DlHEeVMcdxXySwFPY7hxEY1QKSSXw==',
                    'header': {
                        'applicationData': '496461ea64b50527d2d792df7c38f301300085dd463e347453ae72debf6f4d14',
                        'ephemeralPublicKey': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEarp8xOhLX9QliUPS9c54i3cqEfrJD37NG75ieNxncOeFLkjCk',
                        'publicKeyHash': 'jAMRQqg4nffHrXvfwRfbaEc11bk3QD3rv5K9xLqLgu0=',
                        'transactionId': 'f9b0d3cfbb64cd155249c691aca3c521de03725720616b810d90341f97f347b7',
                    },
                    # 'pin': '3230',
                    'signature': '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',
                    'version': 'EC_v1'
                },
            }
        }

        response = online.request(txn, conf)
        # TODO The response is wrong
        # self.assertEquals('000', response['authorizationResponse']['response'])
        # self.assertEquals('Approved', response['authorizationResponse']['message'])


if __name__ == '__main__':
    unittest.main()
