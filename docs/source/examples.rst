EXAMPLES
========

Using dict
----------
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
    # url = 'https://www.testvantivcnp.com/sandbox/communicator/online'
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
    print('cnpTransaction ID: %s' % response['authorizationResponse']['cnpTxnId'])

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
    print('cnpTransaction ID: %s' % response['batchResponse']['authorizationResponse']['cnpTxnId'])

Using object
------------
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
    # url = 'https://www.testvantivcnp.com/sandbox/communicator/online'
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
    print('cnpTransaction ID: %s' % response['authorizationResponse']['cnpTxnId'])

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
    print('cnpTransaction ID: %s' % response['batchResponse']['authorizationResponse']['cnpTxnId'])