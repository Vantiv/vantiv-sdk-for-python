Complex Types
=============

additionalCOFData
-----------------
    .. py:class:: vantivsdk.fields.additionalCOFData

        :var frequencyOfMIT: String or Number
        :var paymentType: String or Number
        :var sequenceIndicator: String or Number
        :var totalPaymentCount: String or Number
        :var uniqueId: String or Number
        :var validationReference: String or Number

address
-------
    .. py:class:: vantivsdk.fields.address

        :var addressLine1: String or Number
        :var addressLine2: String or Number
        :var addressLine3: String or Number
        :var city: String or Number
        :var country: String or Number
        :var state: String or Number
        :var zip: String or Number

advancedFraudChecksType
-----------------------
    .. py:class:: vantivsdk.fields.advancedFraudChecksType

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

        :var deviceReputationScore: String or Number
        :var deviceReviewStatus: String or Number
        :var triggeredRule: String or Number

applepayHeaderType
------------------
    .. py:class:: vantivsdk.fields.applepayHeaderType

        :var applicationData: String or Number
        :var ephemeralPublicKey: String or Number
        :var publicKeyHash: String or Number
        :var transactionId: String or Number

applepayType
------------
    .. py:class:: vantivsdk.fields.applepayType

        :var data: String or Number
        :var header: instance of :py:class:`vantivsdk.fields.applepayHeaderType`
        :var signature: String or Number
        :var version: String or Number

authInformation
---------------
    .. py:class:: vantivsdk.fields.authInformation

        :var authAmount: String or Number
        :var authCode: String or Number
        :var authDate: String or Number
        :var fraudResult: instance of :py:class:`vantivsdk.fields.fraudResult`

billToAddress
-------------
    .. py:class:: vantivsdk.fields.billToAddress

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
        :var sellerId: String or Number
        :var state: String or Number
        :var url: String or Number
        :var zip: String or Number

card
----
    .. py:class:: vantivsdk.fields.card

        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var number: String or Number
        :var pin: String or Number
        :var track: String or Number
        :var type: String or Number

cardPaypageType
---------------
    .. py:class:: vantivsdk.fields.cardPaypageType

        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var paypageRegistrationId: String or Number
        :var type: String or Number

cardTokenType
-------------
    .. py:class:: vantivsdk.fields.cardTokenType

        :var authenticatedShopperID: String or Number
        :var cardValidationNum: String or Number
        :var checkoutId: String or Number
        :var cnpToken: String or Number
        :var expDate: String or Number
        :var tokenURL: String or Number
        :var type: String or Number

cardType
--------
    .. py:class:: vantivsdk.fields.cardType

        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var number: String or Number
        :var pin: String or Number
        :var track: String or Number
        :var type: String or Number

cnpInternalRecurringRequestType
-------------------------------
    .. py:class:: vantivsdk.fields.cnpInternalRecurringRequestType

        :var finalPayment: String or Number
        :var recurringTxnId: String or Number
        :var subscriptionId: String or Number

createAddOnType
---------------
    .. py:class:: vantivsdk.fields.createAddOnType

        :var addOnCode: String or Number
        :var amount: String or Number
        :var endDate: String or Number
        :var name: String or Number
        :var startDate: String or Number

createDiscountType
------------------
    .. py:class:: vantivsdk.fields.createDiscountType

        :var amount: String or Number
        :var discountCode: String or Number
        :var endDate: String or Number
        :var name: String or Number
        :var startDate: String or Number

ctxPaymentInformationType
-------------------------
    .. py:class:: vantivsdk.fields.ctxPaymentInformationType

        :var ctxPaymentDetail: String or Number

customBilling
-------------
    .. py:class:: vantivsdk.fields.customBilling

        :var city: String or Number
        :var descriptor: String or Number
        :var phone: String or Number
        :var url: String or Number

customerInfo
------------
    .. py:class:: vantivsdk.fields.customerInfo

        :var accountCreatedDate: String or Number
        :var accountUsername: String or Number
        :var customerCheckingAccount: String or Number
        :var customerRegistrationDate: String or Number
        :var customerSavingAccount: String or Number
        :var customerType: String or Number
        :var customerWorkTelephone: String or Number
        :var dob: String or Number
        :var employerName: String or Number
        :var incomeAmount: String or Number
        :var incomeCurrency: String or Number
        :var membershipEmail: String or Number
        :var membershipId: String or Number
        :var membershipName: String or Number
        :var membershipPhone: String or Number
        :var residenceStatus: String or Number
        :var ssn: String or Number
        :var userAccountEmail: String or Number
        :var userAccountNumber: String or Number
        :var userAccountPhone: String or Number
        :var yearsAtEmployer: String or Number
        :var yearsAtResidence: String or Number

