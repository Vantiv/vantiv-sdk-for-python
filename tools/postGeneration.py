#!/usr/bin/env python
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
from __future__ import absolute_import, division, print_function

import os
import pprint
import re
import sys

# Require Python 2.7.9 or higher or Python 3.4 or higher
if (sys.version_info[:3] < (2, 7, 9)) or ((sys.version_info[0] == 3) and sys.version_info[:2] < (3, 4)):
    raise ValueError('''PyXB requires:
  Python2 version 2.7.9 or later; or
  Python3 version 3.4 or later
(You have %s.)''' % (sys.version,))

package_root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

sys.path.insert(0, package_root)
from vantivsdk import (fields, version)


def remove_absolute_path(_package_root):
    """Remove all absolute path in generated file by pyxbgen.

    Returns:
        None

    """
    fields_path = os.path.join(_package_root, 'vantivsdk', 'fields.py')
    with open(fields_path, 'r') as ori_xsd:
        lines = ori_xsd.readlines()

        lines_index = -1
        abs_location = re.compile('pyxb.utils.utility.Location\(')
        for line in lines:
            lines_index += 1
            if abs_location.search(line):
                abs_path = re.search("pyxb.utils.utility.Location\('(.*?)'", line).group(1).strip()
                new_line = line.replace(abs_path, os.path.basename(abs_path))
                lines[lines_index] = new_line
                print('-', line)
                print('+', new_line)
                print()
        # TODO Not a good way, have to open the file twice.
        with open(fields_path, 'w') as ori_xsd_w:
            ori_xsd_w.writelines(lines)


def get_class_dict(_package_root):
    _version = version.VERSION
    _path_to_edited_xsd = os.path.join(_package_root, 'SchemaCombined_v%s.xsd' % _version)

    # build txns dict
    txns_dict = dict()
    used_type_dict = dict()
    abs_class_dict = dict()
    with open(_path_to_edited_xsd, 'r') as xsd_file:
        elem_complex_set = set()
        elem_complex_type_set = set()
        elem_ref_set = set()
        anonymous_type_dict = dict()
        lines = xsd_file.readlines()
        txns_head = re.compile('<xs:element name=\"(\w+)\"\s*substitutionGroup=\"xp:(\w+)\".*>')
        elem_complex = re.compile('<xs:element\s*name=\"(\w+)\"\s*type=\"xp:(\w+)\".*\/>')
        elem_ref = re.compile('<xs:element.*ref="xp:(\w+)".*/>')
        element_head = re.compile('<xs:element\s*name=\"(\w+)\".*>')
        lines_index = -1
        for line in lines:
            lines_index += 1
            found_txns_head = txns_head.search(line)
            if found_txns_head:
                _name = found_txns_head.group(1).strip()
                _type = found_txns_head.group(2).strip()
                if _type == 'transaction' or _type == 'recurringTransaction':
                    txns_dict[_name] = dict()
                elif 'Response' not in _type:
                    if _type not in abs_class_dict:
                        abs_class_dict[_type] = []
                    abs_class_dict[_type].append(_name)
            found_elem_complex = elem_complex.search(line)
            if found_elem_complex:
                elem_complex_set.add(found_elem_complex.group(1).strip())
                elem_complex_type_set.add(found_elem_complex.group(2).strip())
            found_elem_ref = elem_ref.search(line)
            if found_elem_ref:
                elem_ref_set.add(found_elem_ref.group(1).strip())
            found_element_head = element_head.search(line)
            if found_element_head and re.search('<xs:complexType>', lines[lines_index + 1]):
                _name = found_element_head.group(1).strip()
                try:
                    obj = getattr(fields, _name)()
                    type_name = type(obj).__name__
                    anonymous_type_dict[type_name] = _name
                except:
                    pass

        # dir() not attributes
        no_attr_list = ['Factory', 'append', 'content', 'extend', 'orderedContent', 'reset', 'toDOM', 'toxml',
                        'validateBinding', 'value', 'wildcardAttributeMap', 'wildcardElements', 'xsdConstraintsOK']
        used_types = set()
        for k in txns_dict:
            obj = getattr(fields, k)()
            attrs = dir(obj)
            for attr_name in attrs:
                if attr_name[0] != '_' and attr_name not in no_attr_list:
                    if attr_name in elem_ref_set:
                        txns_dict[k][attr_name] = attr_name
                        used_types.add(attr_name)
                        continue
                    elif attr_name in elem_complex_set:
                        _type_name = _find_types(lines, k, attr_name)
                        txns_dict[k][attr_name] = _type_name
                        if _type_name:
                            used_types.add(_type_name)
                        continue
                    else:
                        txns_dict[k][attr_name] = ''

        for k in abs_class_dict:
            for _name in abs_class_dict[k]:
                used_types.add(_name)

        while used_types:
            k = used_types.pop()
            if k not in used_type_dict and k not in abs_class_dict:
                used_type_dict[k] = dict()
                obj = getattr(fields, k)()
                if type(obj).__dict__['__module__'] == 'vantivsdk.fields':
                    attrs = dir(obj)
                    for attr_name in attrs:
                        if attr_name[0] != '_' and attr_name not in no_attr_list:
                            if attr_name in elem_ref_set:
                                used_type_dict[k][attr_name] = attr_name
                                used_types.add(attr_name)
                                continue
                            elif attr_name in elem_complex_set:
                                if k in elem_complex_type_set:
                                    _type_name = _find_types(lines, k, attr_name, True)
                                else:
                                    _type_name = _find_types(lines, k, attr_name)
                                used_type_dict[k][attr_name] = _type_name
                                if _type_name:
                                    used_types.add(_type_name)
                                continue
                            else:
                                used_type_dict[k][attr_name] = ''

    return [txns_dict, used_type_dict, abs_class_dict]


