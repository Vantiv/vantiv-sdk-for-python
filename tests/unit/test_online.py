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

if __name__ == '__main__':
    unittest.main()
