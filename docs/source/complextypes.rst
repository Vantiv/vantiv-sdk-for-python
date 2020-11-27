Complex Types
=============

advancedFraudChecksType
-----------------------
    .. py:class:: vantivsdk.fields.advancedFraudChecksType

        :var Meta: String or Number
        :var customAttribute1: String or Number
        :var customAttribute2: String or Number
        :var customAttribute3: String or Number
        :var customAttribute4: String or Number
        :var customAttribute5: String or Number
        :var threatMetrixSessionId: String or Number
        :var webSessionId: String or Number

advancedFraudResultsType
------------------------
    .. py:class:: vantivsdk.fields.advancedFraudResultsType

        :var Meta: String or Number
        :var deviceReputationScore: String or Number
        :var deviceReviewStatus: String or Number
        :var triggeredRule: String or Number

applepayHeaderType
------------------
    .. py:class:: vantivsdk.fields.applepayHeaderType

        :var Meta: String or Number
        :var applicationData: String or Number
        :var ephemeralPublicKey: String or Number
        :var publicKeyHash: String or Number
        :var transactionId: String or Number

applepayType
------------
    .. py:class:: vantivsdk.fields.applepayType

        :var Meta: String or Number
        :var data: String or Number
        :var header: instance of :py:class:`vantivsdk.fields.applepayHeaderType`
        :var signature: String or Number
        :var version: String or Number

authInformation
---------------
    .. py:class:: vantivsdk.fields.authInformation

        :var Meta: String or Number
        :var authAmount: String or Number
        :var authCode: String or Number
        :var authDate: String or Number
        :var fraudResult: instance of :py:class:`vantivsdk.fields.fraudResult`

billToAddress
-------------
    .. py:class:: vantivsdk.fields.billToAddress

        :var Meta: String or Number
        :var addressLine1: String or Number
        :var addressLine2: String or Number
        :var addressLine3: String or Number
        :var city: String or Number
        :var companyName: String or Number
        :var country: String or Number
        :var email: String or Number
        :var firstName: String or Number
        :var lastName: String or Number
        :var middleInitial: String or Number
        :var name: String or Number
        :var phone: String or Number
        :var state: String or Number
        :var zip: String or Number

card
----
    .. py:class:: vantivsdk.fields.card

        :var Meta: String or Number
        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var number: String or Number
        :var pin: String or Number
        :var track: String or Number
        :var type: String or Number

cardPaypageType
---------------
    .. py:class:: vantivsdk.fields.cardPaypageType

        :var Meta: String or Number
        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var paypageRegistrationId: String or Number
        :var type: String or Number

cardTokenType
-------------
    .. py:class:: vantivsdk.fields.cardTokenType

        :var Meta: String or Number
        :var authenticatedShopperId: String or Number
        :var cardValidationNum: String or Number
        :var checkoutId: String or Number
        :var cnpToken: String or Number
        :var expDate: String or Number
        :var tokenUrl: String or Number
        :var type: String or Number

cardType
--------
    .. py:class:: vantivsdk.fields.cardType

        :var Meta: String or Number
        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var number: String or Number
        :var pin: String or Number
        :var track: String or Number
        :var type: String or Number

cnpInternalRecurringRequestType
-------------------------------
    .. py:class:: vantivsdk.fields.cnpInternalRecurringRequestType

        :var Meta: String or Number
        :var finalPayment: String or Number
        :var recurringTxnId: String or Number
        :var subscriptionId: String or Number

createAddOnType
---------------
    .. py:class:: vantivsdk.fields.createAddOnType

        :var Meta: String or Number
        :var addOnCode: String or Number
        :var amount: String or Number
        :var endDate: String or Number
        :var name: String or Number
        :var startDate: String or Number

createDiscountType
------------------
    .. py:class:: vantivsdk.fields.createDiscountType

        :var Meta: String or Number
        :var amount: String or Number
        :var discountCode: String or Number
        :var endDate: String or Number
        :var name: String or Number
        :var startDate: String or Number

ctxPaymentInformationType
-------------------------
    .. py:class:: vantivsdk.fields.ctxPaymentInformationType

        :var Meta: String or Number
        :var ctxPaymentDetail: String or Number

customBilling
-------------
    .. py:class:: vantivsdk.fields.customBilling

        :var Meta: String or Number
        :var city: String or Number
        :var descriptor: String or Number
        :var phone: String or Number
        :var url: String or Number

customerInfo
------------
    .. py:class:: vantivsdk.fields.customerInfo

        :var Meta: String or Number
        :var customerCheckingAccount: String or Number
        :var customerRegistrationDate: String or Number
        :var customerSavingAccount: String or Number
        :var customerType: String or Number
        :var customerWorkTelephone: String or Number
        :var dob: String or Number
        :var employerName: String or Number
        :var incomeAmount: String or Number
        :var incomeCurrency: String or Number
        :var residenceStatus: String or Number
        :var ssn: String or Number
        :var yearsAtEmployer: String or Number
        :var yearsAtResidence: String or Number

deleteAddOnType
---------------
    .. py:class:: vantivsdk.fields.deleteAddOnType

        :var Meta: String or Number
        :var addOnCode: String or Number

