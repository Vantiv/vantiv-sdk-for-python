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
# import paramiko

if sys.version_info[0:2] >= (3, 4):
    from unittest import mock
else:
    from mock import mock


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

    @mock.patch.object(batch, '_get_file_str_from_sftp')
    def test_numAccountUpdates(self, mock__get_file_str_from_sftp):
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

        mock__get_file_str_from_sftp.return_value = """<cnpResponse version='12.10' response='0' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
                        <batchResponse cnpBatchId='12344' merchantId='56789' numAccountUpdates='3' xmlns='http://www.vantivcnp.com/schema'>
                            <saleResponse>
                                <cnpTxnId>123</cnpTxnId>
                                <accountUpdater>
                                    <accountUpdateSource>N</accountUpdateSource>
                                </accountUpdater>
                                </saleResponse>
                            </batchResponse>
                       </cnpResponse>
                       """

        response = batch.retrieve('retrieve_file', conf)
        self.assertEquals(response['batchResponse']['saleResponse']['cnpTxnId'], '123')
        self.assertEquals(response['batchResponse']['@numAccountUpdates'], '3')

    @mock.patch.object(batch, '_get_file_str_from_sftp')
    def test_passanger_transport_data_with_auth_max(self, mock__get_file_str_from_sftp):
        transaction = fields.authorization()
        transaction.id = 'thisisid'
        transaction.customerId = 'Cust0403'
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card

        transport_data = fields.passengerTransportData()
        transport_data.passengerName = 'Post Ma12'
        transport_data.ticketNumber = 'abc123456789'
        transport_data.issuingCarrier = 'AMK'
        transport_data.carrierName = 'AMTKTY'
        transport_data.restrictedTicketIndicator = '11DFG111'
        transport_data.numberOfAdults = 0
        transport_data.numberOfChildren = 9
        transport_data.customerCode = 'code12'
        transport_data.arrivalDate = '2022-01-22'
        transport_data.issueDate = '2021-02-03'
        transport_data.travelAgencyCode = '420104'
        transport_data.travelAgencyName = 'TravelAgency'
        transport_data.computerizedReservationSystem = 'DATS'
        transport_data.creditReasonIndicator = 'A'
        transport_data.ticketChangeIndicator = 'N'
        transport_data.ticketIssuerAddress = 'US'
        transport_data.exchangeTicketNumber = 'Ticket010'
        transport_data.exchangeAmount = '20210'
        transport_data.exchangeFeeAmount = '201010'

        transaction.transport_data = transport_data

        tripleg_data = fields.tripLegData()
        tripleg_data.tripLegNumber = '10'
        tripleg_data.departureCode = 'Code1'
        tripleg_data.carrierCode = 'code2'
        tripleg_data.serviceClass = 'First'
        tripleg_data.stopOverCode = 'Codestop'
        tripleg_data.destinationCode = 'DestCode2'
        tripleg_data.fareBasisCode = 'farecode2'
        tripleg_data.departureDate = '2022-01-01'
        tripleg_data.originCity = 'LA'
        tripleg_data.travelNumber = '1234'
        tripleg_data.departureTime = '02:00'
        tripleg_data.arrivalTime = '01:00'
        tripleg_data.remarks = 'remarks'
        transaction.tripleg_data = tripleg_data
        transaction.crypto = False

        mock__get_file_str_from_sftp.return_value = """<cnpResponse version='12.27' response='0' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
                                  <batchResponse cnpBatchId='12344' merchantId='56789' numAccountUpdates='3' xmlns='http://www.vantivcnp.com/schema'>
                                      <saleResponse>
                                          <cnpTxnId>123</cnpTxnId>
                                          <accountUpdater>
                                              <accountUpdateSource>N</accountUpdateSource>
                                          </accountUpdater>
                                          </saleResponse>
                                      </batchResponse>
                                 </cnpResponse>
                                 """
        response = batch.retrieve('retrieve_file', conf)
        self.assertEquals(response['batchResponse']['saleResponse']['cnpTxnId'], '123')
        self.assertEquals(response['batchResponse']['@numAccountUpdates'], '3')

    @mock.patch.object(batch, '_get_file_str_from_sftp')
    def test_request_for_authIndicatorEnumIncremental(self, mock__get_file_str_from_sftp):
        authorization = fields.authorization()
        authorization.id = '1234'
        authorization.customerId = 'Cust0404'
        authorization.reportGroup = 'Default'
        authorization.cnpTxnId = '34659348401'
        authorization.amount = '106'
        authorization.authIndicator = 'Incremental'

        mock__get_file_str_from_sftp.return_value = """
             <cnpResponse xmlns="http://www.vantivcnp.com/schema" version="12.30" response="0" message="Valid Format">
                 <batchResponse cnpBatchId='12344' merchantId='56789' numAccountUpdates='3' xmlns='http://www.vantivcnp.com/schema'>
                     <authorizationResponse id="auth_GP_success_MC_MerEnabled" reportGroup="DirectWFITxn">
                         <cnpTxnId>587273030852445843</cnpTxnId>
                         <orderId />
                         <response>000</response>
                         <message>Approved</message>
                         <responseTime>2023-03-24T12:17:29.664</responseTime>
                         <location>sandbox</location>
                      </authorizationResponse>   
                 </batchResponse>
             </cnpResponse>
             """

        response = batch.retrieve('retrieve_file', conf)
        self.assertEquals(response['batchResponse']['authorizationResponse']['cnpTxnId'], '587273030852445843')
        self.assertEquals(response['batchResponse']['@numAccountUpdates'], '3')

    @mock.patch.object(batch, '_get_file_str_from_sftp')
    def test_request_for_orderChannelEnumMIT_sellerInfo_authIndicatorEstimated(self, mock__get_file_str_from_sftp):
        authorization = fields.authorization()
        authorization.id = '1'
        authorization.customerId = 'Cust0403'
        authorization.reportGroup = 'Default Report Group'
        authorization.orderId = '12344401'
        authorization.amount = '106'
        authorization.orderSource = 'ecommerce'

        seller_info = fields.sellerInfo()
        seller_info.accountNumber = '4485581000000005'
        seller_info.aggregateOrderCount = '4'
        seller_info.aggregateOrderDollars = '104'

        seller_address = fields.sellerAddress()
        seller_address.sellerStreetaddress = '15 Main Street'
        seller_address.sellerUnit = '100 AB'
        seller_address.sellerPostalcode = '12345'
        seller_address.sellerCity = 'San Jose'
        seller_address.sellerProvincecode = 'MA'
        seller_address.sellerCountrycode = 'US'
        seller_info.sellerAddress = seller_address

        seller_info.createdDate = '2015-11-12T20:33:09'
        seller_info.domain = 'vap'
        seller_info.email = 'bob@example.com'
        seller_info.lastUpdateDate = '2015-11-12T20:33:09'
        seller_info.name = 'bob'
        seller_info.onboardingEmail = 'bob@example.com'
        seller_info.onboardingIpAddress = '75.100.88.78'
        seller_info.parentEntity = 'abc'
        seller_info.phone = '9785510040'
        seller_info.sellerId = '123456789'

        seller_tags = fields.sellerTagsType
        seller_tags.tag = '2'
        seller_info.seller_tags = seller_tags
        seller_info.username = 'bob123'

        authorization.seller_info = seller_info

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        authorization.card = card

        authorization.orderChannel = 'MIT'
        authorization.authIndicator = 'Estimated'

        mock__get_file_str_from_sftp.return_value = """
                 <cnpResponse xmlns="http://www.vantivcnp.com/schema" version="12.30" response="0" message="Valid Format">
                 <batchResponse cnpBatchId='12344' merchantId='56789' numAccountUpdates='3' xmlns='http://www.vantivcnp.com/schema'>
                     <authorizationResponse id="auth_GP_success_MC_MerEnabled" reportGroup="DirectWFITxn">
                         <cnpTxnId>328357670706189403</cnpTxnId>
                         <orderId>XGR-1840823423</orderId>
                         <response>000</response>
                         <message>Approved</message>
                         <responseTime>2023-03-24T12:34:09.484</responseTime>
                         <authCode>06613</authCode>
                         <location>sandbox</location>
                     </authorizationResponse>
                 </batchResponse>
                 </cnpResponse> """

         # return dict
        response = batch.retrieve('retrieve_file', conf)
        self.assertEquals(response['batchResponse']['authorizationResponse']['cnpTxnId'], '328357670706189403')
        self.assertEquals(response['batchResponse']['@numAccountUpdates'], '3')

    @mock.patch.object(batch, '_get_file_str_from_sftp')
    def test_oerderChannelEnumMIT_sellerInfo(self, mock__get_file_str_from_sftp):
        transaction = fields.sale()
        transaction.id = 'auth_GP_DI'
        transaction.reportGroup = 'DirectWFITxn'
        transaction.orderId = 'XGR-1840823423'
        transaction.amount = 1100
        transaction.orderSource = 'telephone'
        seller_info = fields.sellerInfo()
        seller_info.accountNumber = '6557959585426472'
        seller_info.aggregateOrderCount = '4'
        seller_info.aggregateOrderDollars = '100'
        seller_address = fields.sellerAddress()
        seller_address.sellerStreetaddress = '15 Main Street'
        seller_address.sellerUnit = '100 AB'
        seller_address.sellerPostalcode = '12345'
        seller_address.sellerCity = 'San Jose'
        seller_address.sellerProvincecode = 'MA'
        seller_address.sellerCountrycode = 'US'
        seller_info.sellerAddress = seller_address
        seller_info.createdDate = '2015-11-12T20:33:09'
        seller_info.domain = 'vap'
        seller_info.email = 'bob@example.com'
        seller_info.lastUpdateDate = '2015-11-12T20:33:09'
        seller_info.name = 'bob'
        seller_info.onboardingEmail = 'bob@example.com'
        seller_info.onboardingIpAddress = '75.100.88.78'
        seller_info.parentEntity = 'abc'
        seller_info.phone = '9785510040'
        seller_info.sellerId = '123456789'
        seller_tags = fields.sellerTagsType
        seller_tags.tag = '2'
        seller_info.seller_tags = seller_tags
        seller_info.username = 'bob123'
        transaction.seller_info = seller_info
        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card
        transaction.orderChannel = 'MIT'

        mock__get_file_str_from_sftp.return_value = """
                           <cnpResponse version='12.29' response='0' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
                                     <batchResponse cnpBatchId='12344' merchantId='DirectWFITxn' numAccountUpdates='3' xmlns='http://www.vantivcnp.com/schema'>
                                            <saleResponse id="auth_GP_DI" reportGroup="DirectWFITxn">
                                                 <cnpTxnId>427453992541199977</cnpTxnId>
                                                 <orderId>XGR-1840823423</orderId>
                                                 <response>000</response>
                                                 <message>Approved</message>
                                                 <responseTime>2023-03-27T09:27:19.759</responseTime>
                                                 <authCode>00229</authCode>
                                                 <networkTransactionId>63225578415568556365452427825</networkTransactionId>
                                                 <location>sandbox</location>
                                            </saleResponse>
                                     </batchResponse>
                           </cnpResponse>"""
        response = batch.retrieve('retrieve_file', conf)
        self.assertEquals(response['batchResponse']['saleResponse']['cnpTxnId'], '427453992541199977')
        self.assertEquals(response['batchResponse']['@numAccountUpdates'], '3')

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
#     <cnpTxnId>82920136495185966</cnpTxnId>
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
#     <cnpTxnId>82920136495185974</cnpTxnId>
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
#     <cnpTxnId>82920136495185982</cnpTxnId>
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
#         self.assertEquals('4544691351798650001', response['authorizationResponse']['cnpTxnId'])
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
