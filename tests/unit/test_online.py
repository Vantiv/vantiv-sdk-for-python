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
import re
import datetime

if sys.version_info[0:2] >= (3, 4):
    from unittest import mock
else:
    from mock import mock


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
        customerInfo = fields.customerInfo()

        customerInfo.accountUserName = 'Jack'
        customerInfo.userAccountNumber = '1234'
        customerInfo.userAccountEmail = 'gmail@gmail.com'
        customerInfo.membershipId = '11111'
        customerInfo.membershipPhone = '123456'
        customerInfo.membershipEmail = 'gmail@gmail.com'
        customerInfo.membershipName = 'fran'
        customerInfo.accountCreatedDate = datetime.datetime.now().strftime("%Y-%m-%d")
        customerInfo.userAccountPhone = '000461223'
        transaction.customerInfo = customerInfo
        detailTaxList = list()
        detailTax = fields.detailTax()
        detailTax.taxAmount = 100
        detailTax2 = fields.detailTax()
        detailTax2.taxAmount = 200
        detailTaxList.append(detailTax)
        detailTaxList.append(detailTax2)
        lineItemDataList = list()
        lineItemData = fields.lineItemData()
        lineItemData.itemDescription = 'des'
        lineItemData.itemCategory = 'Chock'
        lineItemData.itemCategory = 'Chock'
        lineItemData.itemSubCategory = 'pen'
        lineItemData.productId = '001'
        lineItemData.productName = 'prod'
        lineItemDataList.append(lineItemData)
        enhancedData = fields.enhancedData()
        enhancedData.detailTax = detailTaxList
        enhancedData.lineItemData = lineItemDataList
        enhancedData.discountCode = '001'
        enhancedData.discountPercent = '10'
        enhancedData.fulfilmentMethodType = 'DELIVERY'

        transaction.enhancedData = enhancedData

        # Create contact object
        contact = fields.contact()
        contact.name = 'John & Mary Smith'
        contact.addressLine1 = '1 Main St.'
        contact.city = 'Burlington'
        contact.state = 'MA'
        contact.zip = '01803-3747'
        contact.country = 'USA'
        contact.sellerID = '123'
        contact.url = 'http://tax.xom'
        # The type of retailerAddress is contact
        transaction.retailerAddress = contact

        additionalCOFData = fields.additionalCOFData()
        additionalCOFData.totalPaymentCount = '35'
        additionalCOFData.paymentType = 'Fixed Amount'
        additionalCOFData.uniqueId = '12345wereew233'
        additionalCOFData.frequencyOfMIT = 'BiWeekly'
        additionalCOFData.validationReference = 're3298rhriw4wrw'
        additionalCOFData.sequenceIndicator = '2'

        transaction.additionalCOFData = additionalCOFData

        transaction.crypto = False

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='1' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
</cnpOnlineResponse>
        """
        self.assertRaises(utils.VantivException, online.request, transaction, conf, 'dict')

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='0' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
          <authorizationResponse id='thisisid' reportGroup='Planets' customerId=''>
            <cnpTxnId>4544691351798650001</cnpTxnId>
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
        </cnpOnlineResponse>
                """
        # return dict
        response = online.request(transaction, conf)
        self.assertEquals('0', response['@response'])
        self.assertEquals('4544691351798650001', response['authorizationResponse']['cnpTxnId'])
        self.assertIsInstance(response, dict)

        # return xml string
        response = online.request(transaction, conf, 'xml')
        self.assertIsInstance(response, str)

        # return fields object.
        response = online.request(transaction, conf, 'object')
        self.assertEquals('0', response.response)

    @mock.patch.object(online, '_http_post')
    def test_request_for_guaranteed_payment_with_passengerTransportData(self, mock__http_post):
        transaction = fields.authorization()
        transaction.id = '1'
        transaction.customerId = 'Cust0403'
        transaction.reportGroup = 'русский中文'
        transaction.orderId = '12344401'
        transaction.amount = 500
        transaction.orderSource = 'ecommerce'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card

        additionalCOFData = fields.additionalCOFData()
        additionalCOFData.totalPaymentCount = '35'
        additionalCOFData.paymentType = 'Fixed Amount'
        additionalCOFData.uniqueId = '12345wereew233'
        additionalCOFData.frequencyOfMIT = 'BiWeekly'
        additionalCOFData.validationReference = 're3298rhriw4wrw'
        additionalCOFData.sequenceIndicator = '2'

        transaction.additionalCOFData = additionalCOFData

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

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='1' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
        </cnpOnlineResponse>
            """
        self.assertRaises(utils.VantivException, online.request, transaction, conf, 'dict')

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='0' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
            <authorizationResponse id='thisisid' reportGroup='Planets' customerId=''>
            <cnpTxnId>135967334095735957</cnpTxnId>
            <orderId>TC137654_1_DI_402</orderId>
            <response>000</response>
            <responseTime>2022-11-23T10:39:23.192</responseTime>
            <message>Approved</message>
            <authCode>75354</authCode>
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
            <authMax>
                <authMaxApplied>true</authMaxApplied>
                <networkTokenApplied>true</networkTokenApplied>
                <networkToken>1112000199940085</networkToken>
                <authMaxResponseCode>000</authMaxResponseCode>
                <authMaxResponseMessage>Approved</authMaxResponseMessage>
            </authMax>
            </authorizationResponse>
            </cnpOnlineResponse>
                    """

        # return dict
        response = online.request(transaction, conf)
        self.assertEquals('0', response['@response'])
        self.assertEquals('135967334095735957', response['authorizationResponse']['cnpTxnId'])
        self.assertIsInstance(response, dict)

        # return xml string
        response = online.request(transaction, conf, 'xml')
        self.assertIsInstance(response, str)

        # return fields object.
        response = online.request(transaction, conf, 'object')
        self.assertEquals('0', response.response)


    @mock.patch.object(online, '_http_post')
    def test_request_relturn_format2(self, mock__http_post):
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

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='1' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
</cnpOnlineResponse>
        """
        self.assertRaises(utils.VantivException, online.request, transaction, conf, 'dict')

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='0' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
          <authorizationResponse id='thisisid' reportGroup='Planets' customerId=''>
            <cnpTxnId>4544691351798650001</cnpTxnId>
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
        </cnpOnlineResponse>
                """
        # return dict
        response = online.request(transaction, conf)
        self.assertEquals('0', response['@response'])
        self.assertEquals('4544691351798650001', response['authorizationResponse']['cnpTxnId'])
        self.assertIsInstance(response, dict)

        # return xml string
        response = online.request(transaction, conf, 'xml')
        self.assertIsInstance(response, str)

        # return fields object.
        response = online.request(transaction, conf, 'object')
        self.assertEquals('0', response.response)

    @mock.patch.object(online, '_http_post')
    def test_sale_with_Realtime_accountUpdater(self, mock__http_post):
        transaction = fields.sale()
        transaction.id = '12345'
        transaction.amount = 106
        transaction.cnpTxnId = 123456
        transaction.orderId = '12344'
        transaction.orderSource = 'ecommerce'

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4100000000000000'
        card.expDate = '1210'
        transaction.card = card

        mock__http_post.return_value = """<cnpOnlineResponse version='12.10' response='0' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
                <saleResponse>
                    <cnpTxnId>123</cnpTxnId>
                    <accountUpdater>
                        <accountUpdateSource>R</accountUpdateSource>
                    </accountUpdater>
                </saleResponse>
            </cnpOnlineResponse>
            """

        response = online.request(transaction, conf)
        self.assertEquals('123', response['saleResponse']['cnpTxnId'])
        self.assertEquals("R", response['saleResponse']['accountUpdater']['accountUpdateSource'])

    @mock.patch.object(online, '_http_post')
    def test_sale_with_nonrealtime_accountUpdater(self, mock__http_post):
        transaction = fields.sale()
        transaction.id = '12345'
        transaction.amount = 106
        transaction.cnpTxnId = 123456
        transaction.orderId = '12344'
        transaction.orderSource = 'ecommerce'

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4100000000000000'
        card.expDate = '1210'
        transaction.card = card

        mock__http_post.return_value = """<cnpOnlineResponse version='12.10' response='0' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
                   <saleResponse>
                       <cnpTxnId>123</cnpTxnId>
                       <accountUpdater>
                           <accountUpdateSource>N</accountUpdateSource>
                       </accountUpdater>
                   </saleResponse>
               </cnpOnlineResponse>
               """

        response = online.request(transaction, conf)
        self.assertEquals('123', response['saleResponse']['cnpTxnId'])
        self.assertEquals("N", response['saleResponse']['accountUpdater']['accountUpdateSource'])

    @mock.patch.object(online, '_http_post')
    def test_auth_with_mcc(self, mock__http_post):
        transaction = fields.authorization()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.merchantCategoryCode = '3535'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4100000000000002'
        card.expDate = '1210'

        transaction.card = card

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='1' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
        </cnpOnlineResponse>
                """
        self.assertRaises(utils.VantivException, online.request, transaction, conf, 'dict')

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='0' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
                  <authorizationResponse id='thisisid' reportGroup='Planets' customerId=''>
                    <cnpTxnId>4544691351798650001</cnpTxnId>
                    <orderId>12344</orderId>
                    <response>000</response>
                    <responseTime>2017-03-13T12:14:00</responseTime>
                    <message>Approved</message>
                    <authCode>07585</authCode>
                    <accountUpdater>
                      <originalCardInfo>
                        <type>VI</type>
                        <number>4100000000000002</number>
                        <expDate>1210</expDate>
                      </originalCardInfo>
                      <newCardInfo>
                        <type>VI</type>
                        <number>4532694461984309</number>
                        <expDate>1114</expDate>
                      </newCardInfo>
                    </accountUpdater>
                    <networkTransactionId>63225578415568556365452427825</networkTransactionId>
                  </authorizationResponse>
                  <merchantCategoryCode>3535</merchantCategoryCode>
                </cnpOnlineResponse>
                        """

        response = online.request(transaction, conf)
        self.assertEquals("000", response['authorizationResponse']['response'])
        self.assertEquals("3535", response['merchantCategoryCode'])

    @mock.patch.object(online, '_http_post')
    def test_force_cap_with_mcc(self, mock__http_post):
        transaction = fields.forceCapture()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.merchantCategoryCode = '3535'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4100000000000002'
        card.expDate = '1210'

        transaction.card = card

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='1' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
          </cnpOnlineResponse>
                  """
        self.assertRaises(utils.VantivException, online.request, transaction, conf, 'dict')

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='0' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
                    <authorizationResponse id='thisisid' reportGroup='Planets' customerId=''>
                      <cnpTxnId>4544691351798650001</cnpTxnId>
                      <orderId>12344</orderId>
                      <response>000</response>
                      <responseTime>2017-03-13T12:14:00</responseTime>
                      <message>Approved</message>
                      <authCode>07585</authCode>
                      <accountUpdater>
                        <originalCardInfo>
                          <type>VI</type>
                          <number>4100000000000002</number>
                          <expDate>1210</expDate>
                        </originalCardInfo>
                        <newCardInfo>
                          <type>VI</type>
                          <number>4532694461984309</number>
                          <expDate>1114</expDate>
                        </newCardInfo>
                      </accountUpdater>
                      <networkTransactionId>63225578415568556365452427825</networkTransactionId>
                    </authorizationResponse>
                    <merchantCategoryCode>3535</merchantCategoryCode>
                  </cnpOnlineResponse>
                          """

        response = online.request(transaction, conf)
        self.assertEquals("000", response['authorizationResponse']['response'])
        self.assertEquals("3535", response['merchantCategoryCode'])

    @mock.patch.object(online, '_http_post')
    def test_credit_with_mcc(self, mock__http_post):
        transaction = fields.credit()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '56789'
        transaction.amount = 100
        transaction.orderSource = 'ecommerce'
        transaction.merchantCategoryCode = '7890'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4100000000000100'
        card.expDate = '1210'

        transaction.card = card

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='1' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
              </cnpOnlineResponse>
                      """
        self.assertRaises(utils.VantivException, online.request, transaction, conf, 'dict')

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='0' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
                        <authorizationResponse id='thisisid' reportGroup='Planets' customerId=''>
                          <cnpTxnId>4544691351798650001</cnpTxnId>
                          <orderId>56789</orderId>
                          <response>000</response>
                          <responseTime>2017-03-13T12:14:00</responseTime>
                          <message>Approved</message>
                          <authCode>07585</authCode>
                          <accountUpdater>
                            <originalCardInfo>
                              <type>VI</type>
                              <number>4100000000000100</number>
                              <expDate>1210</expDate>
                            </originalCardInfo>
                            <newCardInfo>
                              <type>VI</type>
                              <number>4532694461984309</number>
                              <expDate>1114</expDate>
                            </newCardInfo>
                          </accountUpdater>
                          <networkTransactionId>63225578415568556365452427825</networkTransactionId>
                        </authorizationResponse>
                        <merchantCategoryCode>7890</merchantCategoryCode>
                      </cnpOnlineResponse>
                              """

        response = online.request(transaction, conf)
        self.assertEquals("000", response['authorizationResponse']['response'])
        self.assertEquals("7890", response['merchantCategoryCode'])

    @mock.patch.object(online, '_http_post')
    def test_echeck__credit_with_mcc(self, mock__http_post):

        transaction = fields.echeckCredit()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        echeck = fields.echeckType()
        echeck.accNum = '12345657890'
        echeck.routingNum = '123456789'
        echeck.checkNum = '123455'
        transaction.merchantCategoryCode = '7890'
        echeck.accType = 'Checking'
        transaction.echeck = echeck

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Peter'
        billtoaddress.lastName = 'Green'
        billtoaddress.companyName = 'Green Co'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4100000000000100'
        card.expDate = '1210'

        transaction.card = card

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='1' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
                    </cnpOnlineResponse>
                            """
        self.assertRaises(utils.VantivException, online.request, transaction, conf, 'dict')

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='0' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
                              <authorizationResponse id='thisisid' reportGroup='Planets' customerId=''>
                                <cnpTxnId>4544691351798650001</cnpTxnId>
                                <orderId>56789</orderId>
                                <response>000</response>
                                <responseTime>2017-03-13T12:14:00</responseTime>
                                <message>Approved</message>
                                <authCode>07585</authCode>
                                <accountUpdater>
                                  <originalCardInfo>
                                    <type>VI</type>
                                    <number>4100000000000100</number>
                                    <expDate>1210</expDate>
                                  </originalCardInfo>
                                  <newCardInfo>
                                    <type>VI</type>
                                    <number>4532694461984309</number>
                                    <expDate>1114</expDate>
                                  </newCardInfo>
                                </accountUpdater>
                                <networkTransactionId>63225578415568556365452427825</networkTransactionId>
                              </authorizationResponse>
                              <merchantCategoryCode>7890</merchantCategoryCode>
                            </cnpOnlineResponse>
                                    """

        response = online.request(transaction, conf)
        self.assertEquals("000", response['authorizationResponse']['response'])
        self.assertEquals("7890", response['merchantCategoryCode'])

    @mock.patch.object(online, '_http_post')
    def test_echeck__redeposit_with_mcc(self, mock__http_post):
        transaction = fields.echeckRedeposit()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        echeck = fields.echeckType()
        echeck.accNum = '12345657890'
        echeck.routingNum = '123456789'
        echeck.checkNum = '123455'
        transaction.merchantCategoryCode = '7890'
        echeck.accType = 'Checking'
        transaction.echeck = echeck

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Peter'
        billtoaddress.lastName = 'Green'
        billtoaddress.companyName = 'Green Co'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4100000000000100'
        card.expDate = '1210'

        transaction.card = card

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='1' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
                        </cnpOnlineResponse>
                                """
        self.assertRaises(utils.VantivException, online.request, transaction, conf, 'dict')

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='0' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
                                  <authorizationResponse id='thisisid' reportGroup='Planets' customerId=''>
                                    <cnpTxnId>4544691351798650001</cnpTxnId>
                                    <orderId>56789</orderId>
                                    <response>000</response>
                                    <responseTime>2017-03-13T12:14:00</responseTime>
                                    <message>Approved</message>
                                    <authCode>07585</authCode>
                                    <accountUpdater>
                                      <originalCardInfo>
                                        <type>VI</type>
                                        <number>4100000000000100</number>
                                        <expDate>1210</expDate>
                                      </originalCardInfo>
                                      <newCardInfo>
                                        <type>VI</type>
                                        <number>4532694461984309</number>
                                        <expDate>1114</expDate>
                                      </newCardInfo>
                                    </accountUpdater>
                                    <networkTransactionId>63225578415568556365452427825</networkTransactionId>
                                  </authorizationResponse>
                                  <merchantCategoryCode>7890</merchantCategoryCode>
                                </cnpOnlineResponse>
                                        """

        response = online.request(transaction, conf)
        self.assertEquals("000", response['authorizationResponse']['response'])
        self.assertEquals("7890", response['merchantCategoryCode'])


    @mock.patch.object(online, '_http_post')
    def test_echeck__Sale_with_mcc(self, mock__http_post):
        transaction = fields.echeckRedeposit()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        echeck = fields.echeckType()
        echeck.accNum = '12345657890'
        echeck.routingNum = '123456789'
        echeck.checkNum = '123455'
        transaction.merchantCategoryCode = '78901'
        echeck.accType = 'Checking'
        transaction.echeck = echeck

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Peter'
        billtoaddress.lastName = 'Green'
        billtoaddress.companyName = 'Green Co'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4100000000000100'
        card.expDate = '1210'

        transaction.card = card

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='1' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
                        </cnpOnlineResponse>
                                """
        self.assertRaises(utils.VantivException, online.request, transaction, conf, 'dict')

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='0' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
                                  <authorizationResponse id='thisisid' reportGroup='Planets' customerId=''>
                                    <cnpTxnId>4544691351798650001</cnpTxnId>
                                    <orderId>56789</orderId>
                                    <response>000</response>
                                    <responseTime>2017-03-13T12:14:00</responseTime>
                                    <message>Approved</message>
                                    <authCode>07585</authCode>
                                    <accountUpdater>
                                      <originalCardInfo>
                                        <type>VI</type>
                                        <number>4100000000000100</number>
                                        <expDate>1210</expDate>
                                      </originalCardInfo>
                                      <newCardInfo>
                                        <type>VI</type>
                                        <number>4532694461984309</number>
                                        <expDate>1114</expDate>
                                      </newCardInfo>
                                    </accountUpdater>
                                    <networkTransactionId>63225578415568556365452427825</networkTransactionId>
                                  </authorizationResponse>
                                  <merchantCategoryCode>7890</merchantCategoryCode>
                                </cnpOnlineResponse>
                                        """

        response = online.request(transaction, conf)
        self.assertEquals("000", response['authorizationResponse']['response'])
        self.assertEquals("7890", response['merchantCategoryCode'])


    @mock.patch.object(online, '_http_post')
    def test_Sale_with_mcc(self, mock__http_post):
        transaction = fields.sale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'
        card = fields.cardType()
        card.type = 'VI'
        card.number = '4100000000000100'
        card.expDate = '1210'

        transaction.card = card

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='1' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
                        </cnpOnlineResponse>
                                """
        self.assertRaises(utils.VantivException, online.request, transaction, conf, 'dict')

        mock__http_post.return_value = """<cnpOnlineResponse version='11.0' response='0' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
                                  <authorizationResponse id='thisisid' reportGroup='Planets' customerId=''>
                                    <cnpTxnId>4544691351798650001</cnpTxnId>
                                    <orderId>56789</orderId>
                                    <response>000</response>
                                    <responseTime>2017-03-13T12:14:00</responseTime>
                                    <message>Approved</message>
                                    <authCode>07585</authCode>
                                    <accountUpdater>
                                      <originalCardInfo>
                                        <type>VI</type>
                                        <number>4100000000000100</number>
                                        <expDate>1210</expDate>
                                      </originalCardInfo>
                                      <newCardInfo>
                                        <type>VI</type>
                                        <number>4532694461984309</number>
                                        <expDate>1114</expDate>
                                      </newCardInfo>
                                    </accountUpdater>
                                    <networkTransactionId>63225578415568556365452427825</networkTransactionId>
                                  </authorizationResponse>
                                  <merchantCategoryCode>7890</merchantCategoryCode>
                                </cnpOnlineResponse>
                                        """

        response = online.request(transaction, conf)
        self.assertEquals("000", response['authorizationResponse']['response'])
        self.assertEquals("7890", response['merchantCategoryCode'])

    @mock.patch.object(online, '_http_post')
    def test_request_for_authIndicatorEnumIncremental(self, mock__http_post):
        authorization = fields.authorization()
        authorization.id = '1234'
        authorization.customerId = 'Cust0404'
        authorization.reportGroup = 'Default'
        authorization.cnpTxnId = '34659348401'
        authorization.amount = '106'
        authorization.authIndicator = 'Incremental'

        mock__http_post.return_value = """<cnpOnlineResponse version='12.30' response='1' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
          </cnpOnlineResponse>
              """
        self.assertRaises(utils.VantivException, online.request, authorization, conf, 'dict')

        mock__http_post.return_value ="""
        <cnpOnlineResponse xmlns="http://www.vantivcnp.com/schema" version="12.30" response="0" message="Valid Format">
            <authorizationResponse id="PPAuthInc1" reportGroup="LitleDirectClearing">
                <cnpTxnId>587273030852445843</cnpTxnId>
                <orderId />
                <response>000</response>
                <message>Approved</message>
                <responseTime>2023-03-24T12:17:29.664</responseTime>
                <location>sandbox</location>
            </authorizationResponse>
        </cnpOnlineResponse>
        """

        # return dict
        response = online.request(authorization, conf)
        self.assertEquals('0', response['@response'])
        self.assertEquals('587273030852445843', response['authorizationResponse']['cnpTxnId'])
        self.assertIsInstance(response, dict)

        # return xml string
        response = online.request(authorization, conf, 'xml')
        self.assertIsInstance(response, str)

        # return fields object.
        response = online.request(authorization, conf, 'object')
        self.assertEquals('0', response.response)


    @mock.patch.object(online, '_http_post')
    def test_request_for_orderChannelEnumMIT_sellerInfo_authIndicatorEstimated(self, mock__http_post):
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

        mock__http_post.return_value = """<cnpOnlineResponse version='12.30' response='1' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
               </cnpOnlineResponse>
                   """
        self.assertRaises(utils.VantivException, online.request, authorization, conf, 'dict')

        mock__http_post.return_value = """
            <cnpOnlineResponse xmlns="http://www.vantivcnp.com/schema" version="12.30" response="0" message="Valid Format">
                <authorizationResponse id="auth_GP_success_MC_MerEnabled" reportGroup="DirectWFITxn">
                    <cnpTxnId>328357670706189403</cnpTxnId>
                    <orderId>XGR-1840823423</orderId>
                    <response>000</response>
                    <message>Approved</message>
                    <responseTime>2023-03-24T12:34:09.484</responseTime>
                    <authCode>06613</authCode>
                    <location>sandbox</location>
                </authorizationResponse>
            </cnpOnlineResponse> """

        # return dict
        response = online.request(authorization, conf)
        self.assertEquals('0', response['@response'])
        self.assertEquals('328357670706189403', response['authorizationResponse']['cnpTxnId'])
        self.assertIsInstance(response, dict)

        # return xml string
        response = online.request(authorization, conf, 'xml')
        self.assertIsInstance(response, str)

        # return fields object.
        response = online.request(authorization, conf, 'object')
        self.assertEquals('0', response.response)

    @mock.patch.object(online, '_http_post')
    def test_simple_sale_with_orderChanneEnumMIT_sellerInfo_authIndicatorEstimated(self ,mock__http_post):
        transaction = fields.sale()
        transaction.id = '1'
        transaction.customerId = 'Cust0403'
        transaction.reportGroup = 'Default Report Group'
        transaction.orderId = '12344401'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
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
        transaction.seller_info = seller_info
        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card
        transaction.orderChannel = 'MIT'


        mock__http_post.return_value = """<cnpOnlineResponse version='12.30' response='1' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
                        </cnpOnlineResponse>
                                """
        self.assertRaises(utils.VantivException, online.request, transaction, conf, 'dict')

        mock__http_post.return_value = """<cnpOnlineResponse xmlns="http://www.vantivcnp.com/schema" version="12.30" response="0" message="Valid Format">
                    <saleResponse id="Cust0403" reportGroup="Default Report Group">
                        <cnpTxnId>972361514381087588</cnpTxnId>
                        <orderId>12344401</orderId>
                        <response>000</response>
                        <message>Approved</message>
                        <responseTime>2023-03-27T09:40:47.868</responseTime>
                        <authCode>84519</authCode>
                        <networkTransactionId>63225578415568556365452427825</networkTransactionId>
                        <location>sandbox</location>
                        <authMax>
                            <authMaxApplied>true</authMaxApplied>
                            <networkTokenApplied>true</networkTokenApplied>
                            <networkToken>1112000199940085</networkToken>
                            <authMaxResponseCode>000</authMaxResponseCode>
                            <authMaxResponseMessage>Approved</authMaxResponseMessage>
                        </authMax>
                    </saleResponse>
                </cnpOnlineResponse>"""


        response = online.request(transaction, conf)
        self.assertEquals('0', response['@response'])
        self.assertEquals('972361514381087588', response['saleResponse']['cnpTxnId'])
        self.assertIsInstance(response, dict)

        # return xml string
        response = online.request(transaction, conf, 'xml')
        self.assertIsInstance(response, str)

        # return fields object.
        response = online.request(transaction, conf, 'object')
        self.assertEquals('0', response.response)

    @mock.patch.object(online, '_http_post')
    def test_simple_sale_with_foreignRetailerIndicator(self ,mock__http_post):
        sale = fields.sale()
        sale.reportGroup = 'Default Report Group'
        sale.orderId = '8484'
        sale.amount = 3000
        sale.orderSource = 'ecommerce'
        sale.id = 'ThisIsID'
        sale.businessIndicator = 'fundTransfer'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        sale.card = card
        sale.foreignRetailerIndicator = 'F'

        mock__http_post.return_value = """<cnpOnlineResponse version='12.31' response='1' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
                        </cnpOnlineResponse>
                                """
        self.assertRaises(utils.VantivException, online.request, sale, conf, 'dict')

        mock__http_post.return_value = """<cnpOnlineResponse xmlns="http://www.vantivcnp.com/schema" version="12.31" response="0" message="Valid Format">
          <saleResponse id="ThisIsID" reportGroup="Default Report Group">
        <cnpTxnId>632423173824164537</cnpTxnId>
        <orderId>8484</orderId>
        <response>000</response>
        <message>Approved</message>
        <responseTime>2023-07-21T10:19:56.264</responseTime>
        <authCode>72777</authCode>
        <networkTransactionId>63225578415568556365452427825</networkTransactionId>
        <location>sandbox</location>
        </saleResponse>
                </cnpOnlineResponse>"""


        response = online.request(sale, conf)
        self.assertEquals('0', response['@response'])
        self.assertEquals('632423173824164537', response['saleResponse']['cnpTxnId'])
        self.assertIsInstance(response, dict)

        # return xml string
        response = online.request(sale, conf, 'xml')
        self.assertIsInstance(response, str)

        # return fields object.
        response = online.request(sale, conf, 'object')
        self.assertEquals('0', response.response)


    @mock.patch.object(online, '_http_post')
    def test_capture_with_foreignRetailerIndicator(self, mock__http_post):
        transaction = fields.capture()
        transaction.cnpTxnId = 123456000
        transaction.orderId = '54321'
        transaction.amount = 1109
        transaction.id = 'NewID'

        transport_data = fields.passengerTransportData()
        transport_data.passengerName = 'Simon M'
        transport_data.ticketNumber = 'xyz123456789'
        transport_data.issuingCarrier = 'AMTK'
        transport_data.carrierName = 'AMTK'
        transport_data.restrictedTicketIndicator = '11111'
        transport_data.numberOfAdults = '0'
        transport_data.numberOfChildren = '99'
        transport_data.customerCode = 'code12'
        transport_data.arrivalDate = '2022-01-22'
        transport_data.issueDate = '2021-02-03'
        transport_data.travelAgencyCode = '420104'
        transport_data.travelAgencyName = 'TravelAgency'
        transport_data.computerizedReservationSystem = 'DERD'
        transport_data.creditReasonIndicator = 'A'
        transport_data.ticketChangeIndicator = 'N'
        transport_data.ticketIssuerAddress = 'US'
        transport_data.exchangeTicketNumber = 'Ticket010'
        transport_data.exchangeAmount = '20210'
        transport_data.exchangeFeeAmount = '201010'

        card = fields.cardType()
        card.number = '4100100000000000'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card
        transaction.foreignRetailerIndicator = 'F'

        mock__http_post.return_value = """<cnpOnlineResponse version='12.31' response='1' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
          </cnpOnlineResponse>
                  """
        self.assertRaises(utils.VantivException, online.request, transaction, conf, 'dict')

        mock__http_post.return_value = """<cnpOnlineResponse version='12.31' response='0' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
        <captureResponse id="ThisIsID" reportGroup="Default Report Group">
            <cnpTxnId>428345917537978729</cnpTxnId>
            <response>000</response>
            <responseTime>2023-07-21T10:08:23.46</responseTime>
            <message>Approved</message>
            <location>sandbox</location>
        </captureResponse>
        </cnpOnlineResponse>"""

        response = online.request(transaction, conf)
        self.assertEquals("000", response['captureResponse']['response'])
        self.assertEquals('428345917537978729', response['captureResponse']['cnpTxnId'])

    @mock.patch.object(online, '_http_post')
    def test_force_capture_with_foreign_Retailer_Indicator(self, mock__http_post):
        transaction = fields.forceCapture()
        transaction.reportGroup = 'Default Report Group'
        transaction.orderId = '54321'
        transaction.amount = 1000
        transaction.orderSource = 'ecommerce'
        transaction.processingType = 'accountFunding'
        transaction.id = '1234'
        transaction.businessIndicator = 'consumerBillPayment'

        card = fields.cardType()
        card.number = '4100000000000001'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card
        transaction.foreignRetailerIndicator = 'F'

        mock__http_post.return_value = """<cnpOnlineResponse version='12.31' response='1' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
          </cnpOnlineResponse>
                  """
        self.assertRaises(utils.VantivException, online.request, transaction, conf, 'dict')

        mock__http_post.return_value = """<cnpOnlineResponse version='12.31' response='0' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
        <forceCaptureResponse id="1234" reportGroup="Default Report Group">
        <cnpTxnId>768152351901163723</cnpTxnId>
        <response>000</response>
        <message>Approved</message>
        <location>sandbox</location>
        </forceCaptureResponse>
        </cnpOnlineResponse>"""

        response = online.request(transaction, conf)
        self.assertEquals("000", response['forceCaptureResponse']['response'])
        self.assertEquals('768152351901163723', response['forceCaptureResponse']['cnpTxnId'])

    @mock.patch.object(online, '_http_post')
    def test_capture_given_auth_with_foreign_Retailer_Indicator(self, mock__http_post):
        transaction = fields.captureGivenAuth()
        transaction.orderId = '77373'
        transaction.amount = 2000
        transaction.orderSource = 'ecommerce'
        transaction.id = 'NewTxnID'
        transaction.businessIndicator = 'consumerBillPayment'

            # Create authInformation
        authInformation = fields.authInformation()
        authInformation.authDate = datetime.datetime.now().strftime("%Y-%m-%d")
        authInformation.authCode = '543216'
        authInformation.authAmount = 12345
        transaction.authInformation = authInformation

        # Create cardType object
        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        # The type of card is cardType
        transaction.card = card
        transaction.foreignRetailerIndicator = 'F'
        mock__http_post.return_value = """<cnpOnlineResponse version='12.31' response='1' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
          </cnpOnlineResponse>
                  """
        self.assertRaises(utils.VantivException, online.request, transaction, conf, 'dict')

        mock__http_post.return_value = """<cnpOnlineResponse version='12.31' response='0' message='Valid Format' xmlns='http://www.vantivcnp.com/schema'>
           <captureGivenAuthResponse id="NewTxnID" reportGroup="Default Report Group">
        <cnpTxnId>132956105425749971</cnpTxnId>
        <response>000</response>
        <message>Approved</message>
        <responseTime>2023-07-21T10:15:52.442</responseTime>
        <giftCardResponse>
            <txnTime>2023-07-21T10:15:52.442</txnTime>
            <refCode>097694</refCode>
            <systemTraceId>0</systemTraceId>
            <sequenceNumber>123456</sequenceNumber>
        </giftCardResponse>
        <location>sandbox</location>
        </captureGivenAuthResponse>
        </cnpOnlineResponse>"""

        response = online.request(transaction, conf)
        self.assertEquals("000", response['captureGivenAuthResponse']['response'])
        self.assertEquals('132956105425749971', response['captureGivenAuthResponse']['cnpTxnId'])




if __name__ == '__main__':
    unittest.main()