deleteDiscountType
------------------
    .. py:class:: vantivsdk.fields.deleteDiscountType

        :var Meta: String or Number
        :var discountCode: String or Number

detailTax
---------
    .. py:class:: vantivsdk.fields.detailTax

        :var Meta: String or Number
        :var cardAcceptorTaxId: String or Number
        :var taxAmount: String or Number
        :var taxIncludedInTotal: String or Number
        :var taxRate: String or Number
        :var taxTypeIdentifier: String or Number

echeckForTokenType
------------------
    .. py:class:: vantivsdk.fields.echeckForTokenType

        :var Meta: String or Number
        :var accNum: String or Number
        :var routingNum: String or Number

echeckTokenType
---------------
    .. py:class:: vantivsdk.fields.echeckTokenType

        :var Meta: String or Number
        :var accType: String or Number
        :var checkNum: String or Number
        :var cnpToken: String or Number
        :var routingNum: String or Number

echeckType
----------
    .. py:class:: vantivsdk.fields.echeckType

        :var Meta: String or Number
        :var accNum: String or Number
        :var accType: String or Number
        :var ccdPaymentInformation: String or Number
        :var checkNum: String or Number
        :var routingNum: String or Number

echeckTypeCtx
-------------
    .. py:class:: vantivsdk.fields.echeckTypeCtx

        :var Meta: String or Number
        :var accNum: String or Number
        :var accType: String or Number
        :var ccdPaymentInformation: String or Number
        :var checkNum: String or Number
        :var ctxPaymentInformation: instance of :py:class:`vantivsdk.fields.ctxPaymentInformationType`
        :var routingNum: String or Number

enhancedData
------------
    .. py:class:: vantivsdk.fields.enhancedData

        :var Meta: String or Number
        :var customerReference: String or Number
        :var deliveryType: String or Number
        :var destinationCountryCode: String or Number
        :var destinationPostalCode: String or Number
        :var detailTax: instance of :py:class:`vantivsdk.fields.detailTax`
        :var discountAmount: String or Number
        :var dutyAmount: String or Number
        :var invoiceReferenceNumber: String or Number
        :var lineItemData: instance of :py:class:`vantivsdk.fields.lineItemData`
        :var orderDate: String or Number
        :var salesTax: String or Number
        :var shipFromPostalCode: String or Number
        :var shippingAmount: String or Number
        :var taxExempt: String or Number

filteringType
-------------
    .. py:class:: vantivsdk.fields.filteringType

        :var Meta: String or Number
        :var chargeback: String or Number
        :var international: String or Number
        :var prepaid: String or Number

fraudCheckType
--------------
    .. py:class:: vantivsdk.fields.fraudCheckType

        :var Meta: String or Number
        :var authenticatedByMerchant: String or Number
        :var authenticationProtocolVersion: String or Number
        :var authenticationTransactionId: String or Number
        :var authenticationValue: String or Number
        :var customerIpAddress: String or Number
        :var tokenAuthenticationValue: String or Number

fraudResult
-----------
    .. py:class:: vantivsdk.fields.fraudResult

        :var Meta: String or Number
        :var advancedAvsresult: String or Number
        :var advancedFraudResults: instance of :py:class:`vantivsdk.fields.advancedFraudResultsType`
        :var authenticationResult: String or Number
        :var avsResult: String or Number
        :var cardValidationResult: String or Number

giftCardCardType
----------------
    .. py:class:: vantivsdk.fields.giftCardCardType

        :var Meta: String or Number
        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var number: String or Number
        :var pin: String or Number
        :var track: String or Number
        :var type: String or Number

giropayType
-----------
    .. py:class:: vantivsdk.fields.giropayType

        :var Meta: String or Number
        :var preferredLanguage: String or Number

idealType
---------
    .. py:class:: vantivsdk.fields.idealType

        :var Meta: String or Number
        :var preferredLanguage: String or Number

lineItemData
------------
    .. py:class:: vantivsdk.fields.lineItemData

        :var Meta: String or Number
        :var commodityCode: String or Number
        :var detailTax: instance of :py:class:`vantivsdk.fields.detailTax`
        :var itemDescription: String or Number
        :var itemDiscountAmount: String or Number
        :var itemSequenceNumber: String or Number
        :var lineItemTotal: String or Number
        :var lineItemTotalWithTax: String or Number
        :var productCode: String or Number
        :var quantity: String or Number
        :var taxAmount: String or Number
        :var unitCost: String or Number
        :var unitOfMeasure: String or Number

lodgingCharge
-------------
    .. py:class:: vantivsdk.fields.lodgingCharge

        :var Meta: String or Number
        :var name: String or Number

lodgingInfo
-----------
    .. py:class:: vantivsdk.fields.lodgingInfo

        :var Meta: String or Number
        :var checkInDate: String or Number
        :var checkOutDate: String or Number
        :var customerServicePhone: String or Number
        :var duration: String or Number
        :var fireSafetyIndicator: String or Number
        :var hotelFolioNumber: String or Number
        :var lodgingCharge: instance of :py:class:`vantivsdk.fields.lodgingCharge`
        :var numAdults: String or Number
        :var programCode: String or Number
        :var propertyLocalPhone: String or Number
        :var roomRate: String or Number
        :var roomTax: String or Number

