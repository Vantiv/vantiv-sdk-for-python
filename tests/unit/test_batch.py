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

from vantivsdk import (utils, batch, fields)

conf = utils.Configuration()


class TestBatch(unittest.TestCase):
    def test_Transactions_add_normal_txn(self):
        txns = batch.Transactions()
        for i in range(1,3):
            transaction = fields.authorization()
            txns.add(transaction)
        self.assertEquals(False, txns.is_rfr_request)
        self.assertEquals(2, len(txns.transactions))

    def test_Transactions_add_rfrrequest(self):
        txns = batch.Transactions()
        transaction = fields.RFRRequest()
        txns.add(transaction)
        self.assertEquals(True, txns.is_rfr_request)
        self.assertEquals(1, len(txns.transactions))
        transaction = fields.RFRRequest()
        self.assertRaises(utils.VantivException, txns.add, transaction)

    def test_Transactions_mix_rfrrequest_normal_txn(self):
        rfr = fields.RFRRequest()
        normal = fields.authorization()

        txns = batch.Transactions()
        txns.add(rfr)
        self.assertRaises(utils.VantivException, txns.add, normal)

        txns = batch.Transactions()
        txns.add(normal)
        self.assertRaises(utils.VantivException, txns.add, rfr)


    def test_Transactions_online_only_txn(self):
        transaction = fields.deactivateReversal()
        txns = batch.Transactions()
        self.assertRaises(utils.VantivException, txns.add, transaction)


    def test_Transactions_duplicate_normal_txn(self):
        normal = fields.authorization()
        txns = batch.Transactions()
        txns.add(normal)
        self.assertRaises(utils.VantivException, txns.add, normal)

    @mock.patch.object(batch, '_put_file_to_sftp')
    def test_submit(self, mock__put_file_to_sftp):
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

        txns = batch.Transactions()
        txns.add(transaction)

        # first arg is not instance of batch.Transactions
        self.assertRaises(utils.VantivException, batch.submit, transaction, conf)

        # first arg is an new instance of utils.Configuration
        self.assertRaises(utils.VantivException, batch.submit, batch.Transactions(), conf)

        # second arg is not instance of utils.Configuration
        self.assertRaises(utils.VantivException, batch.submit, txns, 1)

        # Third arg is not sring
        self.assertRaises(utils.VantivException, batch.submit, txns, conf, txns)

        # Fourth arg is not positive int
        self.assertRaises(utils.VantivException, batch.submit, txns, conf, 'aaa', -1)

        mock__put_file_to_sftp.return_value = 'filename'

        self.assertEquals('filename', batch.submit(txns, conf))

    def test_download(self):
        # first arg is str and len less than 4
        self.assertRaises(utils.VantivException, batch.download, 'abc', conf)

        # second arg is not instance of utils.Configuration
        self.assertRaises(utils.VantivException, batch.download, 'abcd', 1)

        # Fourth arg is not positive int
        self.assertRaises(utils.VantivException, batch.download, 'abcd', conf, False, -1)

# TODO
#     @mock.patch.object(batch, '_get_file_str_from_sftp')
#     @mock.patch.object(batch, '_save_str_file')
#     def test_retrieve(self, mock__get_file_str_from_sftp, mock__save_str_file):
#         # first arg is str and len less than 4
#         self.assertRaises(utils.VantivException, batch.retrieve, 'abc', conf)
#
#         # second arg is not instance of utils.Configuration
#         self.assertRaises(utils.VantivException, batch.retrieve, 'abcd', 1)
#
#         # Fourth arg is not positive int
#         self.assertRaises(utils.VantivException, batch.retrieve, 'abcd', conf, 'dict', -1)
#
#         mock__get_file_str_from_sftp.return_value = '''<litleResponse version="11.0" xmlns="http://www.litle.com/schema" id="" response="0" message="Valid Format" litleSessionId="82920136495185933">
# <batchResponse litleBatchId="82920136495185941" merchantId="1288791">
# <authorizationResponse id="thisisid" reportGroup="Planets">
#     <litleTxnId>82920136495185966</litleTxnId>
#     <orderId>2</orderId>
#     <response>000</response>
#     <responseTime>2017-03-13T18:53:30</responseTime>
#     <message>Approved</message>
#     <authCode>11111 </authCode>
#     <fraudResult>
#         <avsResult>34</avsResult>
#         <cardValidationResult>M</cardValidationResult>
#     </fraudResult>
#     <networkTransactionId>000000000000000</networkTransactionId>
# </authorizationResponse>
# <authorizationResponse id="thisisid" reportGroup="Planets">
#     <litleTxnId>82920136495185974</litleTxnId>
#     <orderId>1</orderId>
#     <response>000</response>
#     <responseTime>2017-03-13T18:53:30</responseTime>
#     <message>Approved</message>
#     <authCode>11111 </authCode>
#     <fraudResult>
#         <avsResult>34</avsResult>
#         <cardValidationResult>M</cardValidationResult>
#     </fraudResult>
#     <networkTransactionId>000000000000000</networkTransactionId>
# </authorizationResponse>
# <saleResponse id="thisisid" reportGroup="Planets">
#     <litleTxnId>82920136495185982</litleTxnId>
#     <orderId>1</orderId>
#     <response>000</response>
#     <responseTime>2017-03-13T18:53:31</responseTime>
#     <message>Approved</message>
#     <authCode>11111 </authCode>
#     <fraudResult>
#         <avsResult>34</avsResult>
#         <cardValidationResult>M</cardValidationResult>
#     </fraudResult>
#     <networkTransactionId>000000000000000</networkTransactionId>
# </saleResponse>
# </batchResponse>
# </litleResponse>
#         '''
#         mock__save_str_file.return_value = True
#
#         # return dict
#         response = batch.retrieve('abcd', conf, 'dict', False)
#         self.assertEquals('0', response['@response'])
#         self.assertEquals('4544691351798650001', response['authorizationResponse']['litleTxnId'])
#         self.assertIsInstance(response, dict)
#
#         # return xml string
#         response = batch.retrieve('abcd', conf, 'xml')
#         self.assertIsInstance(response, str)
#
#         # return fields object.
#         response = batch.retrieve('abcd', conf, 'object')
#         self.assertEquals('0', response.response)


if __name__ == '__main__':
    unittest.main()
