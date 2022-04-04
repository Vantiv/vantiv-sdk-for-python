Transactions
============

accountUpdate
-------------
    .. py:class:: vantivsdk.fields.accountUpdate

        :var cardOrToken: instance of :py:class:`vantivsdk.fields.card`, :py:class:`vantivsdk.fields.token`, 
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var reportGroup: String or Number

activate
--------
    .. py:class:: vantivsdk.fields.activate

        :var amount: String or Number
        :var card: instance of :py:class:`vantivsdk.fields.giftCardCardType`
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number
        :var virtualGiftCard: instance of :py:class:`vantivsdk.fields.virtualGiftCardType`

activateReversal
----------------
    .. py:class:: vantivsdk.fields.activateReversal

        :var card: instance of :py:class:`vantivsdk.fields.giftCardCardType`
        :var cnpTxnId: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var originalAmount: String or Number
        :var originalRefCode: String or Number
        :var originalSequenceNumber: String or Number
        :var originalSystemTraceId: String or Number
        :var originalTxnTime: String or Number
        :var reportGroup: String or Number
        :var virtualGiftCardBin: String or Number

authReversal
------------
    .. py:class:: vantivsdk.fields.authReversal

        :var actionReason: String or Number
        :var amount: String or Number
        :var cnpTxnId: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var payPalNotes: String or Number
        :var reportGroup: String or Number
        :var surchargeAmount: String or Number

authorization
-------------
    .. py:class:: vantivsdk.fields.authorization

        :var additionalCOFData: instance of :py:class:`vantivsdk.fields.additionalCOFData`
        :var advancedFraudChecks: instance of :py:class:`vantivsdk.fields.advancedFraudChecksType`
        :var allowPartialAuth: String or Number
        :var amount: String or Number
        :var applepay: instance of :py:class:`vantivsdk.fields.applepayType`
        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var businessIndicator: String or Number
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var cardholderAuthentication: instance of :py:class:`vantivsdk.fields.fraudCheckType`
        :var cnpTxnId: String or Number
        :var crypto: String or Number
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var customerInfo: instance of :py:class:`vantivsdk.fields.customerInfo`
        :var debtRepayment: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var filtering: instance of :py:class:`vantivsdk.fields.filteringType`
        :var fraudCheckStatus: String or Number
        :var fraudFilterOverride: String or Number
        :var healthcareIIAS: instance of :py:class:`vantivsdk.fields.healthcareIIAS`
        :var id: String or Number
        :var lodgingInfo: instance of :py:class:`vantivsdk.fields.lodgingInfo`
        :var merchantCategoryCode: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
        :var mpos: instance of :py:class:`vantivsdk.fields.mposType`
        :var orderChannel: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var originalNetworkTransactionId: String or Number
        :var originalTransactionAmount: String or Number
        :var paypage: instance of :py:class:`vantivsdk.fields.cardPaypageType`
        :var paypal: instance of :py:class:`vantivsdk.fields.payPal`
        :var pinlessDebitRequest: instance of :py:class:`vantivsdk.fields.pinlessDebitRequestType`
        :var pos: instance of :py:class:`vantivsdk.fields.pos`
        :var processingInstructions: instance of :py:class:`vantivsdk.fields.processingInstructions`
        :var processingType: String or Number
        :var recurringRequest: instance of :py:class:`vantivsdk.fields.recurringRequestType`
        :var recyclingRequest: instance of :py:class:`vantivsdk.fields.recyclingRequestType`
        :var reportGroup: String or Number
        :var retailerAddress: instance of :py:class:`vantivsdk.fields.retailerAddress`
        :var secondaryAmount: String or Number
        :var shipToAddress: instance of :py:class:`vantivsdk.fields.shipToAddress`
        :var skipRealtimeAU: String or Number
        :var surchargeAmount: String or Number
        :var taxType: String or Number
        :var token: instance of :py:class:`vantivsdk.fields.cardTokenType`
        :var wallet: instance of :py:class:`vantivsdk.fields.wallet`

balanceInquiry
--------------
    .. py:class:: vantivsdk.fields.balanceInquiry

        :var card: instance of :py:class:`vantivsdk.fields.giftCardCardType`
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

cancelSubscription
------------------
    .. py:class:: vantivsdk.fields.cancelSubscription

        :var subscriptionId: String or Number

