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

import datetime
import os

import paramiko
import six
import xmltodict

from . import (fields, utils, batch_txns, dict2obj, pgp_helper)

# Key: transaction name
# Value: array of batchRequest attributes according to transactions
_supported_transaction_types = batch_txns.supported_transaction_types

_batch_attributes_num_dict = dict()
_batch_attributes_amount_dict = dict()
for key in _supported_transaction_types:
    if _supported_transaction_types[key][0]:
        _batch_attributes_num_dict[_supported_transaction_types[key][0]] = 0
    if _supported_transaction_types[key][1]:
        _batch_attributes_amount_dict[_supported_transaction_types[key][1]] = 0

_class_transaction_dict = dict()
for key in _supported_transaction_types:
    obj = getattr(fields, key)()
    type_name = type(obj).__name__
    _class_transaction_dict[type_name] = _supported_transaction_types[key]


def submit(transactions, conf, filename='', timeout=60):
    """Submitting a Session File for Processing to server via sFTP

    1. Generate cnpRequest xml.
    2. Save xml at local file system.
    3. Send xml file to server.

    Args:
        transactions: an instance of batch.Transactions.
        conf: An instance of utils.Configuration.
        filename: String. File name for generated xml file. If the file exist, a timestamp string will be added.
        timeout: Positive int. Timeout in second for ssh connection for sftp.

    Returns:
        filename of file in inbound folder at remote server with '.asc' as extension.

    Raises:
        Exception depends on when get it.
    """
    if isinstance(transactions, dict):
        transactions = _to_batch_txns(transactions)

    if not isinstance(transactions, Transactions):
        raise utils.VantivException('transactions must be an instance of batch.Transactions')

    if len(transactions.transactions) < 1:
        raise utils.VantivException('transactions must have at least 1 transaction')

    if not isinstance(conf, utils.Configuration):
        raise utils.VantivException('conf must be an instance of utils.Configuration')

    if not isinstance(filename, six.string_types):
        raise utils.VantivException('filename must be a string')

    if not isinstance(timeout, six.integer_types) or timeout < 0:
        raise utils.VantivException('timeout must be an positive int')

    # 1. Generate cnpRequest xml.
    xml_str = _create_batch_xml(transactions, conf)

    # 2. Save xml at local file system.
    file_path = _save_str_file(xml_str, conf.batch_requests_path, filename)

    # 3. Send xml file to server.
    remote_filename = _put_file_to_sftp(file_path, conf, timeout)
    return remote_filename


def download(filename, conf, delete_remote=False, timeout=60):
    """Download Processed Session File from server via sFTP

    Get xml file from server and save to local file system

    Args:
        filename: filename of file in outbound folder at remote server with '.asc' as extension.
        conf:  An instance of utils.Configuration.
        delete_remote: If delete the remote file after download. The default is False
        timeout: Timeout in second for ssh connection for sftp.

    Returns:
        path for file that saved in local file system.

    Raises:
        Exception depends on when get it.
    """
    if not isinstance(conf, utils.Configuration):
        raise utils.VantivException('conf must be an instance of utils.Configuration')

    if not isinstance(filename, six.string_types) or len(filename) < 4:
        raise utils.VantivException('filename must be a string, and at least 4 chars')

    if not isinstance(timeout, six.integer_types) or timeout < 0:
        raise utils.VantivException('timeout must be an positive int')

    return _get_file_from_sftp(filename, conf, delete_remote, timeout)


def retrieve(filename, conf, return_format='dict', save_to_local=False, delete_remote=False, timeout=60):
    """Retrieving Processed Session File from server via sFTP

    1. Get xml file string from server and return object
    2. If save_to_local, save to local file system

    Args:
        filename: filename of file in outbound folder at remote server with '.asc' as extension.
        conf:  An instance of utils.Configuration.
        return_format: Return format. The default is ‘dict’. Could be one of ‘dict’, ‘object’ or ‘xml’.
        save_to_local: whether save file to local. default is false.
        delete_remote: If delete the remote file after download. The default is False
        timeout: Timeout in second for ssh connection for sftp.

    Returns:
        response XML in desired format.

    Raises:
        Exception depends on when get it.
    """
    if not isinstance(conf, utils.Configuration):
        raise utils.VantivException('conf must be an instance of utils.Configuration')

    if not isinstance(filename, six.string_types) or len(filename) < 4:
        raise utils.VantivException('filename must be a string, and at least 4 chars')

    if not isinstance(timeout, six.integer_types) or timeout < 0:
        raise utils.VantivException('timeout must be an positive int')

    response_xml = _get_file_str_from_sftp(filename, conf, delete_remote, timeout)

    if save_to_local:
        _save_str_file(response_xml, conf.batch_response_path, filename)

    return _generate_response(response_xml, return_format, conf)

