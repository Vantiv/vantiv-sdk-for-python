Vantiv eCommerce Python SDK
===========================
#### WARNING:
##### All major version changes require recertification to the new version. Once certified for the use of a new version, Vantiv modifies your Merchant Profile, allowing you to submit transaction to the Production Environment using the new version. Updating your code without recertification and modification of your Merchant Profile will result in transaction declines. Please consult you Implementation Analyst for additional information about this process.
About Vantiv eCommerce
----------------------
[Vantiv eCommerce](https://developer.vantiv.com/community/ecommerce) powers the payment processing engines for leading companies that sell directly to consumers through  internet retail, direct response marketing (TV, radio and telephone), and online services. Vantiv eCommerce is the leading authority in card-not-present (CNP) commerce, transaction processing and merchant services.


About this SDK
--------------
The Vantiv eCommerce Python SDK is a Python implementation of the [Vantiv eCommerce](https://developer.vantiv.com/community/ecommerce) XML API. This SDK was created to make it as easy as possible to connect to and process payments through Vantiv eCommerce. This SDK utilizes the HTTPS protocol to securely connect to Vantiv eCommerce.  Using the SDK requires coordination with the Vantiv eCommerce team to obtain credentials for accessing our systems.

Each Python SDK release supports all of the functionality present in the associated Vantiv eCommerce XML version (e.g., 12.0.x supports Vantiv eCommerce XML v12.0). Please see the online copy of our XSD for Vantiv eCommerce XML to get more details on what the Vantiv eCommerce payments engine supports .

This SDK was implemented to support the Python2 version 2.7.9 and later, Python3 version 3.4 and later, and was created by Vantiv eCommerce. Its intended use is for online transaction processing utilizing your account on the Vantiv eCommerce payments engine.

See LICENSE file for details on using this software.

Source Code available from : https://github.com/Vantiv/vantiv-sdk-for-python.git

More examples can be found here https://github.com/Vantiv/vantiv-sdk-for-python/tree/12.x/samples

Detail documents can be found here http://vantivecommercepythonsdk.readthedocs.io/en/12.x/

Please contact [Vantiv eCommerce](https://developer.vantiv.com/community/ecommerce) to receive valid merchant credentials and determine which version of the SDK is right for your business requirements or if you require assistance in any other way.  You can reach us at sdksupport@Vantiv.com

Dependencies
------------
* pyxb v1.2.5 : http://pyxb.sourceforge.net/
* paramiko v1.14.0: http://www.paramiko.org/
* requests v2.13.0: http://docs.python-requests.org/en/master/
* six v1.10.0: https://github.com/benjaminp/six
* xmltodict 0.10.2: https://github.com/martinblech/xmltodict

Setup
-----
1) To download and install:

Using pip 

>pip install VantiveCommerceSDK

Without Pip

>git clone https://github.com/Vantiv/vantiv-sdk-for-python.git

>cd vantiv-sdk-for-python

checkout branch master for XML v12.x
>git checkout master

>python setup.py install

2) setup configurations

>vantiv_python_sdk_setup

3) Create a python file similar to:

```python
#Example for SDK transaction presented by object
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

transaction.enhancedData = enhancedData

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
```

```python
#Example for SDK, transaction presented by dict
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

# Send request to server and get response as object
response = online.request(txn_dict, conf)

print('Message: %s' % response['batchResponse']['authorizationResponse']['message'])
print('cnpTransaction ID: %s' % response['batchResponse']['authorizationResponse']['cnpTxnId'])
```

NOTE: you may need to edit the proxy to to work for your system

4) Next run this file.  You should see the following result.

    Message: Valid Format
    cnp Transaction ID: <your-numeric-cnp-txn-id>

Please contact Vantiv eCommerce with any further questions. You can reach us at SDKSupport@Vantiv.com
