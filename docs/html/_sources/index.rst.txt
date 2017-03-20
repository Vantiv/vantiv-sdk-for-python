Vantiv eCommerce Python SDKv2 documentation 11.0!
==================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

EXAMPLE
-------
.. code-block:: python
   :linenos:

    #Example for SDKv2
    from __future__ import print_function

    from vantivsdk import *

    # Initial Configuration object. If you have saved configuration in '.vantiv_python_sdk.conf' at system environment
    # variable: VANTIV_SDK_CONFIG or user home directory, the saved configuration will be automatically load.
    conf = utils.Configuration()

    # Configuration need following attributes for online request:
    # attributes = default value
    # user = ''
    # password = ''
    # merchantId = ''
    # reportGroup = 'Default Report Group'
    # url = 'https://www.testlitle.com/sandbox/communicator/online'
    # proxy = ''
    # print_xml = False

    # Initial Transaction.
    transaction = fields.authorization()
    transaction.orderId = '1'
    transaction.amount = 10010
    transaction.orderSource = 'ecommerce'
    transaction.id = 'ThisIsRequiredby11'

    # Create contact object
    contact = fields.contact()
    contact.name = 'John & Mary Smith'
    contact.addressLine1 = '1 Main St.'
    contact.city = 'Burlington'
    contact.state = 'MA'
    contact.zip = '01803-3747'
    contact.country = 'USA'
    # The type of billToAddress is contact
    transaction.billToAddress = contact

    # Create cardType object
    card = fields.cardType()
    card.number = '4100000000000000'
    card.expDate = '1215'
    card.cardValidationNum = '349'
    card.type = 'VI'
    # The type of card is cardType
    transaction.card = card

    # detail tax
    enhancedData = fields.enhancedData()
    enhancedData.customerReference = 'Litle'
    enhancedData.deliveryType = 'TBD'
    detailTax = fields.detailTax()
    detailTax.taxAmount = 100
    detailTax2 = fields.detailTax()
    detailTax2.taxAmount = 200
    # pyxb cannot bind multi occurs item, have to use pyxb.BIND
    enhancedData = pyxb.BIND(enhancedData.customerReference, enhancedData.deliveryType, detailTax, detailTax2)
    transaction.enhancedData = enhancedData

    # Send request to server and get response as dict
    response = online.request(transaction, conf)

    print('Message: %s' % response['authorizationResponse']['message'])
    print('LitleTransaction ID: %s' % response['authorizationResponse']['litleTxnId'])

    # Configuration need following attributes for batch request:
    # attributes = default value
    # sftp_username = ''
    # sftp_password = ''
    # sftp_url = ''
    # batch_requests_path = '/tmp/vantiv_sdk_batch_request'
    # batch_response_path = '/tmp/vantiv_sdk_batch_response'
    # fast_url = ''
    # fast_ssl = True
    # fast_port = ''
    # id = ''

    # Initial batch transactions container class
    transactions = batch.Transactions()

    # Add transaction to batch transactions container
    transactions.add(transaction)

    # Sent batch to server via socket and get response as dict
    response = batch.stream(transactions, conf)

    print('Message: %s' % response['batchResponse']['authorizationResponse']['message'])
    print('LitleTransaction ID: %s' % response['batchResponse']['authorizationResponse']['litleTxnId'])

API
------
batch.stream
............
    .. autofunction:: vantivsdk.batch.stream

batch.download
..............
    .. autofunction:: vantivsdk.batch.download

batch.submit
............
    .. autofunction:: vantivsdk.batch.submit

batch.retrieve
..............
    .. autofunction:: vantivsdk.batch.retrieve

batch.Transactions
..................
    .. autoclass:: vantivsdk.batch.Transactions
        :members:

online.request
..............
    .. autofunction:: vantivsdk.online.request

utils.Configuration
...................
    .. autoclass:: vantivsdk.utils.Configuration
        :members:

Transactions
------------
accountUpdate
.............
    .. py:class:: vantivsdk.fields.accountUpdate

        :var cardOrToken: instance of :py:class:`vantivsdk.fields.token`,  :py:class:`vantivsdk.fields.card`, 
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var reportGroup: String or Number

activate
........
    .. py:class:: vantivsdk.fields.activate

        :var amount: String or Number
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number
        :var virtualGiftCard: instance of :py:class:`vantivsdk.fields.virtualGiftCardType`

