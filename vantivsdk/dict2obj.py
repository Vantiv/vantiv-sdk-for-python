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
from __future__ import unicode_literals

from . import dictmap,utils,fields

def tofileds(txn_dict):
    if not isinstance(txn_dict, dict):
        raise utils.VantivException('"%s" is not a dict' % txn_dict)

    if len(txn_dict) != 1:
        raise utils.VantivException('Dict must contain one and only one transaction.')

    txn_name = ''
    for k in txn_dict:
        txn_name = k
        break
    txn_attrs = txn_dict[txn_name]

    if txn_name not in dictmap.txns_dict:
        raise utils.VantivException('The transaction "%s" is not supported by the SDK.' % txn_name)

    txn_obj = getattr(fields, txn_name)()
    txn_obj = _obj_map_attributes(txn_obj, txn_name, dictmap.txns_dict[txn_name], txn_attrs)
    return txn_obj

def _obj_map_attributes(obj, obj_name, obj_attrs_type_dict, obj_attrs_values_dict):
    """recursionly map attributes

    Args:
        obj:
        obj_name:
        obj_attrs_type_dict:
        obj_attrs_values_dict:

    Returns:
        object

    Raises:
        utils.VantivException
    """
    if not obj_attrs_values_dict:
        return obj

    for attr_name in obj_attrs_values_dict:
        if attr_name not in obj_attrs_type_dict:
            raise utils.VantivException('"%s" does not include "%s"' % (obj_name, attr_name))

        attr_value = obj_attrs_values_dict[attr_name]
        attr_type = obj_attrs_type_dict[attr_name]

        if isinstance(attr_value, list):
            # <xs:element ref="xp:detailTax" minOccurs="0" maxOccurs="6" />
            # when the element has maxOccurs attributes, and bigger than 1. than the attr_value should be a list.
            _value_obj_list = list()
            for sv in attr_value:
                _obj_tmp = getattr(fields, attr_type)()
                _obj_tmp = _obj_map_attributes(_obj_tmp, attr_name, dictmap.used_type_dict[attr_name], sv)
                _value_obj_list.append(_obj_tmp)
            setattr(obj, attr_name, _value_obj_list)
        elif isinstance(attr_value, dict):
            # when attr_value is a dict, it means the element has complex type or it's a ref of some others.
            if attr_type in dictmap.abs_class_dict:
                # when attr_type is in abs_class_dict
                if len(attr_value) == 1:
                    # Must have and only have one sub group.
                    _abs_sub_classname = ''
                    for k in attr_value:
                        _abs_sub_classname = k
                    if _abs_sub_classname in dictmap.abs_class_dict[attr_type]:
                        # Check if the sub class belongs to the absolute elements
                        _obj_tmp = getattr(fields, _abs_sub_classname)()
                        _obj_tmp = _obj_map_attributes(_obj_tmp, _abs_sub_classname,
                                                       dictmap.used_type_dict[_abs_sub_classname],
                                                       attr_value[_abs_sub_classname])
                        setattr(obj, attr_name, _obj_tmp)
                    else:
                        raise utils.VantivException('"%s" is not sub group of "%s"' % (_abs_sub_classname, attr_name))
                else:
                    raise utils.VantivException('The value of "%s" must be one key dict.' % attr_name)
            elif attr_type in dictmap.used_type_dict:
                # when attr_type is in used_type_dict
                _obj_tmp = getattr(fields, attr_type)()
                _obj_tmp = _obj_map_attributes(_obj_tmp, attr_name, dictmap.used_type_dict[attr_type], attr_value)
                setattr(obj, attr_name, _obj_tmp)
            else:
                # obj didn't have this attribute
                raise utils.VantivException('"%s" cannot set to the attribute "%s" of object "%s"' %
                                            (attr_value, attr_name, obj_name))
        else:
            # when attr_value is str or number
            if attr_type:
                # obj didn't have this attribute
                raise utils.VantivException('"%s" cannot set to the attribute "%s" of object "%s"' %
                                            (attr_value, attr_name, obj_name))
            else:
                setattr(obj, attr_name, attr_value)
    return obj