capture
-------
    .. py:class:: vantivsdk.fields.capture

        :var amount: String or Number
        :var cnpTxnId: String or Number
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var id: String or Number
        :var lodgingInfo: instance of :py:class:`vantivsdk.fields.lodgingInfo`
        :var orderId: String or Number
        :var partial: String or Number
        :var payPalNotes: String or Number
        :var payPalOrderComplete: String or Number
        :var pin: String or Number
        :var processingInstructions: instance of :py:class:`vantivsdk.fields.processingInstructions`
        :var reportGroup: String or Number
        :var surchargeAmount: String or Number

captureGivenAuth
----------------
    .. py:class:: vantivsdk.fields.captureGivenAuth

        :var additionalCOFData: instance of :py:class:`vantivsdk.fields.additionalCOFData`
        :var amount: String or Number
        :var authInformation: instance of :py:class:`vantivsdk.fields.authInformation`
        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var businessIndicator: String or Number
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var crypto: String or Number
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var debtRepayment: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var id: String or Number
        :var lodgingInfo: instance of :py:class:`vantivsdk.fields.lodgingInfo`
        :var merchantCategoryCode: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
        :var mpos: instance of :py:class:`vantivsdk.fields.mposType`
        :var orderId: String or Number
        :var orderSource: String or Number
        :var originalNetworkTransactionId: String or Number
        :var originalTransactionAmount: String or Number
        :var paypage: instance of :py:class:`vantivsdk.fields.cardPaypageType`
        :var pos: instance of :py:class:`vantivsdk.fields.pos`
        :var processingInstructions: instance of :py:class:`vantivsdk.fields.processingInstructions`
        :var processingType: String or Number
        :var reportGroup: String or Number
        :var retailerAddress: instance of :py:class:`vantivsdk.fields.retailerAddress`
        :var secondaryAmount: String or Number
        :var shipToAddress: instance of :py:class:`vantivsdk.fields.shipToAddress`
        :var surchargeAmount: String or Number
        :var taxType: String or Number
        :var token: instance of :py:class:`vantivsdk.fields.cardTokenType`

createPlan
----------
    .. py:class:: vantivsdk.fields.createPlan

        :var active: String or Number
        :var amount: String or Number
        :var description: String or Number
        :var intervalType: String or Number
        :var name: String or Number
        :var numberOfPayments: String or Number
        :var planCode: String or Number
        :var trialIntervalType: String or Number
        :var trialNumberOfIntervals: String or Number

credit
------
    .. py:class:: vantivsdk.fields.credit

        :var actionReason: String or Number
        :var amount: String or Number
        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var businessIndicator: String or Number
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var cnpTxnId: String or Number
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var id: String or Number
        :var lodgingInfo: instance of :py:class:`vantivsdk.fields.lodgingInfo`
        :var merchantCategoryCode: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
        :var mpos: instance of :py:class:`vantivsdk.fields.mposType`
        :var orderId: String or Number
        :var orderSource: String or Number
        :var payPalNotes: String or Number
        :var paypage: instance of :py:class:`vantivsdk.fields.cardPaypageType`
        :var paypal: instance of :py:class:`vantivsdk.fields.payPal`
        :var pin: String or Number
        :var pos: instance of :py:class:`vantivsdk.fields.pos`
        :var processingInstructions: instance of :py:class:`vantivsdk.fields.processingInstructions`
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number
        :var surchargeAmount: String or Number
        :var taxType: String or Number
        :var token: instance of :py:class:`vantivsdk.fields.cardTokenType`

customerCredit
--------------
    .. py:class:: vantivsdk.fields.customerCredit

        :var accountInfo: instance of :py:class:`vantivsdk.fields.echeckTypeCtx`
        :var amount: String or Number
        :var customIdentifier: String or Number
        :var customerId: String or Number
        :var customerName: String or Number
        :var fundingCustomerId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

customerDebit
-------------
    .. py:class:: vantivsdk.fields.customerDebit

        :var accountInfo: instance of :py:class:`vantivsdk.fields.echeckTypeCtx`
        :var amount: String or Number
        :var customIdentifier: String or Number
        :var customerId: String or Number
        :var customerName: String or Number
        :var fundingCustomerId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

deactivate
----------
    .. py:class:: vantivsdk.fields.deactivate

        :var card: instance of :py:class:`vantivsdk.fields.giftCardCardType`
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