activateReversal
................
    .. py:class:: vantivsdk.fields.activateReversal

        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var originalAmount: String or Number
        :var originalRefCode: String or Number
        :var originalSequenceNumber: String or Number
        :var originalSystemTraceId: String or Number
        :var originalTxnTime: String or Number
        :var reportGroup: String or Number
        :var virtualGiftCardBin: String or Number

authReversal
............
    .. py:class:: vantivsdk.fields.authReversal

        :var actionReason: String or Number
        :var amount: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var payPalNotes: String or Number
        :var reportGroup: String or Number
        :var surchargeAmount: String or Number

authorization
.............
    .. py:class:: vantivsdk.fields.authorization

        :var advancedFraudChecks: String or Number
        :var allowPartialAuth: String or Number
        :var amexAggregatorData: instance of :py:class:`vantivsdk.fields.amexAggregatorData`
        :var amount: String or Number
        :var applepay: instance of :py:class:`vantivsdk.fields.applepayType`
        :var billMeLaterRequest: instance of :py:class:`vantivsdk.fields.billMeLaterRequest`
        :var billToAddress: instance of :py:class:`vantivsdk.fields.contact`
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var cardholderAuthentication: String or Number
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var customerInfo: instance of :py:class:`vantivsdk.fields.customerInfo`
        :var debtRepayment: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var filtering: String or Number
        :var fraudFilterOverride: String or Number
        :var healthcareIIAS: instance of :py:class:`vantivsdk.fields.healthcareIIAS`
        :var id: String or Number
        :var litleTxnId: String or Number
        :var merchantData: String or Number
        :var mpos: instance of :py:class:`vantivsdk.fields.mposType`
        :var orderId: String or Number
        :var orderSource: String or Number
        :var originalNetworkTransactionId: String or Number
        :var originalTransactionAmount: String or Number
        :var paypage: instance of :py:class:`vantivsdk.fields.cardPaypageType`
        :var paypal: instance of :py:class:`vantivsdk.fields.payPal`
        :var pos: instance of :py:class:`vantivsdk.fields.pos`
        :var processingInstructions: instance of :py:class:`vantivsdk.fields.processingInstructions`
        :var processingType: String or Number
        :var recurringRequest: String or Number
        :var recyclingRequest: String or Number
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number
        :var shipToAddress: instance of :py:class:`vantivsdk.fields.contact`
        :var surchargeAmount: String or Number
        :var taxType: String or Number
        :var token: instance of :py:class:`vantivsdk.fields.cardTokenType`
        :var wallet: instance of :py:class:`vantivsdk.fields.wallet`

balanceInquiry
..............
    .. py:class:: vantivsdk.fields.balanceInquiry

        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

cancelSubscription
..................
    .. py:class:: vantivsdk.fields.cancelSubscription

        :var subscriptionId: String or Number

capture
.......
    .. py:class:: vantivsdk.fields.capture

        :var amount: String or Number
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var id: String or Number
        :var litleTxnId: String or Number
        :var partial: String or Number
        :var payPalNotes: String or Number
        :var payPalOrderComplete: String or Number
        :var pin: String or Number
        :var processingInstructions: instance of :py:class:`vantivsdk.fields.processingInstructions`
        :var reportGroup: String or Number
        :var surchargeAmount: String or Number

captureGivenAuth
................
    .. py:class:: vantivsdk.fields.captureGivenAuth

        :var amexAggregatorData: instance of :py:class:`vantivsdk.fields.amexAggregatorData`
        :var amount: String or Number
        :var authInformation: instance of :py:class:`vantivsdk.fields.authInformation`
        :var billMeLaterRequest: instance of :py:class:`vantivsdk.fields.billMeLaterRequest`
        :var billToAddress: instance of :py:class:`vantivsdk.fields.contact`
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var debtRepayment: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var id: String or Number
        :var merchantData: String or Number
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
        :var secondaryAmount: String or Number
        :var shipToAddress: instance of :py:class:`vantivsdk.fields.contact`
        :var surchargeAmount: String or Number
        :var taxType: String or Number
        :var token: instance of :py:class:`vantivsdk.fields.cardTokenType`

createPlan
..........
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
......
    .. py:class:: vantivsdk.fields.credit

        :var actionReason: String or Number
        :var amexAggregatorData: instance of :py:class:`vantivsdk.fields.amexAggregatorData`
        :var amount: String or Number
        :var billMeLaterRequest: instance of :py:class:`vantivsdk.fields.billMeLaterRequest`
        :var billToAddress: instance of :py:class:`vantivsdk.fields.contact`
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var id: String or Number
        :var litleTxnId: String or Number
        :var merchantData: String or Number
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

