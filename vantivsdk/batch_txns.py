# -*- coding: utf-8 -*-l
# Copyright (c) 2017 Vantiv eCommerce
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
from __future__ import unicode_literals

# Batch supported transactions dict
# Key: transaction name
# Value: array of batchRequest attributes according to transactions
supported_transaction_types = {
    # '': ['numExtCaptures', 'extCaptureAmount'],
    'accountUpdate': ['numAccountUpdates', ''],
    'activate': ['numActivates', 'activateAmount'],
    'authorization': ['numAuths', 'authAmount'],
    'authReversal': ['numAuthReversals', 'authReversalAmount'],
    'balanceInquiry': ['numBalanceInquirys', ''],
    'cancelSubscription': ['numCancelSubscriptions', ''],
    'capture': ['numCaptures', 'captureAmount'],
    'captureGivenAuth': ['numCaptureGivenAuths', 'captureGivenAuthAmount'],
    'createPlan': ['numCreatePlans', ''],
    'credit': ['numCredits', 'creditAmount'],
    'deactivate': ['numDeactivates', ''],
    'echeckCredit': ['numEcheckCredit', 'echeckCreditAmount'],
    'echeckPreNoteCredit': ['numEcheckPreNoteCredit', ''],
    'echeckPreNoteSale': ['numEcheckPreNoteSale', ''],
    'echeckRedeposit': ['numEcheckRedeposit', ''],
    'echeckSale': ['numEcheckSales', 'echeckSalesAmount'],
    'echeckVerification': ['numEcheckVerification', 'echeckVerificationAmount'],
    'forceCapture': ['numForceCaptures', 'forceCaptureAmount'],
    'fundingInstructionVoid': ['numFundingInstructionVoid', ''],
    'fastAccessFunding':['numFastAccessFunding',''],
    'giftCardAuthReversal': ['numGiftCardAuthReversals', 'giftCardAuthReversalOriginalAmount'],
    'giftCardCapture': ['numGiftCardCaptures', 'giftCardCaptureAmount'],
    'giftCardCredit': ['numGiftCardCredits', 'giftCardCreditAmount'],
    'load': ['numLoads', 'loadAmount'],
    'payFacCredit': ['numPayFacCredit', 'payFacCreditAmount'],
    'payFacDebit': ['numPayFacDebit', 'payFacDebitAmount'],
    'physicalCheckCredit': ['numPhysicalCheckCredit', 'physicalCheckCreditAmount'],
    'physicalCheckDebit': ['numPhysicalCheckDebit', 'physicalCheckDebitAmount'],
    'registerTokenRequest': ['numTokenRegistrations', ''],
    'reserveCredit': ['numReserveCredit', 'reserveCreditAmount'],
    'reserveDebit': ['numReserveDebit', 'reserveDebitAmount'],
    'sale': ['numSales', 'saleAmount'],
    'submerchantCredit': ['numSubmerchantCredit', 'submerchantCreditAmount'],
    'submerchantDebit': ['numSubmerchantDebit', 'submerchantDebitAmount'],
    'translateToLowValueTokenRequest': ['numTranslateToLowValueTokenRequests', ''],
    'unload': ['numUnloads', 'unloadAmount'],
    'updateCardValidationNumOnToken': ['numUpdateCardValidationNumOnTokens', ''],
    'updatePlan': ['numUpdatePlans', ''],
    'updateSubscription': ['numUpdateSubscriptions', ''],
    'vendorCredit': ['numVendorCredit', 'vendorCreditAmount'],
    'vendorDebit': ['numVendorDebit', 'vendorDebitAmount'],
}