deactivateReversal
------------------
    .. py:class:: vantivsdk.fields.deactivateReversal

        :var card: instance of :py:class:`vantivsdk.fields.giftCardCardType`
        :var cnpTxnId: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var originalRefCode: String or Number
        :var originalSequenceNumber: String or Number
        :var originalSystemTraceId: String or Number
        :var originalTxnTime: String or Number
        :var reportGroup: String or Number

depositReversal
---------------
    .. py:class:: vantivsdk.fields.depositReversal

        :var card: instance of :py:class:`vantivsdk.fields.giftCardCardType`
        :var cnpTxnId: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var originalAmount: String or Number
        :var originalRefCode: String or Number
        :var originalSequenceNumber: String or Number
        :var originalSystemTraceId: String or Number
        :var originalTxnTime: String or Number
        :var reportGroup: String or Number

depositTransactionReversal
--------------------------
    .. py:class:: vantivsdk.fields.depositTransactionReversal

        :var amount: String or Number
        :var cnpTxnId: String or Number
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var id: String or Number
        :var lodgingInfo: instance of :py:class:`vantivsdk.fields.lodgingInfo`
        :var pin: String or Number
        :var processingInstructions: instance of :py:class:`vantivsdk.fields.processingInstructions`
        :var reportGroup: String or Number
        :var surchargeAmount: String or Number

echeckCredit
------------
    .. py:class:: vantivsdk.fields.echeckCredit

        :var amount: String or Number
        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var cnpTxnId: String or Number
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customIdentifier: String or Number
        :var customerId: String or Number
        :var echeck: instance of :py:class:`vantivsdk.fields.echeckType`
        :var echeckToken: instance of :py:class:`vantivsdk.fields.echeckTokenType`
        :var id: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number

echeckPreNoteCredit
-------------------
    .. py:class:: vantivsdk.fields.echeckPreNoteCredit

        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var customerId: String or Number
        :var echeck: instance of :py:class:`vantivsdk.fields.echeckType`
        :var id: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

echeckPreNoteSale
-----------------
    .. py:class:: vantivsdk.fields.echeckPreNoteSale

        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var customerId: String or Number
        :var echeck: instance of :py:class:`vantivsdk.fields.echeckType`
        :var id: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

echeckRedeposit
---------------
    .. py:class:: vantivsdk.fields.echeckRedeposit

        :var cnpTxnId: String or Number
        :var customIdentifier: String or Number
        :var customerId: String or Number
        :var echeck: instance of :py:class:`vantivsdk.fields.echeckType`
        :var echeckToken: instance of :py:class:`vantivsdk.fields.echeckTokenType`
        :var id: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
        :var reportGroup: String or Number

echeckSale
----------
    .. py:class:: vantivsdk.fields.echeckSale

        :var amount: String or Number
        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var cnpTxnId: String or Number
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customIdentifier: String or Number
        :var customerId: String or Number
        :var echeck: instance of :py:class:`vantivsdk.fields.echeckType`
        :var echeckToken: instance of :py:class:`vantivsdk.fields.echeckTokenType`
        :var id: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number
        :var shipToAddress: instance of :py:class:`vantivsdk.fields.shipToAddress`
        :var verify: String or Number

echeckVerification
------------------
    .. py:class:: vantivsdk.fields.echeckVerification

        :var amount: String or Number
        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var customerId: String or Number
        :var echeck: instance of :py:class:`vantivsdk.fields.echeckType`
        :var echeckToken: instance of :py:class:`vantivsdk.fields.echeckTokenType`
        :var id: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

echeckVoid
----------
    .. py:class:: vantivsdk.fields.echeckVoid

        :var cnpTxnId: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

fastAccessFunding
-----------------
    .. py:class:: vantivsdk.fields.fastAccessFunding

        :var amount: String or Number
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var cardholderAddress: instance of :py:class:`vantivsdk.fields.address`
        :var customerId: String or Number
        :var customerName: String or Number
        :var disbursementType: String or Number
        :var fundingCustomerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var paypage: instance of :py:class:`vantivsdk.fields.cardPaypageType`
        :var reportGroup: String or Number
        :var submerchantName: String or Number
        :var token: instance of :py:class:`vantivsdk.fields.cardTokenType`

