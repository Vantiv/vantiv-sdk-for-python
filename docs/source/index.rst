Vantiv eCommerce Python SDK documentation 9.12!
================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

EXAMPLE
-------
Using dict
..........
.. code-block:: python
   :linenos:

    #Example for SDK
    from __future__ import print_function, unicode_literals

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

    # Transaction presented by dict
    txn_dict ={
        'authorization':{
            'orderId': '1',
            'amount': 10010,
            'orderSource': 'ecommerce',
            'id': 'ThisIsRequiredby11',
            'billToAddress': {
                'name': 'John & Mary Smith',
                'addressLine1': '1 Main St.',
                'city': 'Burlington',
                'state': 'MA',
                'zip': '01803-3747',
                'country': 'USA'
            },
            'card': {
                'number': '4100000000000000',
                'expDate': '1215',
                'cardValidationNum' : '349',
                'type': 'VI'
            },
            'enhancedData':{
                'detailTax': [
                    {'taxAmount':100},
                    {'taxAmount':200},
                ],
            }
        }
    }

    # Send request to server and get response as dict
    response = online.request(txn_dict, conf)

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
    transactions.add(txn_dict)

    # Sent batch to server via socket and get response as dict
    response = batch.stream(transactions, conf)

    print('Message: %s' % response['batchResponse']['authorizationResponse']['message'])
    print('LitleTransaction ID: %s' % response['batchResponse']['authorizationResponse']['litleTxnId'])

Using object
............
.. code-block:: python
   :linenos:

    #Example for SDK
    from __future__ import print_function, unicode_literals

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
    detailTaxList = list()

    detailTax = fields.detailTax()
    detailTax.taxAmount = 100
    detailTaxList.append(detailTax)

    detailTax2 = fields.detailTax()
    detailTax2.taxAmount = 200
    detailTaxList.append(detailTax2)

    enhancedData = fields.enhancedData()
    enhancedData.detailTax = detailTaxList

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

        :var cardOrToken: instance of :py:class:`vantivsdk.fields.card`, :py:class:`vantivsdk.fields.token`, 
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

        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var reportGroup: String or Number

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

        :var advancedFraudChecks: instance of :py:class:`vantivsdk.fields.advancedFraudChecksType`
        :var allowPartialAuth: String or Number
        :var amexAggregatorData: instance of :py:class:`vantivsdk.fields.amexAggregatorData`
        :var amount: String or Number
        :var applepay: instance of :py:class:`vantivsdk.fields.applepayType`
        :var billMeLaterRequest: instance of :py:class:`vantivsdk.fields.billMeLaterRequest`
        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var cardholderAuthentication: instance of :py:class:`vantivsdk.fields.fraudCheckType`
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var customerInfo: instance of :py:class:`vantivsdk.fields.customerInfo`
        :var debtRepayment: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var filtering: instance of :py:class:`vantivsdk.fields.filteringType`
        :var fraudFilterOverride: String or Number
        :var healthcareIIAS: instance of :py:class:`vantivsdk.fields.healthcareIIAS`
        :var id: String or Number
        :var litleTxnId: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
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
        :var recurringRequest: instance of :py:class:`vantivsdk.fields.recurringRequestType`
        :var recyclingRequest: instance of :py:class:`vantivsdk.fields.recyclingRequestType`
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number
        :var shipToAddress: instance of :py:class:`vantivsdk.fields.shipToAddress`
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
        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var debtRepayment: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var id: String or Number
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
        :var secondaryAmount: String or Number
        :var shipToAddress: instance of :py:class:`vantivsdk.fields.shipToAddress`
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
        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var id: String or Number
        :var litleTxnId: String or Number
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

        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var reportGroup: String or Number

depositReversal
...............
    .. py:class:: vantivsdk.fields.depositReversal

        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var reportGroup: String or Number

echeckCredit
............
    .. py:class:: vantivsdk.fields.echeckCredit

        :var amount: String or Number
        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var echeckOrEcheckToken: instance of :py:class:`vantivsdk.fields.echeck`, :py:class:`vantivsdk.fields.echeckToken`, 
        :var id: String or Number
        :var litleTxnId: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number

