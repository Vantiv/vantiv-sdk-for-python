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
        fast_url (Str): Fast address, using for batch stream
        fast_port (Str): Fast port, using for batch stream
        print_xml (Str): Whether print request and response xml
    """
    VERSION = version.VERSION
    RELEASE = version.RELEASE
    MERCHANTSDK = 'Python SDKv2 ' + RELEASE
    _CONFIG_FILE_PATH = os.path.join(os.environ['VANTIV_SDK_CONFIG'], ".vantiv_python_sdk.conf") \
        if 'VANTIV_SDK_CONFIG' in os.environ else os.path.join(os.path.expanduser("~"), ".vantiv_python_sdk.conf")

    def __init__(self):

        self.user = ''
        self.password = ''
        self.merchantId = ''
        self.reportGroup = 'Default Report Group'
        self.url = 'https://www.testlitle.com/sandbox/communicator/online'
        self.proxy = ''
        self.sftp_username = ''
        self.sftp_password = ''
        self.sftp_url = ''
        self.batch_requests_path = os.path.join(tempfile.gettempdir(), 'vantiv_sdk_batch_request')
        self.batch_response_path = os.path.join(tempfile.gettempdir(), 'vantiv_sdk_batch_response')
        self.fast_url = ''
        self.fast_ssl = True
        self.fast_port = ''
        self.print_xml = False
        self.id = ''
        # Load Configuration from local file system.
        # noinspection PyBroadException
        try:
            with open(self._CONFIG_FILE_PATH, 'r') as config_file:
                config_json = json.load(config_file)
                self.user = config_json["user"] if "user" in config_json else ""
                self.password = config_json["password"] if "password" in config_json else ""
                self.merchantId = config_json["merchantId"] if "merchantId" in config_json else ""
                self.reportGroup = config_json["reportGroup"] if "reportGroup" in config_json else self.reportGroup
                self.url = config_json["url"] if "url" in config_json else self.url
                self.proxy = config_json["proxy"] if "proxy" in config_json else ""
                self.sftp_username = config_json["sftp_username"] if "sftp_username" in config_json else ""
                self.sftp_password = config_json["sftp_password"] if "sftp_password" in config_json else ""
                self.sftp_url = config_json["sftp_url"] if "sftp_url" in config_json else ""
                self.fast_url = config_json["fast_url"] if "fast_url" in config_json else ""
                self.fast_ssl = config_json["fast_ssl"] if "fast_ssl" in config_json else self.fast_ssl
                self.fast_port = config_json["fast_port"] if "fast_port" in config_json else ""
                self.print_xml = config_json["print_xml"] if "print_xml" in config_json else self.print_xml
                self.id = config_json["id"] if "id" in config_json else self.id
                self.batch_requests_path = config_json["batch_requests_path"] if "batch_requests_path" in config_json \
                    else self.batch_requests_path
                self.batch_response_path = config_json["batch_response_path"] if "batch_response_path" in config_json \
                    else self.batch_response_path
        except:
            # If get any exception just pass.
            pass

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