deactivate
..........
    .. py:class:: vantivsdk.fields.deactivate

        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

deactivateReversal
..................
    .. py:class:: vantivsdk.fields.deactivateReversal

        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var originalRefCode: String or Number
        :var originalSequenceNumber: String or Number
        :var originalSystemTraceId: String or Number
        :var originalTxnTime: String or Number
        :var reportGroup: String or Number

depositReversal
...............
    .. py:class:: vantivsdk.fields.depositReversal

        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var originalAmount: String or Number
        :var originalRefCode: String or Number
        :var originalSequenceNumber: String or Number
        :var originalSystemTraceId: String or Number
        :var originalTxnTime: String or Number
        :var reportGroup: String or Number

echeckCredit
............
    .. py:class:: vantivsdk.fields.echeckCredit

        :var amount: String or Number
        :var billToAddress: instance of :py:class:`vantivsdk.fields.contact`
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customIdentifier: String or Number
        :var customerId: String or Number
        :var echeckOrEcheckToken: instance of :py:class:`vantivsdk.fields.echeckToken`,  :py:class:`vantivsdk.fields.echeck`, 
        :var id: String or Number
        :var litleTxnId: String or Number
        :var merchantData: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number

echeckPreNoteCredit
...................
    .. py:class:: vantivsdk.fields.echeckPreNoteCredit

        :var billToAddress: instance of :py:class:`vantivsdk.fields.contact`
        :var customerId: String or Number
        :var echeck: instance of :py:class:`vantivsdk.fields.echeckType`
        :var id: String or Number
        :var merchantData: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

echeckPreNoteSale
.................
    .. py:class:: vantivsdk.fields.echeckPreNoteSale

        :var billToAddress: instance of :py:class:`vantivsdk.fields.contact`
        :var customerId: String or Number
        :var echeck: instance of :py:class:`vantivsdk.fields.echeckType`
        :var id: String or Number
        :var merchantData: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

echeckRedeposit
...............
    .. py:class:: vantivsdk.fields.echeckRedeposit

        :var customIdentifier: String or Number
        :var customerId: String or Number
        :var echeckOrEcheckToken: instance of :py:class:`vantivsdk.fields.echeckToken`,  :py:class:`vantivsdk.fields.echeck`, 
        :var id: String or Number
        :var litleTxnId: String or Number
        :var merchantData: String or Number
        :var reportGroup: String or Number

echeckSale
..........
    .. py:class:: vantivsdk.fields.echeckSale

        :var amount: String or Number
        :var billToAddress: instance of :py:class:`vantivsdk.fields.contact`
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customIdentifier: String or Number
        :var customerId: String or Number
        :var echeckOrEcheckToken: instance of :py:class:`vantivsdk.fields.echeckToken`,  :py:class:`vantivsdk.fields.echeck`, 
        :var id: String or Number
        :var litleTxnId: String or Number
        :var merchantData: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number
        :var shipToAddress: instance of :py:class:`vantivsdk.fields.contact`
        :var verify: String or Number

echeckVerification
..................
    .. py:class:: vantivsdk.fields.echeckVerification

        :var amount: String or Number
        :var billToAddress: instance of :py:class:`vantivsdk.fields.contact`
        :var customerId: String or Number
        :var echeckOrEcheckToken: instance of :py:class:`vantivsdk.fields.echeckToken`,  :py:class:`vantivsdk.fields.echeck`, 
        :var id: String or Number
        :var merchantData: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

echeckVoid
..........
    .. py:class:: vantivsdk.fields.echeckVoid

        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var reportGroup: String or Number

forceCapture
............
    .. py:class:: vantivsdk.fields.forceCapture

        :var amexAggregatorData: instance of :py:class:`vantivsdk.fields.amexAggregatorData`
        :var amount: String or Number
        :var billToAddress: instance of :py:class:`vantivsdk.fields.contact`
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var debtRepayment: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var id: String or Number
        :var merchantData: String or Number
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
..........
    .. py:class:: vantivsdk.fields.fraudCheck

        :var advancedFraudChecks: String or Number
        :var amount: String or Number
        :var billToAddress: instance of :py:class:`vantivsdk.fields.contact`
        :var customerId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number
        :var shipToAddress: instance of :py:class:`vantivsdk.fields.contact`

fundingInstructionVoid
......................
    .. py:class:: vantivsdk.fields.fundingInstructionVoid

        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var reportGroup: String or Number

