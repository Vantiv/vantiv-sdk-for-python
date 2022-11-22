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

conf = utils.Configuration()


class TestDepositTransactionReversal(unittest.TestCase):
    def test_simple_txn_reversal(self):
        transactions = fields.depositTransactionReversal()
        transactions.reportGroup = 'Planets'
        transactions.customerId = '987654321'
        transactions.cnpTxnId = '12345678000'
        transactions.amount = 106
        transactions.orderSource = 'ecommerce'
        transactions.id = 'thisisid'
        transactions.pin = '123456'

        response = online.request(transactions, conf)
        self.assertEquals('000', response['depositTransactionReversalResponse']['response'])
        self.assertEquals('sandbox', response['depositTransactionReversalResponse']['location'])
        self.assertEquals('12345678000', response['depositTransactionReversalResponse']['recyclingResponse']['creditCnpTxnId'])

    def test_simple_auth_with_passenger_Transport_Data_tripLegData(self):
        transactions = fields.depositTransactionReversal()
        transactions.reportGroup = 'Planets'
        transactions.customerId = '987654321'
        transactions.cnpTxnId = '12345678000'
        transactions.amount = 106
        transactions.orderSource = 'ecommerce'
        transactions.id = 'thisisid'
        transactions.pin = '123456'

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
        transactions.transport_data = transport_data

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
        transactions.tripleg_data = tripleg_data

        response = online.request(transactions, conf)
        self.assertEquals('000', response['depositTransactionReversalResponse']['response'])
        self.assertEquals('sandbox', response['depositTransactionReversalResponse']['location'])
        self.assertEquals('12345678000', response['depositTransactionReversalResponse']['recyclingResponse']['creditCnpTxnId'])


if __name__ == '__main__':
    unittest.main()