deleteAddOnType
---------------
    .. py:class:: vantivsdk.fields.deleteAddOnType

        :var addOnCode: String or Number

deleteDiscountType
------------------
    .. py:class:: vantivsdk.fields.deleteDiscountType

        :var discountCode: String or Number

detailTax
---------
    .. py:class:: vantivsdk.fields.detailTax

        :var cardAcceptorTaxId: String or Number
        :var taxAmount: String or Number
        :var taxIncludedInTotal: String or Number
        :var taxRate: String or Number
        :var taxTypeIdentifier: String or Number

echeckForTokenType
------------------
    .. py:class:: vantivsdk.fields.echeckForTokenType

        :var accNum: String or Number
        :var routingNum: String or Number

echeckTokenType
---------------
    .. py:class:: vantivsdk.fields.echeckTokenType

        :var accType: String or Number
        :var checkNum: String or Number
        :var cnpToken: String or Number
        :var routingNum: String or Number

echeckType
----------
    .. py:class:: vantivsdk.fields.echeckType

        :var accNum: String or Number
        :var accType: String or Number
        :var ccdPaymentInformation: String or Number
        :var checkNum: String or Number
        :var routingNum: String or Number

echeckTypeCtx
-------------
    .. py:class:: vantivsdk.fields.echeckTypeCtx

        :var accNum: String or Number
        :var accType: String or Number
        :var ccdPaymentInformation: String or Number
        :var checkNum: String or Number
        :var ctxPaymentInformation: instance of :py:class:`vantivsdk.fields.ctxPaymentInformationType`
        :var routingNum: String or Number

enhancedData
------------
    .. py:class:: vantivsdk.fields.enhancedData

        :var customerReference: String or Number
        :var deliveryType: String or Number
        :var destinationCountryCode: String or Number
        :var destinationPostalCode: String or Number
        :var detailTax: instance of :py:class:`vantivsdk.fields.detailTax`
        :var discountAmount: String or Number
        :var discountCode: String or Number
        :var discountPercent: String or Number
        :var dutyAmount: String or Number
        :var fulfilmentMethodType: String or Number
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

        :var chargeback: String or Number
        :var international: String or Number
        :var prepaid: String or Number

fraudCheckType
--------------
    .. py:class:: vantivsdk.fields.fraudCheckType

        :var authenticatedByMerchant: String or Number
        :var authenticationProtocolVersion: String or Number
        :var authenticationTransactionId: String or Number
        :var authenticationValue: String or Number
        :var customerIpAddress: String or Number
        :var tokenAuthenticationValue: String or Number

fraudResult
-----------
    .. py:class:: vantivsdk.fields.fraudResult

        :var advancedAVSResult: String or Number
        :var advancedFraudResults: instance of :py:class:`vantivsdk.fields.advancedFraudResultsType`
        :var authenticationResult: String or Number
        :var avsResult: String or Number
        :var cardValidationResult: String or Number

giftCardCardType
----------------
    .. py:class:: vantivsdk.fields.giftCardCardType

        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var number: String or Number
        :var pin: String or Number
        :var track: String or Number
        :var type: String or Number

giropayType
-----------
    .. py:class:: vantivsdk.fields.giropayType

        :var preferredLanguage: String or Number

healthcareAmounts
-----------------
    .. py:class:: vantivsdk.fields.healthcareAmounts

        :var RxAmount: String or Number
        :var clinicOtherAmount: String or Number
        :var copayAmount: String or Number
        :var dentalAmount: String or Number
        :var totalHealthcareAmount: String or Number
        :var visionAmount: String or Number

healthcareIIAS
--------------
    .. py:class:: vantivsdk.fields.healthcareIIAS

        :var IIASFlag: String or Number
        :var healthcareAmounts: instance of :py:class:`vantivsdk.fields.healthcareAmounts`

idealType
---------
    .. py:class:: vantivsdk.fields.idealType

        :var preferredLanguage: String or Number