echeckPreNoteCredit
...................
    .. py:class:: vantivsdk.fields.echeckPreNoteCredit

        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var customerId: String or Number
        :var echeck: instance of :py:class:`vantivsdk.fields.echeck`
        :var id: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

echeckPreNoteSale
.................
    .. py:class:: vantivsdk.fields.echeckPreNoteSale

        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var customerId: String or Number
        :var echeck: instance of :py:class:`vantivsdk.fields.echeck`
        :var id: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

echeckRedeposit
...............
    .. py:class:: vantivsdk.fields.echeckRedeposit

        :var customerId: String or Number
        :var echeckOrEcheckToken: instance of :py:class:`vantivsdk.fields.echeck`, :py:class:`vantivsdk.fields.echeckToken`, 
        :var id: String or Number
        :var litleTxnId: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
        :var reportGroup: String or Number

echeckSale
..........
    .. py:class:: vantivsdk.fields.echeckSale

        :var amount: String or Number
        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var echeckOrEcheckToken: instance of :py:class:`vantivsdk.fields.echeck`, :py:class:`vantivsdk.fields.echeckToken`, 
        :var id: String or Number
        :var litleTxnId: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number
        :var shipToAddress: instance of :py:class:`vantivsdk.fields.shipToAddress`
        :var verify: String or Number

echeckVerification
..................
    .. py:class:: vantivsdk.fields.echeckVerification

        :var amount: String or Number
        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var customerId: String or Number
        :var echeckOrEcheckToken: instance of :py:class:`vantivsdk.fields.echeck`, :py:class:`vantivsdk.fields.echeckToken`, 
        :var id: String or Number
        :var litleTxnId: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
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
        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var debtRepayment: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var id: String or Number
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
..........
    .. py:class:: vantivsdk.fields.fraudCheck

        :var advancedFraudChecks: instance of :py:class:`vantivsdk.fields.advancedFraudChecksType`
        :var amount: String or Number
        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var customerId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number
        :var shipToAddress: instance of :py:class:`vantivsdk.fields.shipToAddress`

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

        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
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
        :var origAccountNumber: String or Number
        :var origActionType: String or Number
        :var origId: String or Number
        :var origLitleTxnId: String or Number
        :var origOrderId: String or Number
        :var reportGroup: String or Number

refundReversal
..............
    .. py:class:: vantivsdk.fields.refundReversal

        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var reportGroup: String or Number

registerTokenRequest
....................
    .. py:class:: vantivsdk.fields.registerTokenRequest

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

        :var advancedFraudChecks: instance of :py:class:`vantivsdk.fields.advancedFraudChecksType`
        :var allowPartialAuth: String or Number
        :var amexAggregatorData: instance of :py:class:`vantivsdk.fields.amexAggregatorData`
        :var amount: String or Number
        :var applepay: instance of :py:class:`vantivsdk.fields.applepayType`
        :var billMeLaterRequest: instance of :py:class:`vantivsdk.fields.billMeLaterRequest`
        :var billToAddress: instance of :py:class:`vantivsdk.fields.billToAddress`
        :var card: instance of :py:class:`vantivsdk.fields.cardType`
        :var cardholderAuthentication: instance of :py:class:`vantivsdk.fields.fraudCheckType`
        :var customBilling: instance of :py:class:`vantivsdk.fields.customBilling`
        :var customerId: String or Number
        :var customerInfo: instance of :py:class:`vantivsdk.fields.customerInfo`
        :var debtRepayment: String or Number
        :var enhancedData: instance of :py:class:`vantivsdk.fields.enhancedData`
        :var filtering: instance of :py:class:`vantivsdk.fields.filteringType`
        :var fraudCheck: instance of :py:class:`vantivsdk.fields.fraudCheckType`
        :var fraudFilterOverride: String or Number
        :var healthcareIIAS: instance of :py:class:`vantivsdk.fields.healthcareIIAS`
        :var id: String or Number
        :var ideal: instance of :py:class:`vantivsdk.fields.idealType`
        :var litleInternalRecurringRequest: instance of :py:class:`vantivsdk.fields.litleInternalRecurringRequestType`
        :var litleTxnId: String or Number
        :var merchantData: instance of :py:class:`vantivsdk.fields.merchantDataType`
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
        :var recurringRequest: instance of :py:class:`vantivsdk.fields.recurringRequestType`
        :var recyclingRequest: instance of :py:class:`vantivsdk.fields.recyclingRequestType`
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number
        :var sepaDirectDebit: instance of :py:class:`vantivsdk.fields.sepaDirectDebitType`
        :var shipToAddress: instance of :py:class:`vantivsdk.fields.shipToAddress`
        :var surchargeAmount: String or Number
        :var taxType: String or Number
        :var token: instance of :py:class:`vantivsdk.fields.cardTokenType`
        :var wallet: instance of :py:class:`vantivsdk.fields.wallet`