forceCapture
------------
    .. py:class:: vantivsdk.fields.forceCapture

        :var amount: String or Number
        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var businessIndicator: String or Number
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var debtRepayment: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var id: String or Number
        :var lodgingInfo: instance of :py:class:`vantivsdk.fields.lodgingInfo`
        :var merchantCategoryCode: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
        :var mpos: instance of :py:class:`vantivsdk.fields.mposType`
        :var orderId: String or Number
        :var orderSource: String or Number
        :var paypage: instance of :py:class:`vantivsdk.fields.cardPaypageType`
        :var pos: instance of :py:class:`vantivsdk.fields.pos`
        :var processingInstructions: instance of :py:class:`vantivsdk.fields.processingInstructions`
        :var processingType: String or Number
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number
        :var surchargeAmount: String or Number
        :var taxType: String or Number
        :var token: instance of :py:class:`vantivsdk.fields.cardTokenType`

fraudCheck
----------
    .. py:class:: vantivsdk.fields.fraudCheck

        :var accountLogin: String or Number
        :var accountPasshash: String or Number
        :var advancedFraudChecks: instance of :py:class:`vantivsdk.fields.advancedFraudChecksType`
        :var amount: String or Number
        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var customerId: String or Number
        :var eventType: String or Number
        :var id: String or Number
        :var reportGroup: String or Number
        :var shipToAddress: instance of :py:class:`vantivsdk.fields.shipToAddress`

fundingInstructionVoid
----------------------
    .. py:class:: vantivsdk.fields.fundingInstructionVoid

        :var cnpTxnId: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

giftCardAuthReversal
--------------------
    .. py:class:: vantivsdk.fields.giftCardAuthReversal

        :var card: instance of :py:class:`vantivsdk.fields.giftCardCardType`
        :var cnpTxnId: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var originalAmount: String or Number
        :var originalRefCode: String or Number
        :var originalSequenceNumber: String or Number
        :var originalSystemTraceId: String or Number
        :var originalTxnTime: String or Number
        :var reportGroup: String or Number

giftCardCapture
---------------
    .. py:class:: vantivsdk.fields.giftCardCapture

        :var captureAmount: String or Number
        :var card: instance of :py:class:`vantivsdk.fields.giftCardCardType`
        :var cnpTxnId: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var originalAmount: String or Number
        :var originalRefCode: String or Number
        :var originalTxnTime: String or Number
        :var partial: String or Number
        :var reportGroup: String or Number

giftCardCredit
--------------
    .. py:class:: vantivsdk.fields.giftCardCredit

        :var card: instance of :py:class:`vantivsdk.fields.giftCardCardType`
        :var cnpTxnId: String or Number
        :var creditAmount: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

load
----
    .. py:class:: vantivsdk.fields.load

        :var amount: String or Number
        :var card: instance of :py:class:`vantivsdk.fields.giftCardCardType`
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

loadReversal
------------
    .. py:class:: vantivsdk.fields.loadReversal

        :var card: instance of :py:class:`vantivsdk.fields.giftCardCardType`
        :var cnpTxnId: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var originalAmount: String or Number
        :var originalRefCode: String or Number
        :var originalSequenceNumber: String or Number
        :var originalSystemTraceId: String or Number
        :var originalTxnTime: String or Number
        :var reportGroup: String or Number

payFacCredit
------------
    .. py:class:: vantivsdk.fields.payFacCredit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

payFacDebit
-----------
    .. py:class:: vantivsdk.fields.payFacDebit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

payoutOrgCredit
---------------
    .. py:class:: vantivsdk.fields.payoutOrgCredit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingCustomerId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

payoutOrgDebit
--------------
    .. py:class:: vantivsdk.fields.payoutOrgDebit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingCustomerId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

physicalCheckCredit
-------------------
    .. py:class:: vantivsdk.fields.physicalCheckCredit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingCustomerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

physicalCheckDebit
------------------
    .. py:class:: vantivsdk.fields.physicalCheckDebit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingCustomerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

queryTransaction
----------------
    .. py:class:: vantivsdk.fields.queryTransaction

        :var customerId: String or Number
        :var id: String or Number
        :var origActionType: String or Number
        :var origCnpTxnId: String or Number
        :var origId: String or Number
        :var reportGroup: String or Number
        :var showStatusOnly: String or Number

refundReversal
--------------
    .. py:class:: vantivsdk.fields.refundReversal

        :var card: instance of :py:class:`vantivsdk.fields.giftCardCardType`
        :var cnpTxnId: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var originalAmount: String or Number
        :var originalRefCode: String or Number
        :var originalSequenceNumber: String or Number
        :var originalSystemTraceId: String or Number
        :var originalTxnTime: String or Number
        :var reportGroup: String or Number

