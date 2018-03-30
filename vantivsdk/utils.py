# -*- coding: utf-8 -*-
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

from __future__ import absolute_import, print_function, unicode_literals

import json
import os
import tempfile

import pyxb

from . import version

class Configuration(object):
    """Setup Configuration variables.

    Attributes:
        user (Str): authentication.user
        password (Str): authentication.password
        merchantId (Str): The unique string to identify the merchant within the system.
        reportGroup (Str): To separate your transactions into different categories,
        url (Str): Url for server.
        proxy (Str): Https proxy server address. Must start with "https://"
        sftp_username (Str): Username for sftp
        sftp_password (Str): Password for sftp
        sftp_url (Str): Address for sftp
        batch_requests_path (Str): Location for saving generated batch request xml
        batch_response_path (Str): Location for saving batch response xml
        print_xml (Str): Whether print request and response xml
    """
    VERSION = version.VERSION
    RELEASE = version.RELEASE
    MERCHANTSDK = 'Python;' + RELEASE
    _CONFIG_FILE_PATH = os.path.join(os.environ['VANTIV_SDK_CONFIG'], ".vantiv_python_sdk.conf") \
        if 'VANTIV_SDK_CONFIG' in os.environ else os.path.join(os.path.expanduser("~"), ".vantiv_python_sdk.conf")

    def __init__(self, conf_dict = dict()):
        attr_dict = {
            'user':'',
            'password':'',
            'merchantId':'',
            'reportGroup':'Default Report Group',
            'url':'https://www.testvantivcnp.com/sandbox/new/sandbox/communicator/online',
            'proxy':'',
            'sftp_username':'',
            'sftp_password':'',
            'sftp_url':'',
            'batch_requests_path':os.path.join(tempfile.gettempdir(), 'vantiv_sdk_batch_request'),
            'batch_response_path':os.path.join(tempfile.gettempdir(), 'vantiv_sdk_batch_response'),
            'print_xml':False,
            'id':'',
            'vantivPublicKeyID':'',
            'gpgPassphrase':'',
            'merchantPublicKeyID':'',
            'useEncryption':'',
            'deleteBatchFiles':''
        }

        # set default values
        for k in attr_dict:
            setattr(self, k , attr_dict[k])

        # override valuse by loading saved conf
        try:
            with open(self._CONFIG_FILE_PATH, 'r') as config_file:
                config_json = json.load(config_file)
                for k in attr_dict:
                    if k in config_json and config_json[k]:
                        setattr(self, k, config_json[k])
        except:
            # If get any exception just pass.
            pass

        # override values by args
        if conf_dict:
            for k in conf_dict:
                if k in attr_dict:
                    setattr(self, k, conf_dict[k])

    def save(self):
        """Save Class Attributes to .vantiv_python_sdk.conf

        Returns:
            full path for configuration file.

        Raises:
            IOError: An error occurred
        """
        with open(self._CONFIG_FILE_PATH, 'w') as config_file:
            json.dump(vars(self), config_file)
        return self._CONFIG_FILE_PATH


def obj_to_xml(obj):
    """Convert object to xml string without namespaces

    Args:
        obj: Object

    Returns:
        Xml string

    Raises:
        pyxb.ValidationError
    """
    # TODO convert object to xml without default namespace gracefully.
    try:
        xml = obj.toxml('utf-8')
    except pyxb.ValidationError as e:
        raise VantivException(e.details())
    xml = xml.replace(b'ns1:', b'')
    xml = xml.replace(b':ns1', b'')
    return xml


class VantivException(Exception):
    pass
