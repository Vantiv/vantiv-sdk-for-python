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
import datetime
import os
import sys
import unittest

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

from vantivsdk import *

conf = utils.Configuration()


class TestCredit(unittest.TestCase):
    def test_simple_credit_with_card(self):
        transaction = fields.credit()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['creditResponse']['response'])
        self.assertEquals('sandbox', response['creditResponse']['location'])

    def test_simple_credit_with_paypal(self):
        transaction = fields.credit()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        paypal = fields.payPal()
        paypal.payerId = '1234'
        transaction.paypal = paypal

        response = online.request(transaction, conf)
        self.assertEquals('000', response['creditResponse']['response'])
        self.assertEquals('sandbox', response['creditResponse']['location'])

    def test_simple_credit_with_card_and_secondary_amount(self):
        transaction = fields.credit()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.secondaryAmount = 20
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['creditResponse']['response'])
        self.assertEquals('sandbox', response['creditResponse']['location'])

    def test_simple_credit_paypal_notes(self):
        transaction = fields.credit()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.payPalNotes = 'Hello'
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['creditResponse']['response'])
        self.assertEquals('sandbox', response['creditResponse']['location'])


    def test_processing_instruction_and_amex(self):
        transaction = fields.credit()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        processingInstructions = fields.processingInstructions()
        processingInstructions.bypassVelocityCheck = True
        transaction.processingInstructions = processingInstructions

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['creditResponse']['response'])
        self.assertEquals('sandbox', response['creditResponse']['location'])


    def test_simple_credit_with_litletxn_and_pin(self):
        transaction = fields.credit()
        transaction.cnpTxnId = '1234'
        transaction.amount = 106
        transaction.secondaryAmount = 20
        transaction.pin = '3333'
        transaction.id = 'ThisIsID'

        response = online.request(transaction, conf)
        self.assertEquals('000', response['creditResponse']['response'])
        self.assertEquals('sandbox', response['creditResponse']['location'])

    def test_simple_credit_with_pin_and_optional_order_id(self):
        transaction = fields.credit()
        transaction.cnpTxnId = '1234'
        transaction.amount = 106
        transaction.secondaryAmount = 20
        transaction.pin = '3333'
        transaction.id = 'ThisIsID'
        transaction.orderId = '123OptionalOrderID'

        response = online.request(transaction, conf)
        self.assertEquals('000', response['creditResponse']['response'])
        self.assertEquals('sandbox', response['creditResponse']['location'])

    def test_credit_with_business_indicator(self):
        transaction = fields.credit()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'
        transaction.businessIndicator = 'consumerBillPayment'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response['creditResponse']['response'])
        self.assertEquals('sandbox', response['creditResponse']['location'])

    def test_simple_auth_with_passenger_Transport_Data_tripLegData(self):
        transaction = fields.credit()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'
        transaction.businessIndicator = 'consumerBillPayment'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        transaction.card = card

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

        response = online.request(transaction, conf)
        self.assertEquals('000', response['creditResponse']['response'])
        self.assertEquals('sandbox', response['creditResponse']['location'])


    def test_simple_credit_with_additionaCOFData(self):
        transaction = fields.credit()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'
        transaction.businessIndicator = 'consumerBillPayment'

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

        response = online.request(transaction, conf)
        self.assertEquals('000', response['creditResponse']['response'])
        self.assertEquals('sandbox', response['creditResponse']['location'])

    def test_simple_credit_with_subscription_Shipment_Id(self):
        transaction = fields.credit()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'
        transaction.businessIndicator = 'consumerBillPayment'
        card = fields.cardType()
        card.number = '4457010000000009'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card
        lineItemDataList = list()
        lineItemData = fields.lineItemData()
        lineItemData.itemDescription = 'proc'
        lineItemData.itemCategory = 'Inv'
        lineItemData.shipmentId = 'prod5634'
        sub = fields.subscription()
        sub.subscriptionId = '567'
        sub.nextDeliveryDate = datetime.datetime.now().strftime("%Y-%m-%d")
        sub.periodUnit = 'MONTH'
        sub.numberOfPeriods = '110'
        sub.regularItemPrice = 776
        sub.currentPeriod = '988'
        lineItemData.subscription = sub
        lineItemDataList.append(lineItemData)
        enhancedData = fields.enhancedData()
        enhancedData.lineItemData = lineItemDataList
        transaction.enhancedData = enhancedData

        response = online.request(transaction, conf)
        self.assertEqual('000', response['creditResponse']['response'])
        self.assertEqual('sandbox', response['creditResponse']['location'])


if __name__ == '__main__':
    unittest.main()