refundTransactionReversal
-------------------------
    .. py:class:: vantivsdk.fields.refundTransactionReversal

        :var amount: String or Number
        :var cnpTxnId: String or Number
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var id: String or Number
        :var lodgingInfo: instance of :py:class:`vantivsdk.fields.lodgingInfo`
        :var pin: String or Number
        :var processingInstructions: instance of :py:class:`vantivsdk.fields.processingInstructions`
        :var reportGroup: String or Number
        :var surchargeAmount: String or Number

registerTokenRequest
--------------------
    .. py:class:: vantivsdk.fields.registerTokenRequest

        :var accountNumber: String or Number
        :var applepay: instance of :py:class:`vantivsdk.fields.applepayType`
        :var cardValidationNum: String or Number
        :var customerId: String or Number
        :var echeckForToken: instance of :py:class:`vantivsdk.fields.echeckForTokenType`
        :var encryptedAccountNumber: String or Number
        :var encryptedCardValidationNum: String or Number
        :var encryptionKeyId: String or Number
        :var id: String or Number
        :var mpos: instance of :py:class:`vantivsdk.fields.mposType`
        :var orderId: String or Number
        :var paypageRegistrationId: String or Number
        :var reportGroup: String or Number

reserveCredit
-------------
    .. py:class:: vantivsdk.fields.reserveCredit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingCustomerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

reserveDebit
------------
    .. py:class:: vantivsdk.fields.reserveDebit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingCustomerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

sale
----
    .. py:class:: vantivsdk.fields.sale

        :var additionalCOFData: instance of :py:class:`vantivsdk.fields.additionalCOFData`
        :var advancedFraudChecks: instance of :py:class:`vantivsdk.fields.advancedFraudChecksType`
        :var allowPartialAuth: String or Number
        :var amount: String or Number
        :var applepay: instance of :py:class:`vantivsdk.fields.applepayType`
        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var businessIndicator: String or Number
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var cardholderAuthentication: instance of :py:class:`vantivsdk.fields.fraudCheckType`
        :var cnpInternalRecurringRequest: instance of :py:class:`vantivsdk.fields.cnpInternalRecurringRequestType`
        :var cnpTxnId: String or Number
        :var crypto: String or Number
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var customerInfo: instance of :py:class:`vantivsdk.fields.customerInfo`
        :var debtRepayment: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var filtering: instance of :py:class:`vantivsdk.fields.filteringType`
        :var fraudCheck: instance of :py:class:`vantivsdk.fields.fraudCheckType`
        :var fraudCheckStatus: String or Number
        :var fraudFilterOverride: String or Number
        :var giropay: instance of :py:class:`vantivsdk.fields.giropayType`
        :var healthcareIIAS: instance of :py:class:`vantivsdk.fields.healthcareIIAS`
        :var id: String or Number
        :var ideal: instance of :py:class:`vantivsdk.fields.idealType`
        :var lodgingInfo: instance of :py:class:`vantivsdk.fields.lodgingInfo`
        :var merchantCategoryCode: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
        :var mpos: instance of :py:class:`vantivsdk.fields.mposType`
        :var orderChannel: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var originalNetworkTransactionId: String or Number
        :var originalTransactionAmount: String or Number
        :var payPalNotes: String or Number
        :var payPalOrderComplete: String or Number
        :var paypage: instance of :py:class:`vantivsdk.fields.cardPaypageType`
        :var paypal: instance of :py:class:`vantivsdk.fields.payPal`
        :var pinlessDebitRequest: instance of :py:class:`vantivsdk.fields.pinlessDebitRequestType`
        :var pos: instance of :py:class:`vantivsdk.fields.pos`
        :var processingInstructions: instance of :py:class:`vantivsdk.fields.processingInstructions`
        :var processingType: String or Number
        :var recurringRequest: instance of :py:class:`vantivsdk.fields.recurringRequestType`
        :var recyclingRequest: instance of :py:class:`vantivsdk.fields.recyclingRequestType`
        :var reportGroup: String or Number
        :var retailerAddress: instance of :py:class:`vantivsdk.fields.retailerAddress`
        :var secondaryAmount: String or Number
        :var sepaDirectDebit: instance of :py:class:`vantivsdk.fields.sepaDirectDebitType`
        :var shipToAddress: instance of :py:class:`vantivsdk.fields.shipToAddress`
        :var skipRealtimeAU: String or Number
        :var sofort: instance of :py:class:`vantivsdk.fields.sofortType`
        :var surchargeAmount: String or Number
        :var taxType: String or Number
        :var token: instance of :py:class:`vantivsdk.fields.cardTokenType`
        :var wallet: instance of :py:class:`vantivsdk.fields.wallet`