merchantDataType
----------------
    .. py:class:: vantivsdk.fields.merchantDataType

        :var Meta: String or Number
        :var affiliate: String or Number
        :var campaign: String or Number
        :var merchantGroupingId: String or Number

mposType
--------
    .. py:class:: vantivsdk.fields.mposType

        :var Meta: String or Number
        :var encryptedTrack: String or Number
        :var formatId: String or Number
        :var ksn: String or Number
        :var track1Status: String or Number
        :var track2Status: String or Number

payPal
------
    .. py:class:: vantivsdk.fields.payPal

        :var Meta: String or Number
        :var payerEmail: String or Number
        :var payerId: String or Number
        :var token: instance of :py:class:`vantivsdk.fields.cardTokenType`
        :var transactionId: String or Number

pinlessDebitRequestType
-----------------------
    .. py:class:: vantivsdk.fields.pinlessDebitRequestType

        :var Meta: String or Number
        :var preferredDebitNetworks: instance of :py:class:`vantivsdk.fields.preferredDebitNetworksType`
        :var routingPreference: String or Number

pos
---
    .. py:class:: vantivsdk.fields.pos

        :var Meta: String or Number
        :var capability: String or Number
        :var cardholderId: String or Number
        :var catLevel: String or Number
        :var entryMode: String or Number
        :var terminalId: String or Number

preferredDebitNetworksType
--------------------------
    .. py:class:: vantivsdk.fields.preferredDebitNetworksType

        :var Meta: String or Number
        :var debitNetworkName: String or Number

processingInstructions
----------------------
    .. py:class:: vantivsdk.fields.processingInstructions

        :var Meta: String or Number
        :var bypassVelocityCheck: String or Number

recurringRequestType
--------------------
    .. py:class:: vantivsdk.fields.recurringRequestType

        :var Meta: String or Number
        :var createSubscription: instance of :py:class:`vantivsdk.fields.recurringSubscriptionType`

recurringSubscriptionType
-------------------------
    .. py:class:: vantivsdk.fields.recurringSubscriptionType

        :var Meta: String or Number
        :var amount: String or Number
        :var createAddOn: instance of :py:class:`vantivsdk.fields.createAddOnType`
        :var createDiscount: instance of :py:class:`vantivsdk.fields.createDiscountType`
        :var numberOfPayments: String or Number
        :var planCode: String or Number
        :var startDate: String or Number

recyclingRequestType
--------------------
    .. py:class:: vantivsdk.fields.recyclingRequestType

        :var Meta: String or Number
        :var recycleBy: String or Number
        :var recycleId: String or Number

sepaDirectDebitType
-------------------
    .. py:class:: vantivsdk.fields.sepaDirectDebitType

        :var Meta: String or Number
        :var iban: String or Number
        :var mandateProvider: String or Number
        :var mandateReference: String or Number
        :var mandateSignatureDate: String or Number
        :var mandateUrl: String or Number
        :var preferredLanguage: String or Number
        :var sequenceType: String or Number

shipToAddress
-------------
    .. py:class:: vantivsdk.fields.shipToAddress

        :var Meta: String or Number
        :var addressLine1: String or Number
        :var addressLine2: String or Number
        :var addressLine3: String or Number
        :var city: String or Number
        :var companyName: String or Number
        :var country: String or Number
        :var email: String or Number
        :var firstName: String or Number
        :var lastName: String or Number
        :var middleInitial: String or Number
        :var name: String or Number
        :var phone: String or Number
        :var state: String or Number
        :var zip: String or Number

sofortType
----------
    .. py:class:: vantivsdk.fields.sofortType

        :var Meta: String or Number
        :var preferredLanguage: String or Number

token
-----
    .. py:class:: vantivsdk.fields.token

        :var Meta: String or Number
        :var authenticatedShopperId: String or Number
        :var cardValidationNum: String or Number
        :var checkoutId: String or Number
        :var cnpToken: String or Number
        :var expDate: String or Number
        :var tokenUrl: String or Number
        :var type: String or Number

updateAddOnType
---------------
    .. py:class:: vantivsdk.fields.updateAddOnType

        :var Meta: String or Number
        :var addOnCode: String or Number
        :var amount: String or Number
        :var endDate: String or Number
        :var name: String or Number
        :var startDate: String or Number

updateDiscountType
------------------
    .. py:class:: vantivsdk.fields.updateDiscountType

        :var Meta: String or Number
        :var amount: String or Number
        :var discountCode: String or Number
        :var endDate: String or Number
        :var name: String or Number
        :var startDate: String or Number

virtualGiftCardType
-------------------
    .. py:class:: vantivsdk.fields.virtualGiftCardType

        :var Meta: String or Number
        :var accountNumberLength: String or Number
        :var giftCardBin: String or Number

wallet
------
    .. py:class:: vantivsdk.fields.wallet

        :var Meta: String or Number
        :var walletSourceType: String or Number
        :var walletSourceTypeId: String or Number