giftCardAuthReversal
....................
    .. py:class:: vantivsdk.fields.giftCardAuthReversal

        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var originalAmount: String or Number
        :var originalRefCode: String or Number
        :var originalSequenceNumber: String or Number
        :var originalSystemTraceId: String or Number
        :var originalTxnTime: String or Number
        :var reportGroup: String or Number

giftCardCapture
...............
    .. py:class:: vantivsdk.fields.giftCardCapture

        :var captureAmount: String or Number
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var originalAmount: String or Number
        :var originalRefCode: String or Number
        :var originalTxnTime: String or Number
        :var partial: String or Number
        :var reportGroup: String or Number

giftCardCredit
..............
    .. py:class:: vantivsdk.fields.giftCardCredit

        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var creditAmount: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

load
....
    .. py:class:: vantivsdk.fields.load

        :var amount: String or Number
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

loadReversal
............
    .. py:class:: vantivsdk.fields.loadReversal

        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var originalAmount: String or Number
        :var originalRefCode: String or Number
        :var originalSequenceNumber: String or Number
        :var originalSystemTraceId: String or Number
        :var originalTxnTime: String or Number
        :var reportGroup: String or Number

payFacCredit
............
    .. py:class:: vantivsdk.fields.payFacCredit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

payFacDebit
...........
    .. py:class:: vantivsdk.fields.payFacDebit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

physicalCheckCredit
...................
    .. py:class:: vantivsdk.fields.physicalCheckCredit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

physicalCheckDebit
..................
    .. py:class:: vantivsdk.fields.physicalCheckDebit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

queryTransaction
................
    .. py:class:: vantivsdk.fields.queryTransaction

        :var customerId: String or Number
        :var id: String or Number
        :var origActionType: String or Number
        :var origId: String or Number
        :var origLitleTxnId: String or Number
        :var reportGroup: String or Number

refundReversal
..............
    .. py:class:: vantivsdk.fields.refundReversal

        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var originalAmount: String or Number
        :var originalRefCode: String or Number
        :var originalSequenceNumber: String or Number
        :var originalSystemTraceId: String or Number
        :var originalTxnTime: String or Number
        :var reportGroup: String or Number

reserveCredit
.............
    .. py:class:: vantivsdk.fields.reserveCredit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

reserveDebit
............
    .. py:class:: vantivsdk.fields.reserveDebit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

sale
....
    .. py:class:: vantivsdk.fields.sale

        :var advancedFraudChecks: String or Number
        :var allowPartialAuth: String or Number
        :var amexAggregatorData: instance of :py:class:`vantivsdk.fields.amexAggregatorData`
        :var amount: String or Number
        :var applepay: instance of :py:class:`vantivsdk.fields.applepayType`
        :var billMeLaterRequest: instance of :py:class:`vantivsdk.fields.billMeLaterRequest`
        :var billToAddress: instance of :py:class:`vantivsdk.fields.contact`
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var cardholderAuthentication: String or Number
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var customerInfo: instance of :py:class:`vantivsdk.fields.customerInfo`
        :var debtRepayment: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var filtering: String or Number
        :var fraudCheck: instance of :py:class:`vantivsdk.fields.fraudCheck`
        :var fraudFilterOverride: String or Number
        :var giropay: instance of :py:class:`vantivsdk.fields.giropayType`
        :var healthcareIIAS: instance of :py:class:`vantivsdk.fields.healthcareIIAS`
        :var id: String or Number
        :var ideal: instance of :py:class:`vantivsdk.fields.idealType`
        :var litleInternalRecurringRequest: String or Number
        :var litleTxnId: String or Number
        :var merchantData: String or Number
        :var mpos: instance of :py:class:`vantivsdk.fields.mposType`
        :var orderId: String or Number
        :var orderSource: String or Number
        :var originalNetworkTransactionId: String or Number
        :var originalTransactionAmount: String or Number
        :var payPalNotes: String or Number
        :var payPalOrderComplete: String or Number
        :var paypage: instance of :py:class:`vantivsdk.fields.cardPaypageType`
        :var paypal: instance of :py:class:`vantivsdk.fields.payPal`
        :var pos: instance of :py:class:`vantivsdk.fields.pos`
        :var processingInstructions: instance of :py:class:`vantivsdk.fields.processingInstructions`
        :var processingType: String or Number
        :var recurringRequest: String or Number
        :var recyclingRequest: String or Number
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number
        :var sepaDirectDebit: instance of :py:class:`vantivsdk.fields.sepaDirectDebitType`
        :var shipToAddress: instance of :py:class:`vantivsdk.fields.contact`
        :var sofort: instance of :py:class:`vantivsdk.fields.sofortType`
        :var surchargeAmount: String or Number
        :var taxType: String or Number
        :var token: instance of :py:class:`vantivsdk.fields.cardTokenType`
        :var wallet: instance of :py:class:`vantivsdk.fields.wallet`