def _generate_response(_response_xml, _return_format, conf):
    response_dict = xmltodict.parse(_response_xml)['cnpResponse']
    if response_dict['@response'] == '0':
        return_f_l = _return_format.lower()
        if return_f_l == 'xml':
            return _response_xml
        elif return_f_l == 'object':
            return fields.CreateFromDocument(_response_xml)
        else:
            if conf.print_xml:
                import json
                print('Response Dict:\n', json.dumps(response_dict, indent=4), '\n\n')
            return response_dict
    else:
        raise utils.VantivException(response_dict['@message'])

def _put_file_to_sftp(file_path, conf, timeout):
    """Upload file to server via sftp.

    Args:
        file_path: local file path
        conf: An instance of utils.Configuration.
        timeout: Timeout in second for ssh connection for sftp.

    Returns:
        filename of file in inbound folder at remote server with '.asc' as extension.
    """
    # Check if the file should be encrypted.
    if conf.useEncryption:
        crypto = pgp_helper.PgpHelper()
        crypto.encryptFileSameName(conf.vantivPublicKeyID, file_path)


    basename = os.path.basename(file_path)
    remote_path_prg = 'inbound/%s.prg' % basename
    remote_path_asc = 'inbound/%s.asc' % basename

    transport = ''
    try:
        transport = paramiko.Transport((conf.sftp_url, 22))
        transport.connect(username=conf.sftp_username, password=conf.sftp_password)
        channel = transport.open_session()
        channel.settimeout(timeout)
        sftp = paramiko.SFTPClient.from_transport(transport)
        while __check_file_exist_in_sftp(sftp, remote_path_prg) or __check_file_exist_in_sftp(sftp, remote_path_asc):
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            remote_path_prg = 'inbound/%s_%s.prg' % (basename, timestamp)
            remote_path_asc = 'inbound/%s_%s.asc' % (basename, timestamp)
        sftp.put(file_path, remote_path_prg)
        sftp.rename(remote_path_prg, remote_path_asc)
        transport.close()
    except Exception:
        try:
            transport.close()
        except:
            pass
        raise utils.VantivException('Fail to send "%s" to Vantiv server.' % file_path)

    return os.path.basename(remote_path_asc)


def _get_file_from_sftp(filename, conf, delete_remote, timeout):
    """Download file from server via sftp

    Args:
        filename: filename in outbound folder
        conf: An instance of utils.Configuration.
        delete_remote: If delete the remote file after download.
        timeout: Timeout in second for ssh connection for sftp.

    Returns:
        path for file that saved in local file system.
    """
    if not os.path.exists(conf.batch_response_path):
        os.makedirs(conf.batch_response_path)
    local_path = os.path.join(conf.batch_response_path, filename)

    remote_path_asc = 'outbound/' + filename

    transport = ''
    try:
        transport = paramiko.Transport((conf.sftp_url, 22))
        transport.connect(username=conf.sftp_username, password=conf.sftp_password)
        channel = transport.open_session()
        channel.settimeout(timeout)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.get(remote_path_asc, local_path)
        if delete_remote:
            sftp.remove(remote_path_asc)
        transport.close()

        print('Passed downloaded!')
        # Check if the file should be decrypted.
        if conf.useEncryption:
            crypto = pgp_helper.PgpHelper()
            crypto.decryptFile(conf.gpgPassphrase, local_path, local_path)
            print('Passed decryption!')

    except Exception as ex:
        try:
            transport.close()
        except:
            pass
        print(ex)
        raise utils.VantivException('Cannot find file "%s" on Vantiv server.' % filename)
    return local_path


