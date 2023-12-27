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
import datetime
conf = utils.Configuration()


class TestCapture(unittest.TestCase):
    
    def test_simple_capture(self):
        transaction = fields.capture()
        transaction.cnpTxnId = 123456000
        transaction.amount = 106
        transaction.id = 'ThisIsID'

        response = online.request(transaction, conf)
        self.assertEquals('000', response['captureResponse']['response'])
        self.assertEquals('sandbox', response['captureResponse']['location'])

    def test_simple_capture_with_optional_order_id(self):
        transaction = fields.capture()
        transaction.cnpTxnId = 123456000
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.id = 'ThisIsID'

        response = online.request(transaction, conf)
        self.assertEquals('000', response['captureResponse']['response'])
        self.assertEquals('sandbox', response['captureResponse']['location'])

    def test_simple_auth_with_passenger_Transport_Data_triplegData(self):
        transaction = fields.capture()
        transaction.cnpTxnId = 123456000
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.id = 'ThisIsID'

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

        card = fields.cardType()
        card.number = '4100100000000000'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['captureResponse']['response'])
        self.assertEquals('sandbox', response['captureResponse']['location'])

    def test_simple_capture_with_foreign_Retailer_Indicator(self):
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

        response = online.request(transaction, conf)
        self.assertEquals('000', response['captureResponse']['response'])
        self.assertEquals('sandbox', response['captureResponse']['location'])

    def test_simple_capture_with_subscription_Shipment_Id(self):
        transaction = fields.capture()
        transaction.cnpTxnId = 123456000
        transaction.orderId = '54321'
        transaction.amount = 1109
        transaction.id = 'NewID'
        card = fields.cardType()
        card.number = '4457010000000009'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card
        lineItemDataList = list()
        lineItemData = fields.lineItemData()
        lineItemData.itemDescription = 'des'
        lineItemData.itemCategory = 'Chock'
        lineItemData.itemCategory = 'Chock'
        lineItemData.itemSubCategory = 'pen'
        lineItemData.productId = '001'
        lineItemData.productName = 'prod'
        lineItemData.shipmentId = 'prod1234'
        sub = fields.subscription()
        sub.subscriptionId = '567'
        sub.nextDeliveryDate = datetime.datetime.now().strftime("%Y-%m-%d")
        sub.periodUnit = 'QUARTER'
        sub.numberOfPeriods = '111'
        sub.regularItemPrice = 976
        sub.currentPeriod = '996'
        lineItemData.subscription = sub
        lineItemDataList.append(lineItemData)
        enhancedData = fields.enhancedData()
        enhancedData.lineItemData = lineItemDataList
        transaction.enhancedData = enhancedData
        transaction.foreignRetailerIndicator = 'F'
        response = online.request(transaction, conf)
        self.assertEqual('000', response['captureResponse']['response'])
        self.assertEqual('sandbox', response['captureResponse']['location'])

if __name__ == '__main__':
    unittest.main()