serviceStatusRequest
....................
    .. py:class:: vantivsdk.fields.serviceStatusRequest

        :var customerId: String or Number
        :var id: String or Number
        :var pathId: String or Number
        :var reportGroup: String or Number
        :var serviceId: String or Number

submerchantCredit
.................
    .. py:class:: vantivsdk.fields.submerchantCredit

        :var accountInfo: instance of :py:class:`vantivsdk.fields.echeckType`
        :var amount: String or Number
        :var customIdentifier: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number
        :var submerchantName: String or Number

submerchantDebit
................
    .. py:class:: vantivsdk.fields.submerchantDebit

        :var accountInfo: instance of :py:class:`vantivsdk.fields.echeckType`
        :var amount: String or Number
        :var customIdentifier: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number
        :var submerchantName: String or Number

unload
......
    .. py:class:: vantivsdk.fields.unload

        :var amount: String or Number
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

unloadReversal
..............
    .. py:class:: vantivsdk.fields.unloadReversal

        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var originalAmount: String or Number
        :var originalRefCode: String or Number
        :var originalSequenceNumber: String or Number
        :var originalSystemTraceId: String or Number
        :var originalTxnTime: String or Number
        :var reportGroup: String or Number

updatePlan
..........
    .. py:class:: vantivsdk.fields.updatePlan

        :var active: String or Number
        :var planCode: String or Number

updateSubscription
..................
    .. py:class:: vantivsdk.fields.updateSubscription

        :var billToAddress: instance of :py:class:`vantivsdk.fields.contact`
        :var billingDate: String or Number
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var createAddOn: String or Number
        :var createDiscount: String or Number
        :var deleteAddOn: String or Number
        :var deleteDiscount: String or Number
        :var paypage: instance of :py:class:`vantivsdk.fields.cardPaypageType`
        :var planCode: String or Number
        :var subscriptionId: String or Number
        :var token: instance of :py:class:`vantivsdk.fields.cardTokenType`
        :var updateAddOn: String or Number
        :var updateDiscount: String or Number

vendorCredit
............
    .. py:class:: vantivsdk.fields.vendorCredit

        :var accountInfo: instance of :py:class:`vantivsdk.fields.echeckType`
        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number
        :var vendorName: String or Number

vendorDebit
...........
    .. py:class:: vantivsdk.fields.vendorDebit

        :var accountInfo: instance of :py:class:`vantivsdk.fields.echeckType`
        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number
        :var vendorName: String or Number

void
....
    .. py:class:: vantivsdk.fields.void

        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var processingInstructions: instance of :py:class:`vantivsdk.fields.processingInstructions`
        :var reportGroup: String or Number

Complex Types
-------------
CTD_ANON_15
...........
    .. py:class:: vantivsdk.fields.CTD_ANON_15

        :var availableBalance: String or Number
        :var prepaidCardType: String or Number
        :var reloadable: String or Number
        :var type: String or Number

CTD_ANON_35
...........
    .. py:class:: vantivsdk.fields.CTD_ANON_35

        :var transactionResponse: instance of

RFRRequest
..........
    .. py:class:: vantivsdk.fields.RFRRequest

        :var accountUpdateFileRequestData: instance of :py:class:`vantivsdk.fields.accountUpdateFileRequestData`
        :var litleSessionId: String or Number

accountInfoType
...............
    .. py:class:: vantivsdk.fields.accountInfoType

        :var number: String or Number
        :var type: String or Number

accountUpdateFileRequestData
............................
    .. py:class:: vantivsdk.fields.accountUpdateFileRequestData

        :var merchantId: String or Number
        :var postDay: String or Number