def _get_file_str_from_sftp(filename, conf, delete_remote, timeout):
    """read file from server via sftp

    Args:
        filename: filename in outbound folder
        conf: An instance of utils.Configuration.
        delete_remote: If delete the remote file after download.
        timeout: Timeout in second for ssh connection for sftp.

    Returns:
        xml string
    """
    remote_path_asc = 'outbound/' + filename
    transport = ''
    try:
        transport = paramiko.Transport((conf.sftp_url, 22))
        transport.connect(username=conf.sftp_username, password=conf.sftp_password)
        channel = transport.open_session()
        channel.settimeout(timeout)
        sftp = paramiko.SFTPClient.from_transport(transport)
        remote_file = sftp.open(remote_path_asc)
        # If the merchant is using encryption, we got to download and decrypt
        # it so that the content is readable.
        return_str = ''
        if conf.useEncryption:
            # Download the content to a temporary file.
            tempFilename = 'pgp.vantiv'
            temp = open(tempFilename, 'wb')
            temp.write(remote_file.read())
            temp.close()
            crypto = pgp_helper.PgpHelper()
            # Decrypt the file.
            crypto.decryptFile(conf.gpgPassphrase, tempFilename, tempFilename)
            # Read the decrypted file.
            temp = open(tempFilename, 'rb')
            return_str = temp.read()
            temp.close()
            # Delete the temporary file.
            os.remove(tempFilename)
        else:
            return_str = remote_file.read()

        return_str = return_str.decode('utf-8')
        if delete_remote:
            sftp.remove(remote_path_asc)
        transport.close()
    except Exception as ex:
        try:
            transport.close()
        except:
            pass
        print(ex)
        raise utils.VantivException('Cannot find file "%s" on Vantiv server.' % filename)

    if conf.print_xml:
        print('Batch response file content: \n', return_str, '\n')

    return return_str


def __check_file_exist_in_sftp(sftp, path):
    """ Check if path exist in server via sftp

    Args:
        sftp: An instance of sftp connection
        path: file path on server

    Returns:
        boolean
    """
    try:
        sftp.stat(path)
        return True
    except IOError:
        return False


