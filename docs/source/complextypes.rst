Complex Types
=============

advancedFraudChecksType
-----------------------
    .. py:class:: vantivsdk.fields.advancedFraudChecksType

        :var customAttribute1: String or Number
        :var customAttribute2: String or Number
        :var customAttribute3: String or Number
        :var customAttribute4: String or Number
        :var customAttribute5: String or Number
        :var threatMetrixSessionId: String or Number

advancedFraudResultsType
------------------------
    .. py:class:: vantivsdk.fields.advancedFraudResultsType

        :var deviceReputationScore: String or Number
        :var deviceReviewStatus: String or Number
        :var triggeredRule: String or Number

amexAggregatorData
------------------
    .. py:class:: vantivsdk.fields.amexAggregatorData

        :var sellerId: String or Number
        :var sellerMerchantCategoryCode: String or Number

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

billMeLaterRequest
------------------
    .. py:class:: vantivsdk.fields.billMeLaterRequest

        :var authorizationSourcePlatform: String or Number
        :var bmlMerchantId: String or Number
        :var bmlProductType: instance of :py:class:`vantivsdk.fields.bmlProductType`
        :var customerBillingAddressChanged: String or Number
        :var customerEmailChanged: String or Number
        :var customerPasswordChanged: String or Number
        :var customerPhoneChanged: String or Number
        :var itemCategoryCode: String or Number
        :var merchantPromotionalCode: String or Number
        :var preapprovalNumber: String or Number
        :var secretQuestionAnswer: String or Number
        :var secretQuestionCode: String or Number
        :var termsAndConditions: String or Number
        :var virtualAuthenticationKeyData: String or Number
        :var virtualAuthenticationKeyPresenceIndicator: String or Number

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
        :var state: String or Number
        :var zip: String or Number

bmlProductType
--------------
    .. py:class:: vantivsdk.fields.bmlProductType


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

        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var litleToken: String or Number
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

echeck
------
    .. py:class:: vantivsdk.fields.echeck

        :var accNum: String or Number
        :var accType: String or Number
        :var ccdPaymentInformation: String or Number
        :var checkNum: String or Number
        :var routingNum: String or Number

echeckForTokenType
------------------
    .. py:class:: vantivsdk.fields.echeckForTokenType

        :var accNum: String or Number
        :var routingNum: String or Number

echeckToken
-----------
    .. py:class:: vantivsdk.fields.echeckToken

        :var accType: String or Number
        :var checkNum: String or Number
        :var litleToken: String or Number
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

        :var chargeback: String or Number
        :var international: String or Number
        :var prepaid: String or Number

fraudCheckType
--------------
    .. py:class:: vantivsdk.fields.fraudCheckType

        :var authenticatedByMerchant: String or Number
        :var authenticationTransactionId: String or Number
        :var authenticationValue: String or Number
        :var customerIpAddress: String or Number

fraudResult
-----------
    .. py:class:: vantivsdk.fields.fraudResult

        :var advancedAVSResult: String or Number
        :var advancedFraudResults: instance of :py:class:`vantivsdk.fields.advancedFraudResultsType`
        :var authenticationResult: String or Number
        :var avsResult: String or Number
        :var cardValidationResult: String or Number

healthcareAmounts
-----------------
    .. py:class:: vantivsdk.fields.healthcareAmounts

        :var RxAmount: String or Number
        :var clinicOtherAmount: String or Number
        :var dentalAmount: String or Number
        :var totalHealthcareAmount: String or Number
        :var visionAmount: String or Number

healthcareIIAS
--------------
    .. py:class:: vantivsdk.fields.healthcareIIAS

        :var IIASFlag: String or Number
        :var healthcareAmounts: instance of :py:class:`vantivsdk.fields.healthcareAmounts`

lineItemData
------------
    .. py:class:: vantivsdk.fields.lineItemData

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

litleInternalRecurringRequestType
---------------------------------
    .. py:class:: vantivsdk.fields.litleInternalRecurringRequestType

        :var finalPayment: String or Number
        :var recurringTxnId: String or Number
        :var subscriptionId: String or Number

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
        :var token: String or Number
        :var transactionId: String or Number

pos
---
    .. py:class:: vantivsdk.fields.pos

        :var capability: String or Number
        :var cardholderId: String or Number
        :var catLevel: String or Number
        :var entryMode: String or Number
        :var terminalId: String or Number

processingInstructions
----------------------
    .. py:class:: vantivsdk.fields.processingInstructions

        :var bypassVelocityCheck: String or Number

recurringRequestType
--------------------
    .. py:class:: vantivsdk.fields.recurringRequestType

        :var subscription: instance of :py:class:`vantivsdk.fields.recurringSubscriptionType`

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
        :var state: String or Number
        :var zip: String or Number

token
-----
    .. py:class:: vantivsdk.fields.token

        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var litleToken: String or Number
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