accountUpdater
..............
    .. py:class:: vantivsdk.fields.accountUpdater

        :var extendedCardResponse: String or Number
        :var newAccountInfo: instance of :py:class:`vantivsdk.fields.echeckAccountInfoType`
        :var newCardInfo: instance of :py:class:`vantivsdk.fields.cardAccountInfoType`
        :var newCardTokenInfo: instance of :py:class:`vantivsdk.fields.cardTokenInfoType`
        :var newTokenInfo: instance of :py:class:`vantivsdk.fields.echeckTokenInfoType`
        :var originalAccountInfo: instance of :py:class:`vantivsdk.fields.echeckAccountInfoType`
        :var originalCardInfo: instance of :py:class:`vantivsdk.fields.cardAccountInfoType`
        :var originalCardTokenInfo: instance of :py:class:`vantivsdk.fields.cardTokenInfoType`
        :var originalTokenInfo: instance of :py:class:`vantivsdk.fields.echeckTokenInfoType`

advancedFraudChecksType
.......................
    .. py:class:: vantivsdk.fields.advancedFraudChecksType

        :var customAttribute1: String or Number
        :var customAttribute2: String or Number
        :var customAttribute3: String or Number
        :var customAttribute4: String or Number
        :var customAttribute5: String or Number
        :var threatMetrixSessionId: String or Number

advancedFraudResultsType
........................
    .. py:class:: vantivsdk.fields.advancedFraudResultsType

        :var deviceReputationScore: String or Number
        :var deviceReviewStatus: String or Number
        :var triggeredRule: String or Number

amexAggregatorData
..................
    .. py:class:: vantivsdk.fields.amexAggregatorData

        :var sellerId: String or Number
        :var sellerMerchantCategoryCode: String or Number

applepayHeaderType
..................
    .. py:class:: vantivsdk.fields.applepayHeaderType

        :var applicationData: String or Number
        :var ephemeralPublicKey: String or Number
        :var publicKeyHash: String or Number
        :var transactionId: String or Number

applepayType
............
    .. py:class:: vantivsdk.fields.applepayType

        :var data: String or Number
        :var header: String or Number
        :var signature: String or Number
        :var version: String or Number

authInformation
...............
    .. py:class:: vantivsdk.fields.authInformation

        :var authAmount: String or Number
        :var authCode: String or Number
        :var authDate: String or Number
        :var fraudResult: instance of :py:class:`vantivsdk.fields.fraudResult`

billMeLaterRequest
..................
    .. py:class:: vantivsdk.fields.billMeLaterRequest

        :var authorizationSourcePlatform: String or Number
        :var bmlMerchantId: String or Number
        :var bmlProductType: String or Number
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

cardAccountInfoType
...................
    .. py:class:: vantivsdk.fields.cardAccountInfoType

        :var expDate: String or Number
        :var number: String or Number
        :var type: String or Number

cardPaypageType
...............
    .. py:class:: vantivsdk.fields.cardPaypageType

        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var paypageRegistrationId: String or Number
        :var type: String or Number

cardTokenInfoType
.................
    .. py:class:: vantivsdk.fields.cardTokenInfoType

        :var bin: String or Number
        :var expDate: String or Number
        :var litleToken: String or Number
        :var type: String or Number

cardTokenType
.............
    .. py:class:: vantivsdk.fields.cardTokenType

        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var litleToken: String or Number
        :var type: String or Number

cardTokenTypeAU
...............
    .. py:class:: vantivsdk.fields.cardTokenTypeAU

        :var bin: String or Number
        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var litleToken: String or Number
        :var type: String or Number

cardType
........
    .. py:class:: vantivsdk.fields.cardType

        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var number: String or Number
        :var pin: String or Number
        :var track: String or Number
        :var type: String or Number

contact
.......
    .. py:class:: vantivsdk.fields.contact

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

createAddOnType
...............
    .. py:class:: vantivsdk.fields.createAddOnType

        :var addOnCode: String or Number
        :var amount: String or Number
        :var endDate: String or Number
        :var name: String or Number
        :var startDate: String or Number

createDiscountType
..................
    .. py:class:: vantivsdk.fields.createDiscountType

        :var amount: String or Number
        :var discountCode: String or Number
        :var endDate: String or Number
        :var name: String or Number
        :var startDate: String or Number

customBilling
.............
    .. py:class:: vantivsdk.fields.customBilling

        :var city: String or Number
        :var descriptor: String or Number
        :var phone: String or Number
        :var url: String or Number

customerInfo
............
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
...............
    .. py:class:: vantivsdk.fields.deleteAddOnType

        :var addOnCode: String or Number

deleteDiscountType
..................
    .. py:class:: vantivsdk.fields.deleteDiscountType

        :var discountCode: String or Number