def _save_str_file(xml_str, path, filename):
    """Save string to local system

    Args:
        xml_str: String
        path: path for file to save
        filename: filename

    Returns:
        file path that saved
    """
    if not filename:
        filename = 'Vantiv_Batch_XML_%s' % datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    file_path = os.path.join(path, '%s.xml' % filename)
    if not os.path.exists(path):
        os.makedirs(path)
    while os.path.exists(file_path):
        file_path = os.path.join(path, '%s_%s.xml' % (filename, datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")))
    if six.PY2:
        with open(file_path, 'wb') as request_xml_file:
            request_xml_file.write(xml_str.encode('utf-8'))
    else:
        with open(file_path, 'w') as request_xml_file:
            request_xml_file.write(xml_str)
    return file_path


def _create_batch_xml(transactions, conf):
    """Create cnpRequest xml string

    Args:
        transactions: an instance of batch.Transactions.
        conf: An instance of utils.Configuration.

    Returns:
        cnpRequest xml string
    """

    authentication = fields.authentication()
    authentication.user = conf.user
    authentication.password = conf.password

    txns = transactions.transactions
    rtxns = transactions.recurringTransactions

    cnp_request = fields.cnpRequest()
    batch_request_list = list()
    transaction_list_for_batch_request = list()

    if transactions.is_rfr_request:
        # Using obj
        cnp_request.RFRRequest = txns[0]
    else:
        attributes_num_dict = _batch_attributes_num_dict.copy()
        attributes_amount_dict = _batch_attributes_amount_dict.copy()
        for txn in txns:
            # Add default reportGroup to txn
            if hasattr(txn, 'reportGroup') and not txn.reportGroup:
                txn.reportGroup = conf.reportGroup
            type_name = type(txn).__name__
            attributes_num_dict[_class_transaction_dict[type_name][0]] += 1
            if hasattr(txn, 'amount') and getattr(txn, 'amount') and _class_transaction_dict[type_name][1]:
                attributes_amount_dict[_class_transaction_dict[type_name][1]] += int(getattr(txn, 'amount'))
            # Using obj
            transaction_list_for_batch_request.append(txn)
            if len(transaction_list_for_batch_request) == 20000:
                batch_request = fields.batchRequest()
                if hasattr(batch_request, 'sameDayFunding'):
                    batch_request.sameDayFunding = transactions.sameDayFunding
                if hasattr(batch_request, 'merchantId'):
                    batch_request.merchantId = conf.merchantId
                for k in attributes_num_dict:
                    if attributes_num_dict[k]:
                        setattr(batch_request, k, attributes_num_dict[k])
                for k in attributes_amount_dict:
                    if attributes_amount_dict[k]:
                        setattr(batch_request, k, attributes_amount_dict[k])
                # clean attibutes dict
                attributes_num_dict = _batch_attributes_num_dict.copy()
                attributes_amount_dict = _batch_attributes_amount_dict.copy()
                # add to transaction
                batch_request.transaction = transaction_list_for_batch_request
                transaction_list_for_batch_request = list()
                batch_request_list.append(batch_request)
        if len(transaction_list_for_batch_request):
            batch_request = fields.batchRequest()
            if hasattr(batch_request, 'sameDayFunding'):
                batch_request.sameDayFunding = transactions.sameDayFunding
            if hasattr(batch_request, 'merchantId'):
                batch_request.merchantId = conf.merchantId
            for k in attributes_num_dict:
                if attributes_num_dict[k]:
                    setattr(batch_request, k, attributes_num_dict[k])
            for k in attributes_amount_dict:
                if attributes_amount_dict[k]:
                    setattr(batch_request, k, attributes_amount_dict[k])
            # clean attibutes dict
            attributes_num_dict = _batch_attributes_num_dict.copy()
            attributes_amount_dict = _batch_attributes_amount_dict.copy()
            batch_request.transaction = transaction_list_for_batch_request
            transaction_list_for_batch_request = list()
            batch_request_list.append(batch_request)

        for txn in rtxns:
            # Add default reportGroup to txn
            if hasattr(txn, 'reportGroup') and not txn.reportGroup:
                txn.reportGroup = conf.reportGroup
            type_name = type(txn).__name__
            attributes_num_dict[_class_transaction_dict[type_name][0]] += 1
            if hasattr(txn, 'amount') and getattr(txn, 'amount') and _class_transaction_dict[type_name][1]:
                attributes_amount_dict[_class_transaction_dict[type_name][1]] += int(getattr(txn, 'amount'))
            # Using obj
            transaction_list_for_batch_request.append(txn)
            if len(transaction_list_for_batch_request) == 20000:
                batch_request = fields.batchRequest()
                if hasattr(batch_request, 'sameDayFunding'):
                    batch_request.sameDayFunding = transactions.sameDayFunding
                if hasattr(batch_request, 'merchantId'):
                    batch_request.merchantId = conf.merchantId
                for k in attributes_num_dict:
                    if attributes_num_dict[k]:
                        setattr(batch_request, k, attributes_num_dict[k])
                for k in attributes_amount_dict:
                    if attributes_amount_dict[k]:
                        setattr(batch_request, k, attributes_amount_dict[k])
                # clean attibutes dict
                attributes_num_dict = _batch_attributes_num_dict.copy()
                attributes_amount_dict = _batch_attributes_amount_dict.copy()
                # add to transaction
                batch_request.recurringTransaction = transaction_list_for_batch_request
                transaction_list_for_batch_request = list()
                batch_request_list.append(batch_request)
        if len(transaction_list_for_batch_request):
            batch_request = fields.batchRequest()
            if hasattr(batch_request, 'sameDayFunding'):
                batch_request.sameDayFunding = transactions.sameDayFunding
            if hasattr(batch_request, 'merchantId'):
                batch_request.merchantId = conf.merchantId
            for k in attributes_num_dict:
                if attributes_num_dict[k]:
                    setattr(batch_request, k, attributes_num_dict[k])
            for k in attributes_amount_dict:
                if attributes_amount_dict[k]:
                    setattr(batch_request, k, attributes_amount_dict[k])
            # clean attibutes dict
            batch_request.recurringTransaction = transaction_list_for_batch_request
            batch_request_list.append(batch_request)

        cnp_request.batchRequest = batch_request_list

    cnp_request.version = conf.VERSION
    cnp_request.id = conf.id
    cnp_request.numBatchRequests = len(batch_request_list)
    cnp_request.authentication = authentication

    batch_xml = utils.obj_to_xml(cnp_request).decode('utf-8')

    if conf.print_xml:
        print('Batch request XML Obj:\n', batch_xml, '\n')

    return batch_xml


def _to_batch_txns(txns_dict):
    if not isinstance(txns_dict, dict):
        raise utils.VantivException('"%s" is not a dict' % txns_dict)

    txns = Transactions()

    for k in txns_dict:
        if k in batch_txns.supported_transaction_types or k == 'RFRRequest':
            if isinstance(txns_dict[k], list):
                for v in txns_dict[k]:
                    txn = dict2obj.tofileds({k:v})
                    txns.add(txn)
            else:
                txn = dict2obj.tofileds({k: txns_dict[k]})
                txns.add(txn)
        elif k == 'sameDayFunding':
            if txns_dict[k]:
                txns.sameDayFunding = True
            else:
                txns.sameDayFunding = False
        else:
            raise utils.VantivException('Transaction "%s" is not supported by batch' % k)

    return txns


class Transactions(object):
    """Container of transactions for batch request

    Then transactions could be RFRRequest and any batch request supported transactions and recurringTransaction.
    RFRRequest cannot exist in the same instance with any other transactions.

    A instance cannot contain more than 1,000,000 transactions.

    Attributes:
        sameDayFunding (bool): Since v11.1. Used for Dynamic Payout Funding Instructions only. Set to True to mark this Batch of Funding Instructions for same day funding.

    """

    sameDayFunding = False

    @property
    def is_rfr_request(self):
        """A property, whether current instanc include a RFRRequest

        Returns:
            Boolean
        """
        return self._RFRRequest

    @property
    def transactions(self):
        """A property, return a new list of transactions.

        Returns:
            list of transactions
        """
        # The purpose to do this is to avoid giving directly access to _transactions
        return list(self._transactions)

    @property
    def recurringTransactions(self):
        """A property, return a new list of recurringTransactions.

        Returns:
            list of recurringTransactions
        """
        # The purpose to do this is to avoid giving directly access to _recurringTransactions
        return list(self._recurringTransactions)

    def __init__(self):
        self._RFRRequest = False
        self._transactions = set()
        self._recurringTransactions = set()
        self.sameDayFunding = False
        obje = getattr(fields, 'RFRRequest')()
        self._RFRRequest_cls_name = type(obje).__name__

    def add(self, transaction):
        """Add transaction to the container class.

        Args:
            transaction: an instance of Transactions or RFRRequest which could process by Batch.

        Returns:
            None

        Raises:
            Exceptions.
        """
        # A Batch should not exceed 1,000,000 transactions.
        if (len(self._transactions) + len(self._recurringTransactions)) > 1000000:
            raise utils.VantivException('A session should not exceed 1,000,000 transactions.')

        if isinstance(transaction, dict):
            transaction = dict2obj.tofileds(transaction)

        type_name = type(transaction).__name__

        if self._RFRRequest_cls_name == type_name:
            if self._RFRRequest:
                raise utils.VantivException('only can add one RFRRequest')
            else:
                if not self._transactions:
                    self._transactions.add(transaction)
                    self._RFRRequest = True
                else:
                    raise utils.VantivException('cannot mix transactions and RFRRequest')
        else:
            if self._RFRRequest:
                raise utils.VantivException('cannot mix transactions and RFRRequest')
            if type_name in _class_transaction_dict:
                if isinstance(transaction, fields.transactionType) and transaction not in self._transactions:
                    # Add transaction
                    self._transactions.add(transaction)
                elif isinstance(transaction, fields.recurringTransactionType) and \
                                transaction not in self._recurringTransactions:
                    self._recurringTransactions.add(transaction)
                else:
                    raise utils.VantivException('duplicate transaction cannot be added to a batch')
            else:
                raise utils.VantivException('transaction not support by batch')