def _find_types(lines, root_ele_name, ele_name, complexType=False):
    result = ''
    found_root = False
    root_ele = re.compile('<xs:element\s*name=\"%s\".*>' % root_ele_name)
    if complexType:
        root_ele = re.compile('<xs:complexType\s*name=\"%s\".*>' % root_ele_name)
    ele_head = re.compile('<xs:element\s*name=\"%s\"\s*type=\"xp:(\w+)\".*\/>' % ele_name)
    for line in lines:
        if not found_root:
            if root_ele.search(line):
                found_root = True
        else:
            found_ele_head = ele_head.search(line)
            if found_ele_head:
                result = found_ele_head.group(1).strip()
                break
    return result


def generate_index_rst(_package_root, _dict_list):
    _version = version.VERSION
    _index_rst_path = os.path.join(_package_root, 'docs/source/index.rst')
    # base string for index.rst
    index_rst_base = "Vantiv eCommerce Python SDKv2 documentation %s!\n" % _version
    index_rst_base += "%s" % '=' * len(index_rst_base)
    index_rst_base += '\n'
    index_rst_base += """
.. toctree::
   :maxdepth: 2
   :caption: Contents:

EXAMPLE
-------
Using dict
..........
.. code-block:: python
   :linenos:

    #Example for SDKv2
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

    #Example for SDKv2
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
"""

    txns_dict = _dict_list[0].copy()
    used_type_dict = _dict_list[1].copy()
    abs_class_dict = _dict_list[2].copy()

    # Sort class by name
    txns_list = list(txns_dict.keys())
    txns_list.sort()

    for txns in txns_list:
        index_rst_base += '%s\n%s\n' % (txns, '.' * len(txns))
        index_rst_base += '    .. py:class:: vantivsdk.fields.%s\n\n' % txns
        attr_list = list(txns_dict[txns].keys())
        attr_list.sort()

        for attr_name in attr_list:
            attr_tpye = txns_dict[txns][attr_name]
            if attr_tpye:
                if attr_tpye in abs_class_dict:
                    index_rst_base += '        :var %s: instance of ' % attr_name
                    for e in abs_class_dict[attr_tpye]:
                        index_rst_base += ':py:class:`vantivsdk.fields.%s`, ' % e
                    index_rst_base += '\n'
                else:
                    index_rst_base += '        :var %s: instance of :py:class:`vantivsdk.fields.%s`\n' \
                                      % (attr_name, attr_tpye)
            else:
                index_rst_base += '        :var %s: String or Number\n' % attr_name
        index_rst_base += '\n'
    index_rst_base += 'Complex Types\n-------------\n'

    used_type_list = list(used_type_dict.keys())
    used_type_list.sort()
    for used_type in used_type_list:
        index_rst_base += '%s\n%s\n' % (used_type, '.' * len(used_type))
        index_rst_base += '    .. py:class:: vantivsdk.fields.%s\n\n' % used_type
        attr_list = list(used_type_dict[used_type].keys())
        attr_list.sort()

        for attr_name in attr_list:
            attr_tpye = used_type_dict[used_type][attr_name]
            if attr_tpye:
                if attr_tpye in abs_class_dict:
                    index_rst_base += '        :var %s: instance of ' % attr_name
                    for e in abs_class_dict[attr_tpye]:
                        index_rst_base += ':py:class:`vantivsdk.fields.%s`, ' % e
                    index_rst_base += '\n'
                else:
                    index_rst_base += '        :var %s: instance of :py:class:`vantivsdk.fields.%s`\n' \
                                      % (attr_name, attr_tpye)
            else:
                index_rst_base += '        :var %s: String or Number\n' % attr_name
        index_rst_base += '\n'

    with open(_index_rst_path, 'w') as index_rst_file_w:
        index_rst_file_w.write(index_rst_base)


def generate_dictmap_py(_package_root, _dict_list):
    dictmap_path = os.path.join(_package_root, 'vantivsdk', 'dictmap.py')
    dictmap_content = """# -*- coding: utf-8 -*-l
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

# The following dict is automatically generated by tools/postGeneration.py, Please DO NOT manually change it.

"""
    dictmap_content += 'txns_dict = %s\n\n' % pprint.pformat(_dict_list[0], 0)
    dictmap_content += 'used_type_dict = %s\n\n' % pprint.pformat(_dict_list[1], 0)
    dictmap_content += 'abs_class_dict = %s\n' % _dict_list[2]

    with open(dictmap_path, 'w') as index_rst_file_w:
        index_rst_file_w.write(dictmap_content)


if __name__ == '__main__':
    remove_absolute_path(package_root)
    dict_list = get_class_dict(package_root)
    generate_dictmap_py(package_root, dict_list)
    generate_index_rst(package_root, dict_list)
