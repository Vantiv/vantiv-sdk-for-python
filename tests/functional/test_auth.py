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

import pyxb

from vantivsdk import *
import datetime

conf = utils.Configuration()


class TestAuth(unittest.TestCase):

    def test_simple_auth_with_card(self):
        authorization = fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.id = 'thisisid'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        authorization.card = card

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

        authorization.customerInfo = customerInfo

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

        authorization.enhancedData = enhancedData

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_simple_auth_with_order_id_gt25(self):
        authorization = fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '123456789012345678901234567890'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.id = 'thisisid'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_simple_auth_with_card_dict(self):
        # Transactions presented by dict
        txn_dict = {
            'authorization': {
                'reportGroup': 'Planets',
                'orderId': '12344',
                'amount': '106',
                'orderSource': 'ecommerce',
                'id': 'thisisid',
                'card': {
                    'expDate': '1210',
                    'number': '4100000000000000',
                    'type': 'VI',
                }
            }
        }
        response = online.request(txn_dict, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_simple_auth_with_lodging_and_passangertransportdata(self):
        authorization = fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.id = 'thisisid'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        authorization.card = card

        lodging_info = fields.lodgingInfo()
        lodging_info.roomRate = 1001
        lodging_info.roomTax = 1
        lodging_info.bookingID = 'ID12345'
        lodging_info.passengerName = 'Post Malone'
        lodging_info.travelPackageIndicator = "AirlineReservation"
        lodging_info.smokingPreference = 'N'
        lodging_info.numberOfRooms = 13
        lodging_info.tollFreePhoneNumber = '1234567890'

        lodging_charge = fields.lodgingCharge()
        lodging_charge.name = "RESTAURANT"
        lodging_info.lodgingCharge = [lodging_charge]
        authorization.lodgingInfo = lodging_info

        property_Address = fields.propertyAddress()
        property_Address.name = 'propertyaddress1'
        property_Address.city = 'nyc'
        property_Address.region = 'abc'
        property_Address.country = 'US'
        authorization.lodgingInfo = lodging_info

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

        authorization.transport_data = transport_data

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])


    def test_simple_auth_with_android_pay(self):
        authorization = fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'androidpay'
        authorization.id = 'thisisid'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ0K',
                          response['authorizationResponse']['androidpayResponse']['cryptogram'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_simple_auth_with_paypal(self):
        authorization = fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.id = 'thisisid'

        paypal = fields.payPal()
        paypal.payerId = '1234'
        paypal.token = '1234'
        paypal.transactionId = '1234'
        authorization.paypal = paypal

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    # ***
    def test_simple_auth_with_applepay_and_secondary_amount(self):
        authorization = fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.secondaryAmount = 50
        authorization.orderSource = 'ecommerce'
        authorization.id = 'thisisid'

        applepayHeaderType = fields.applepayHeaderType()
        applepayHeaderType.applicationData = '454657413164'
        applepayHeaderType.ephemeralPublicKey = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        applepayHeaderType.publicKeyHash = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        applepayHeaderType.transactionId = '1234'
        applepay = fields.applepayType()
        applepay.header = applepayHeaderType
        applepay.data = 'user'
        applepay.signature = 'sign'
        applepay.version = '12345'
        authorization.applepay = applepay

        response = online.request(authorization, conf)
        # vvv
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('106', response['authorizationResponse']['applepayResponse']['transactionAmount'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_pos_without_capability_entrymod(self):
        authorization = fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'

        pos = fields.pos()
        pos.cardholderId = 'pin'
        authorization.pos = pos

        card = fields.cardType()
        card.number = u'4100000000000002'
        card.expDate = '1210'
        card.type = 'VI'
        card.pin = '2222'
        authorization.card = card

        self.assertRaises(utils.VantivException, online.request, authorization, conf)

    def test_account_update(self):
        authorization = fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.id = 'thisisid'

        card = fields.cardType()
        card.number = '4100100000000000'
        card.expDate = '1210'
        card.type = 'VI'
        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('4100100000000000',
                          response['authorizationResponse']['accountUpdater']['originalCardInfo']['number'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_track_data(self):
        authorization = fields.authorization()
        authorization.id = 'AX54321678'
        authorization.reportGroup = 'RG27'
        authorization.orderId = '12z58743y1'
        authorization.amount = 12522
        authorization.orderSource = 'retail'

        billToAddress = fields.contact()
        billToAddress.zip = '95032'
        authorization.billToAddress = billToAddress

        card = fields.cardType()
        card.track = '%B40000001^Doe/JohnP^06041...?;40001=0604101064200?'
        authorization.card = card

        pos = fields.pos()
        pos.cardholderId = 'signature'
        pos.capability = 'magstripe'
        pos.entryMode = 'completeread'
        authorization.pos = pos

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_list_of_tax_amount(self):
        authorization = fields.authorization()
        authorization.id = '12345'
        authorization.reportGroup = 'Default'
        authorization.orderId = '67890'
        authorization.amount = 10000
        authorization.orderSource = 'ecommerce'

        detailTaxList = list()
        detailTax = fields.detailTax()
        detailTax.taxAmount = 100
        detailTax2 = fields.detailTax()
        detailTax2.taxAmount = 200
        detailTaxList.append(detailTax)
        detailTaxList.append(detailTax2)

        enhancedData = fields.enhancedData()
        enhancedData.detailTax = detailTaxList

        authorization.enhancedData = enhancedData

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_simple_auth_with_card_skipRealtimeAU_null(self):
        authorization = fields.authorization()
        authorization.reportGroup = "Planets"
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.id = "id"

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4100000000000000'
        card.expDate = '1210'
        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_simple_auth_with_card_skipRealtimeAU_true(self):
        authorization = fields.authorization()
        authorization.reportGroup = "Planets"
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.id = "id"
        authorization.skipRealtimeAU = True

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4100000000000000'
        card.expDate = '1210'
        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_simple_auth_with_card_skipRealtimeAU_false(self):
        authorization = fields.authorization()
        authorization.reportGroup = "Planets"
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.id = "id"
        authorization.skipRealtimeAU = False

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4100000000000000'
        card.expDate = '1210'
        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('Approved', response['authorizationResponse']['message'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_auth_with_processing_type(self):
        authorization = fields.authorization()
        authorization.id = '12345'
        authorization.reportGroup = 'Default'
        authorization.orderId = '67890'
        authorization.amount = 10000
        authorization.orderSource = 'ecommerce'
        authorization.processingType = 'initialInstallment'
        authorization.originalNetworkTransactionId = '9876543210'
        authorization.originalTransactionAmount = 53698

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_auth_with_processing_type_COF(self):
        authorization = fields.authorization()
        authorization.id = '12345'
        authorization.reportGroup = 'Default'
        authorization.orderId = '67890'
        authorization.amount = 10000
        authorization.orderSource = 'ecommerce'
        authorization.processingType = 'initialCOF'
        authorization.originalNetworkTransactionId = '9876543210'
        authorization.originalTransactionAmount = 53698

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])

        authorization.processingType = 'merchantInitiatedCOF'
        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])

        authorization.processingType = 'cardholderInitiatedCOF'
        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])

        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_auth_with_wallet(self):
        authorization = fields.authorization()
        authorization.id = '12345'
        authorization.reportGroup = 'Default'
        authorization.orderId = '67890'
        authorization.amount = 10000
        authorization.orderSource = 'ecommerce'
        authorization.processingType = 'initialInstallment'
        authorization.originalNetworkTransactionId = '9876543210'
        authorization.originalTransactionAmount = 53698

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        authorization.card = card

        wallet = fields.wallet()
        wallet.walletSourceTypeId = '1'
        wallet.walletSourceType = 'VisaCheckout'
        authorization.wallet = wallet

        response = online.request(authorization, conf)
        # self.assertEquals('63225578415568556365452427825', response['authorizationResponse']['networkTransactionId'])

    def test_auth_with_wallet_and_card_suffix_response(self):
        authorization = fields.authorization()
        authorization.id = '12345'
        authorization.reportGroup = 'Default'
        authorization.orderId = '67890'
        authorization.amount = 10000
        authorization.orderSource = 'ecommerce'
        authorization.processingType = 'initialInstallment'
        authorization.originalNetworkTransactionId = '9876543210'
        authorization.originalTransactionAmount = 53698

        card = fields.cardType()
        card.number = '5400700000000000'
        card.expDate = '1215'
        card.type = 'MC'
        authorization.card = card

        wallet = fields.wallet()
        wallet.walletSourceTypeId = '1'
        wallet.walletSourceType = 'MasterPass'
        authorization.wallet = wallet

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertNotIn('networkTransactionId', response['authorizationResponse'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_simple_auth_business_indicator(self):
        authorization = fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.id = 'thisisid'
        authorization.businessIndicator = 'buyOnlinePickUpInStore'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_simple_auth_with_retaileraddress(self):
        authorization = fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.id = 'thisisid'
        authorization.businessIndicator = 'consumerBillPayment'
        authorization.crypto = False
        authorization.checkoutId = '123tyhgr34'
        authorization.orderChannel = 'PHONE'
        authorization.fraudCheckStatus = 'Not Approved'

        contact = fields.contact()
        contact.name = 'john & Mary Smith'
        contact.addressLine1 = '1st Main Street'
        contact.city = 'Burlington'
        contact.state = 'MA'
        contact.zip = '01867-4456'
        contact.country = 'USA'

        authorization.retailerAddress = contact

        additionalCOFData = fields.additionalCOFData()
        additionalCOFData.totalPaymentCount = '35'
        additionalCOFData.paymentType = 'Fixed Amount'
        additionalCOFData.uniqueId = '12345wereew233'
        additionalCOFData.frequencyOfMIT = 'BiWeekly'
        additionalCOFData.validationReference = 're3298rhriw4wrw'
        additionalCOFData.sequenceIndicator = '2'

        authorization.additionalCOFData = additionalCOFData

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_simple_auth_overridePolicy_fserrorcode_productEnrolled(self):
        authorization = fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.id = 'thisisid'
        authorization.businessIndicator = 'buyOnlinePickUpInStore'
        authorization.overridePolicy = 'fispolicy'
        authorization.fsErrorCode = 'Fiserrorcode'
        authorization.merchantAccountStatus = 'Active'
        authorization.productEnrolled = 'GUARPAY2'
        authorization.decisionPurpose = 'INFORMATION_ONLY'
        authorization.fraudSwitchIndicator = "PRE"

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_simple_auth_with_passenger_Transport_Data_triplegData(self):
        authorization = fields.authorization()
        authorization.id = '12345'
        authorization.reportGroup = 'Default'
        authorization.orderId = '67890'
        authorization.amount = 10000
        authorization.orderSource = 'ecommerce'

        transport_data = fields.passengerTransportData()
        transport_data.passengerName = 'Post Malone123'
        transport_data.ticketNumber = 'abc123456789'
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
        authorization.transport_data = transport_data

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
        authorization.tripleg_data = tripleg_data

        card = fields.cardType()
        card.number = '4100100000000000'
        card.expDate = '1210'
        card.type = 'VI'
        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_simple_auth_with_auth_max_Disabled(self):
        authorization = fields.authorization()
        authorization.id = '1'
        authorization.customerId = 'Cust0403'
        authorization.reportGroup = '001550'
        authorization.orderId = 'TC137654_1_DI_402'
        authorization.amount = 500
        authorization.orderSource = 'ecommerce'

        card = fields.cardType()
        card.number = '5500000050261001'
        card.expDate = '1199'
        card.type = 'MC'
        authorization.card = card

        response = online.request(authorization, conf)

        self.assertEquals('false',response['authorizationResponse']['authMax']['authMaxApplied'])
        self.assertEquals('001', response['authorizationResponse']['response'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_simple_auth_with_auth_max_enabled(self):
        authorization = fields.authorization()
        authorization.id = '1'
        authorization.customerId = 'Cust0403'
        authorization.reportGroup = 'русский中文'
        authorization.orderId = '12344401'
        authorization.amount = 500
        authorization.orderSource = 'ecommerce'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        authorization.card = card

        response = online.request(authorization, conf)

        self.assertEquals('true', response['authorizationResponse']['authMax']['authMaxApplied'])
        self.assertEquals('000', response['authorizationResponse']['response'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])

    def test_simple_auth_with_auth_max_enabled_networkToken(self):
        authorization = fields.authorization()
        authorization.id = '1'
        authorization.customerId = 'Cust0403'
        authorization.reportGroup = 'русский中文'
        authorization.orderId = '12344401'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        authorization.card = card

        response = online.request(authorization, conf)

        self.assertEquals('true', response['authorizationResponse']['authMax']['networkTokenApplied'])
        self.assertEquals('1112000199940085', response['authorizationResponse']['authMax']['networkToken'])
        self.assertEquals('Approved', response['authorizationResponse']['authMax']['authMaxResponseMessage'])
        self.assertEquals('000', response['authorizationResponse']['authMax']['authMaxResponseCode'])
        self.assertEquals('true', response['authorizationResponse']['authMax']['authMaxApplied'])
        self.assertEquals('sandbox', response['authorizationResponse']['location'])


if __name__ == '__main__':
    unittest.main()