serviceStatusRequest
--------------------
    .. py:class:: vantivsdk.fields.serviceStatusRequest

        :var customerId: String or Number
        :var id: String or Number
        :var pathId: String or Number
        :var reportGroup: String or Number
        :var serviceId: String or Number

submerchantCredit
-----------------
    .. py:class:: vantivsdk.fields.submerchantCredit

        :var accountInfo: instance of :py:class:`vantivsdk.fields.echeckTypeCtx`
        :var amount: String or Number
        :var customIdentifier: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number
        :var submerchantName: String or Number

submerchantDebit
----------------
    .. py:class:: vantivsdk.fields.submerchantDebit

        :var accountInfo: instance of :py:class:`vantivsdk.fields.echeckTypeCtx`
        :var amount: String or Number
        :var customIdentifier: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number
        :var submerchantName: String or Number

translateToLowValueTokenRequest
-------------------------------
    .. py:class:: vantivsdk.fields.translateToLowValueTokenRequest

        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var reportGroup: String or Number
        :var token: String or Number

unload
------
    .. py:class:: vantivsdk.fields.unload

        :var amount: String or Number
        :var card: instance of :py:class:`vantivsdk.fields.giftCardCardType`
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

unloadReversal
--------------
    .. py:class:: vantivsdk.fields.unloadReversal

        :var card: instance of :py:class:`vantivsdk.fields.giftCardCardType`
        :var cnpTxnId: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var originalAmount: String or Number
        :var originalRefCode: String or Number
        :var originalSequenceNumber: String or Number
        :var originalSystemTraceId: String or Number
        :var originalTxnTime: String or Number
        :var reportGroup: String or Number

updateCardValidationNumOnToken
------------------------------
    .. py:class:: vantivsdk.fields.updateCardValidationNumOnToken

        :var cardValidationNum: String or Number
        :var cnpToken: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var reportGroup: String or Number

updatePlan
----------
    .. py:class:: vantivsdk.fields.updatePlan

        :var active: String or Number
        :var planCode: String or Number

updateSubscription
------------------
    .. py:class:: vantivsdk.fields.updateSubscription

        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var billingDate: String or Number
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var createAddOn: instance of :py:class:`vantivsdk.fields.createAddOnType`
        :var createDiscount: instance of :py:class:`vantivsdk.fields.createDiscountType`
        :var deleteAddOn: instance of :py:class:`vantivsdk.fields.deleteAddOnType`
        :var deleteDiscount: instance of :py:class:`vantivsdk.fields.deleteDiscountType`
        :var paypage: instance of :py:class:`vantivsdk.fields.cardPaypageType`
        :var planCode: String or Number
        :var subscriptionId: String or Number
        :var token: instance of :py:class:`vantivsdk.fields.cardTokenType`
        :var updateAddOn: instance of :py:class:`vantivsdk.fields.updateAddOnType`
        :var updateDiscount: instance of :py:class:`vantivsdk.fields.updateDiscountType`

vendorCredit
------------
    .. py:class:: vantivsdk.fields.vendorCredit

        :var accountInfo: instance of :py:class:`vantivsdk.fields.echeckTypeCtx`
        :var amount: String or Number
        :var customerId: String or Number
        :var fundingCustomerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number
        :var vendorAddress: instance of :py:class:`vantivsdk.fields.address`
        :var vendorName: String or Number

vendorDebit
-----------
    .. py:class:: vantivsdk.fields.vendorDebit

        :var accountInfo: instance of :py:class:`vantivsdk.fields.echeckTypeCtx`
        :var amount: String or Number
        :var customerId: String or Number
        :var fundingCustomerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number
        :var vendorAddress: instance of :py:class:`vantivsdk.fields.address`
        :var vendorName: String or Number

void
----
    .. py:class:: vantivsdk.fields.void

        :var cnpTxnId: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var processingInstructions: instance of :py:class:`vantivsdk.fields.processingInstructions`
        :var reportGroup: String or Number