detailTax
.........
    .. py:class:: vantivsdk.fields.detailTax

        :var cardAcceptorTaxId: String or Number
        :var taxAmount: String or Number
        :var taxIncludedInTotal: String or Number
        :var taxRate: String or Number
        :var taxTypeIdentifier: String or Number

driversLicenseInfo
..................
    .. py:class:: vantivsdk.fields.driversLicenseInfo

        :var dateOfBirth: String or Number
        :var licenseNumber: String or Number
        :var state: String or Number

echeckAccountInfoType
.....................
    .. py:class:: vantivsdk.fields.echeckAccountInfoType

        :var accNum: String or Number
        :var accType: String or Number
        :var routingNum: String or Number

echeckForTokenType
..................
    .. py:class:: vantivsdk.fields.echeckForTokenType

        :var accNum: String or Number
        :var routingNum: String or Number

echeckTokenInfoType
...................
    .. py:class:: vantivsdk.fields.echeckTokenInfoType

        :var accType: String or Number
        :var litleToken: String or Number
        :var routingNum: String or Number

echeckTokenType
...............
    .. py:class:: vantivsdk.fields.echeckTokenType

        :var accType: String or Number
        :var checkNum: String or Number
        :var litleToken: String or Number
        :var routingNum: String or Number

echeckType
..........
    .. py:class:: vantivsdk.fields.echeckType

        :var accNum: String or Number
        :var accType: String or Number
        :var ccdPaymentInformation: String or Number
        :var checkNum: String or Number
        :var routingNum: String or Number

enhancedData
............
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
.............
    .. py:class:: vantivsdk.fields.filteringType

        :var chargeback: String or Number
        :var international: String or Number
        :var prepaid: String or Number

fraudCheckType
..............
    .. py:class:: vantivsdk.fields.fraudCheckType

        :var authenticatedByMerchant: String or Number
        :var authenticationTransactionId: String or Number
        :var authenticationValue: String or Number
        :var customerIpAddress: String or Number

fraudResult
...........
    .. py:class:: vantivsdk.fields.fraudResult

        :var advancedAVSResult: String or Number
        :var advancedFraudResults: String or Number
        :var authenticationResult: String or Number
        :var avsResult: String or Number
        :var cardValidationResult: String or Number

giftCardCardType
................
    .. py:class:: vantivsdk.fields.giftCardCardType

        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var number: String or Number
        :var pin: String or Number
        :var track: String or Number
        :var type: String or Number

giropayType
...........
    .. py:class:: vantivsdk.fields.giropayType

        :var preferredLanguage: String or Number

healthcareAmounts
.................
    .. py:class:: vantivsdk.fields.healthcareAmounts

        :var RxAmount: String or Number
        :var clinicOtherAmount: String or Number
        :var dentalAmount: String or Number
        :var totalHealthcareAmount: String or Number
        :var visionAmount: String or Number

healthcareIIAS
..............
    .. py:class:: vantivsdk.fields.healthcareIIAS

        :var IIASFlag: String or Number
        :var healthcareAmounts: instance of :py:class:`vantivsdk.fields.healthcareAmounts`

idealType
.........
    .. py:class:: vantivsdk.fields.idealType

        :var preferredLanguage: String or Number

lineItemData
............
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
.................................
    .. py:class:: vantivsdk.fields.litleInternalRecurringRequestType

        :var finalPayment: String or Number
        :var recurringTxnId: String or Number
        :var subscriptionId: String or Number

litleOnlineRequest
..................
    .. py:class:: vantivsdk.fields.litleOnlineRequest

        :var authentication: instance of :py:class:`vantivsdk.fields.authentication`
        :var loggedInUser: String or Number
        :var merchantId: String or Number
        :var merchantSdk: String or Number
        :var recurringTransaction: instance of
        :var transaction: instance of :py:class:`vantivsdk.fields.updateCardValidationNumOnToken`,  :py:class:`vantivsdk.fields.registerTokenRequest`, 
        :var version: String or Number

litleRequest
............
    .. py:class:: vantivsdk.fields.litleRequest

        :var RFRRequest: instance of :py:class:`vantivsdk.fields.RFRRequest`
        :var authentication: instance of :py:class:`vantivsdk.fields.authentication`
        :var batchRequest: instance of :py:class:`vantivsdk.fields.batchRequest`
        :var id: String or Number
        :var numBatchRequests: String or Number
        :var version: String or Number

merchantDataType
................
    .. py:class:: vantivsdk.fields.merchantDataType

        :var affiliate: String or Number
        :var campaign: String or Number
        :var merchantGroupingId: String or Number

