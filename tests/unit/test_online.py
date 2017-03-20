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
from unittest import mock
import six

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

from vantivsdk import (utils, online, fields)

conf = utils.Configuration()


class TestOnline(unittest.TestCase):
    def test_request_args_invalid_transaction(self):
        transaction = 1
        self.assertRaises(utils.VantivException, online.request, transaction, conf)

    def test_request_args_invalid_conf(self):
        transaction = fields.authorization()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        transaction.card = card
        conf_wrong = 1
        self.assertRaises(utils.VantivException, online.request, transaction, conf_wrong)

    def test_request_args_invalid_timeout(self):
        transaction = fields.authorization()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        transaction.card = card

        self.assertRaises(utils.VantivException, online.request, transaction, conf, 'dict', '-1')
        self.assertRaises(utils.VantivException, online.request, transaction, conf, 'dict', 'time')


    @mock.patch.object(online, '_http_post')
    def test_request_relturn_format(self, mock__http_post):
        transaction = fields.authorization()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        transaction.card = card

        mock__http_post.return_value = """<litleOnlineResponse version='11.0' response='1' message='Valid Format' xmlns='http://www.litle.com/schema'>
</litleOnlineResponse>
        """
        self.assertRaises(utils.VantivException, online.request, transaction, conf, 'dict')

        mock__http_post.return_value = """<litleOnlineResponse version='11.0' response='0' message='Valid Format' xmlns='http://www.litle.com/schema'>
          <authorizationResponse id='thisisid' reportGroup='Planets' customerId=''>
            <litleTxnId>4544691351798650001</litleTxnId>
            <orderId>12344</orderId>
            <response>000</response>
            <responseTime>2017-03-13T12:14:00</responseTime>
            <message>Approved</message>
            <authCode>07585</authCode>
            <accountUpdater>
              <originalCardInfo>
                <type>VI</type>
                <number>4100100000000000</number>
                <expDate>1110</expDate>
              </originalCardInfo>
              <newCardInfo>
                <type>VI</type>
                <number>4532694461984309</number>
                <expDate>1114</expDate>
              </newCardInfo>
            </accountUpdater>
            <networkTransactionId>63225578415568556365452427825</networkTransactionId>
          </authorizationResponse>
        </litleOnlineResponse>
                """
        # return dict
        response = online.request(transaction, conf)
        self.assertEquals('0', response['@response'])
        self.assertEquals('4544691351798650001', response['authorizationResponse']['litleTxnId'])
        self.assertIsInstance(response, dict)

        # return xml string
        response = online.request(transaction, conf, 'xml')
        self.assertIsInstance(response, str)

        # return fields object.
        response = online.request(transaction, conf, 'object')
        self.assertEquals('0', response.response)

if __name__ == '__main__':
    unittest.main()