lineItemData
------------
    .. py:class:: vantivsdk.fields.lineItemData

        :var commodityCode: String or Number
        :var detailTax: instance of :py:class:`vantivsdk.fields.detailTax`
        :var itemCategory: String or Number
        :var itemDescription: String or Number
        :var itemDiscountAmount: String or Number
        :var itemSequenceNumber: String or Number
        :var itemSubCategory: String or Number
        :var lineItemTotal: String or Number
        :var lineItemTotalWithTax: String or Number
        :var productCode: String or Number
        :var productId: String or Number
        :var productName: String or Number
        :var quantity: String or Number
        :var taxAmount: String or Number
        :var unitCost: String or Number
        :var unitOfMeasure: String or Number

lodgingCharge
-------------
    .. py:class:: vantivsdk.fields.lodgingCharge

        :var name: String or Number

lodgingInfo
-----------
    .. py:class:: vantivsdk.fields.lodgingInfo

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

        :var affiliate: String or Number
        :var campaign: String or Number
        :var merchantGroupingId: String or Number

mposType
--------
    .. py:class:: vantivsdk.fields.mposType

        :var encryptedTrack: String or Number
        :var formatId: String or Number
        :var ksn: String or Number
        :var track1Status: String or Number
        :var track2Status: String or Number

payPal
------
    .. py:class:: vantivsdk.fields.payPal

        :var payerEmail: String or Number
        :var payerId: String or Number
        :var token: instance of :py:class:`vantivsdk.fields.cardTokenType`
        :var transactionId: String or Number

pinlessDebitRequestType
-----------------------
    .. py:class:: vantivsdk.fields.pinlessDebitRequestType

        :var preferredDebitNetworks: instance of :py:class:`vantivsdk.fields.preferredDebitNetworksType`
        :var routingPreference: String or Number

pos
---
    .. py:class:: vantivsdk.fields.pos

        :var capability: String or Number
        :var cardholderId: String or Number
        :var catLevel: String or Number
        :var entryMode: String or Number
        :var terminalId: String or Number

preferredDebitNetworksType
--------------------------
    .. py:class:: vantivsdk.fields.preferredDebitNetworksType

        :var debitNetworkName: String or Number

processingInstructions
----------------------
    .. py:class:: vantivsdk.fields.processingInstructions

        :var bypassVelocityCheck: String or Number

recurringRequestType
--------------------
    .. py:class:: vantivsdk.fields.recurringRequestType

        :var createSubscription: instance of :py:class:`vantivsdk.fields.recurringSubscriptionType`

recurringSubscriptionType
-------------------------
    .. py:class:: vantivsdk.fields.recurringSubscriptionType

        :var amount: String or Number
        :var createAddOn: instance of :py:class:`vantivsdk.fields.createAddOnType`
        :var createDiscount: instance of :py:class:`vantivsdk.fields.createDiscountType`
        :var numberOfPayments: String or Number
        :var planCode: String or Number
        :var startDate: String or Number

recyclingRequestType
--------------------
    .. py:class:: vantivsdk.fields.recyclingRequestType

        :var recycleBy: String or Number
        :var recycleId: String or Number

retailerAddress
---------------
    .. py:class:: vantivsdk.fields.retailerAddress

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
        :var sellerId: String or Number
        :var state: String or Number
        :var url: String or Number
        :var zip: String or Number

sepaDirectDebitType
-------------------
    .. py:class:: vantivsdk.fields.sepaDirectDebitType

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
        :var sellerId: String or Number
        :var state: String or Number
        :var url: String or Number
        :var zip: String or Number

sofortType
----------
    .. py:class:: vantivsdk.fields.sofortType

        :var preferredLanguage: String or Number

token
-----
    .. py:class:: vantivsdk.fields.token

        :var authenticatedShopperID: String or Number
        :var cardValidationNum: String or Number
        :var checkoutId: String or Number
        :var cnpToken: String or Number
        :var expDate: String or Number
        :var tokenURL: String or Number
        :var type: String or Number

updateAddOnType
---------------
    .. py:class:: vantivsdk.fields.updateAddOnType

        :var addOnCode: String or Number
        :var amount: String or Number
        :var endDate: String or Number
        :var name: String or Number
        :var startDate: String or Number

updateDiscountType
------------------
    .. py:class:: vantivsdk.fields.updateDiscountType

        :var amount: String or Number
        :var discountCode: String or Number
        :var endDate: String or Number
        :var name: String or Number
        :var startDate: String or Number

virtualGiftCardType
-------------------
    .. py:class:: vantivsdk.fields.virtualGiftCardType

        :var accountNumberLength: String or Number
        :var giftCardBin: String or Number

wallet
------
    .. py:class:: vantivsdk.fields.wallet

        :var walletSourceType: String or Number
        :var walletSourceTypeId: String or Number

