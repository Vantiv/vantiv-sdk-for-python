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
from __future__ import absolute_import, print_function, unicode_literals

import requests
import xmltodict
import six

from . import (fields, utils, dict2obj)


def request(transaction, conf, return_format='dict', timeout=30, sameDayFunding = False):
    """Send request to server.

    Args:
        transaction: An instance of transaction class
        conf: An instance of utils.Configuration
        return_format: Return format. The default is 'dict'. Could be one of 'dict', 'object' or 'xml'.
        timeout: timeout for the request in seconds. timeout is not a time limit on the entire response. It's the time that server has not issued a response.
        sameDayFunding (bool): Start v11.3. Used for Online Dynamic Payout Funding Instructions only. Set to True for same day funding.

    Returns:
        response XML in desired format.

    Raises:
        VantivExceptions.
    """
    if isinstance(transaction, dict):
        transaction = dict2obj.tofileds(transaction)

    if not (isinstance(transaction, fields.recurringTransactionType)
            or isinstance(transaction, fields.transactionType)):
        raise utils.VantivException(
            'transaction must be either cnp_xml_fields.recurringTransactionType or transactionType')

    if not isinstance(conf, utils.Configuration):
        raise utils.VantivException('conf must be an instance of utils.Configuration')

    if not isinstance(timeout, six.integer_types) or timeout < 0:
        raise utils.VantivException('timeout must be an positive int')

    request_xml = _create_request_xml(transaction, conf, sameDayFunding)
    response_xml = _http_post(request_xml, conf, timeout)

    response_dict = xmltodict.parse(response_xml)['cnpOnlineResponse']

    if response_dict['@response'] == '0':
        return_f_l = return_format.lower()
        if return_f_l == 'xml':
            return response_xml
        elif return_f_l == 'object':
            return fields.CreateFromDocument(response_xml)
        else:
            # if conf.print_xml:
            #     import json
            #     print('Response Dict:\n', json.dumps(response_dict, indent=4), '\n\n')
            return response_dict
    else:
        raise utils.VantivException(response_dict['@message'])


def _create_request_xml(transaction, conf, same_day_funding):
    """Create xml string from transaction object

    Args:
        transaction: an instance of object, could be either recurringTransaction or transaction
        conf: an instance of utils.Configuration

    Returns:
        XML string
    """
    request_obj = _create_request_obj(transaction, conf, same_day_funding)
    request_xml = utils.obj_to_xml(request_obj)

    if conf.print_xml:
        print('Request XML:\n', request_xml.decode('utf-8'), '\n')

    return request_xml


def _create_request_obj(transaction, conf, same_day_funding):
    """ Create <xs:element name="cnpOnlineRequest">

    <xs:complexType name="baseRequest">
        <xs:sequence>
            <xs:element ref="xp:authentication" />
            <xs:choice>
                <xs:element ref="xp:transaction" />
                <xs:element ref="xp:recurringTransaction" />
            </xs:choice>
        </xs:sequence>
        <xs:attribute name="version" type="xp:versionType" use="required" />
    </xs:complexType>

    <xs:element name="cnpOnlineRequest">
        <xs:complexType>
            <xs:complexContent>
                <xs:extension base="xp:baseRequest">
                    <xs:attribute name="merchantId" type="xp:merchantIdentificationType" use="required" />
                    <xs:attribute name="merchantSdk" type="xs:string" use="optional" />
                    <xs:attribute name="loggedInUser" type="xs:string" use="optional"/>
                </xs:extension>
            </xs:complexContent>
        </xs:complexType>
    </xs:element>

    Args:
        transaction: an instance of object, could be either recurringTransaction or transaction
        conf: an instance of utils.Configuration

    Returns:
        an instance of cnpOnlineRequest object
    """
    request_obj = fields.cnpOnlineRequest()
    request_obj.merchantId = conf.merchantId
    request_obj.version = conf.VERSION
    request_obj.merchantSdk = conf.MERCHANTSDK

    if hasattr(request_obj, 'sameDayFunding') and same_day_funding:
        request_obj.sameDayFunding = same_day_funding

    authentication = fields.authentication()
    authentication.user = conf.user
    authentication.password = conf.password
    request_obj.authentication = authentication
    if hasattr(transaction, 'reportGroup') and not transaction.reportGroup:
        transaction.reportGroup = conf.reportGroup
    # determine option for choice.
    # <xs:choice>
    #     <xs:element ref="xp:transaction" />
    #     <xs:element ref="xp:recurringTransaction" />
    # </xs:choice>
    if isinstance(transaction, fields.recurringTransactionType):
        request_obj.recurringTransaction = transaction
    else:
        request_obj.transaction = transaction
    return request_obj


def _http_post(post_data, conf, timeout):
    """Post xml to server via https using requests

    Args:
        timeout:
        post_data: Request XML String
        conf: Instances of Configuration

    Returns:
        XML string for server response.

    Raise:
        VantivException
    """
    headers = {'Content-type': 'text/xml; charset=UTF-8'}
    proxies = {'https': conf.proxy} if (conf.proxy is not None and conf.proxy != '') else None
    try:
        response = requests.post(conf.url, data=post_data, headers=headers, proxies=proxies, timeout=timeout)
    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    if response.status_code != 200:
        raise utils.VantivException("Error with Https Response, Status code: ", response.status_code)

    # Check empty response
    if not response:
        raise utils.VantivException("The response is empty, Please call Vantiv eCommerce")

    if conf.print_xml:
        print('Response XML:\n', response.text, '\n')

    return response.text