mposType
........
    .. py:class:: vantivsdk.fields.mposType

        :var encryptedTrack: String or Number
        :var formatId: String or Number
        :var ksn: String or Number
        :var track1Status: String or Number
        :var track2Status: String or Number

networkField
............
    .. py:class:: vantivsdk.fields.networkField

        :var fieldName: String or Number
        :var fieldNumber: String or Number
        :var fieldValue: String or Number
        :var networkSubField: instance of :py:class:`vantivsdk.fields.networkSubField`

networkSubField
...............
    .. py:class:: vantivsdk.fields.networkSubField

        :var fieldNumber: String or Number
        :var fieldValue: String or Number

payPal
......
    .. py:class:: vantivsdk.fields.payPal

        :var payerEmail: String or Number
        :var payerId: String or Number
        :var token: instance of :py:class:`vantivsdk.fields.cardTokenType`
        :var transactionId: String or Number

pos
...
    .. py:class:: vantivsdk.fields.pos

        :var capability: String or Number
        :var cardholderId: String or Number
        :var catLevel: String or Number
        :var entryMode: String or Number
        :var terminalId: String or Number

processingInstructions
......................
    .. py:class:: vantivsdk.fields.processingInstructions

        :var bypassVelocityCheck: String or Number

recurringRequestType
....................
    .. py:class:: vantivsdk.fields.recurringRequestType

        :var subscription: String or Number

recurringSubscriptionType
.........................
    .. py:class:: vantivsdk.fields.recurringSubscriptionType

        :var amount: String or Number
        :var createAddOn: String or Number
        :var createDiscount: String or Number
        :var numberOfPayments: String or Number
        :var planCode: String or Number
        :var startDate: String or Number

recycleAdviceType
.................
    .. py:class:: vantivsdk.fields.recycleAdviceType

        :var nextRecycleTime: String or Number
        :var recycleAdviceEnd: String or Number

recyclingRequestType
....................
    .. py:class:: vantivsdk.fields.recyclingRequestType

        :var recycleBy: String or Number
        :var recycleId: String or Number

recyclingType
.............
    .. py:class:: vantivsdk.fields.recyclingType

        :var recycleAdvice: String or Number
        :var recycleEngineActive: String or Number

registerTokenRequestType
........................
    .. py:class:: vantivsdk.fields.registerTokenRequestType

        :var accountNumber: String or Number
        :var applepay: instance of :py:class:`vantivsdk.fields.applepayType`
        :var cardValidationNum: String or Number
        :var customerId: String or Number
        :var echeckForToken: instance of :py:class:`vantivsdk.fields.echeckForTokenType`
        :var id: String or Number
        :var mpos: instance of :py:class:`vantivsdk.fields.mposType`
        :var orderId: String or Number
        :var paypageRegistrationId: String or Number
        :var reportGroup: String or Number

sepaDirectDebitType
...................
    .. py:class:: vantivsdk.fields.sepaDirectDebitType

        :var iban: String or Number
        :var mandateProvider: String or Number
        :var mandateReference: String or Number
        :var mandateSignatureDate: String or Number
        :var mandateUrl: String or Number
        :var preferredLanguage: String or Number
        :var sequenceType: String or Number

sofortType
..........
    .. py:class:: vantivsdk.fields.sofortType

        :var preferredLanguage: String or Number

updateAddOnType
...............
    .. py:class:: vantivsdk.fields.updateAddOnType

        :var addOnCode: String or Number
        :var amount: String or Number
        :var endDate: String or Number
        :var name: String or Number
        :var startDate: String or Number

updateCardValidationNumOnToken_
...............................
    .. py:class:: vantivsdk.fields.updateCardValidationNumOnToken_

        :var cardValidationNum: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var litleToken: String or Number
        :var orderId: String or Number
        :var reportGroup: String or Number

updateDiscountType
..................
    .. py:class:: vantivsdk.fields.updateDiscountType

        :var amount: String or Number
        :var discountCode: String or Number
        :var endDate: String or Number
        :var name: String or Number
        :var startDate: String or Number

virtualGiftCardType
...................
    .. py:class:: vantivsdk.fields.virtualGiftCardType

        :var accountNumberLength: String or Number
        :var giftCardBin: String or Number

wallet
......
    .. py:class:: vantivsdk.fields.wallet

        :var walletSourceType: String or Number
        :var walletSourceTypeId: String or Number