submerchantCredit
.................
    .. py:class:: vantivsdk.fields.submerchantCredit

        :var accountInfo: instance of :py:class:`vantivsdk.fields.echeckType`
        :var amount: String or Number
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

        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var reportGroup: String or Number

updateCardValidationNumOnToken
..............................
    .. py:class:: vantivsdk.fields.updateCardValidationNumOnToken

        :var cardValidationNum: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var litleToken: String or Number
        :var orderId: String or Number
        :var reportGroup: String or Number

updatePlan
..........
    .. py:class:: vantivsdk.fields.updatePlan

        :var active: String or Number
        :var planCode: String or Number

updateSubscription
..................
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
        :var header: instance of :py:class:`vantivsdk.fields.applepayHeaderType`
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
.............
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
..............
    .. py:class:: vantivsdk.fields.bmlProductType


card
....
    .. py:class:: vantivsdk.fields.card

        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var number: String or Number
        :var pin: String or Number
        :var track: String or Number
        :var type: String or Number

cardPaypageType
...............
    .. py:class:: vantivsdk.fields.cardPaypageType

        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var paypageRegistrationId: String or Number
        :var type: String or Number

cardTokenType
.............
    .. py:class:: vantivsdk.fields.cardTokenType

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

echeck
......
    .. py:class:: vantivsdk.fields.echeck

        :var accNum: String or Number
        :var accType: String or Number
        :var ccdPaymentInformation: String or Number
        :var checkNum: String or Number
        :var routingNum: String or Number

echeckForTokenType
..................
    .. py:class:: vantivsdk.fields.echeckForTokenType

        :var accNum: String or Number
        :var routingNum: String or Number

echeckToken
...........
    .. py:class:: vantivsdk.fields.echeckToken

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
        :var advancedFraudResults: instance of :py:class:`vantivsdk.fields.advancedFraudResultsType`
        :var authenticationResult: String or Number
        :var avsResult: String or Number
        :var cardValidationResult: String or Number

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

payPal
......
    .. py:class:: vantivsdk.fields.payPal

        :var payerEmail: String or Number
        :var payerId: String or Number
        :var token: String or Number
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

        :var subscription: instance of :py:class:`vantivsdk.fields.recurringSubscriptionType`

recurringSubscriptionType
.........................
    .. py:class:: vantivsdk.fields.recurringSubscriptionType

        :var amount: String or Number
        :var createAddOn: instance of :py:class:`vantivsdk.fields.createAddOnType`
        :var createDiscount: instance of :py:class:`vantivsdk.fields.createDiscountType`
        :var numberOfPayments: String or Number
        :var planCode: String or Number
        :var startDate: String or Number

recyclingRequestType
....................
    .. py:class:: vantivsdk.fields.recyclingRequestType

        :var recycleBy: String or Number
        :var recycleId: String or Number

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

shipToAddress
.............
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
.....
    .. py:class:: vantivsdk.fields.token

        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var litleToken: String or Number
        :var type: String or Number

updateAddOnType
...............
    .. py:class:: vantivsdk.fields.updateAddOnType

        :var addOnCode: String or Number
        :var amount: String or Number
        :var endDate: String or Number
        :var name: String or Number
        :var startDate: String or Number

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

