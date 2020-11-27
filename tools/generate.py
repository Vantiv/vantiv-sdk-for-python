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

# IF YOU ARE RUNNING THIS ON THE ECOM VMS:
# BE SURE TO RUN IN YOUR VIRTUAL ENV!


from __future__ import absolute_import, division, print_function

import os
import sys

package_root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, package_root)
from vantivsdk import utils

version = utils.Configuration().VERSION
xsd_name = 'SchemaCombined_v%s.xsd' % version


# Run pregen
print('Generate %s' % xsd_name)
pre_gen_path = os.path.join(package_root, 'tools', 'preGeneration.py')
os.system('python %s' % pre_gen_path)

#
print('Generate module fields using xsdata')
xsd_abs_path = os.path.join(package_root, xsd_name)
old_fields_path = os.path.join(package_root, 'vantivsdk', 'fields.py')
new_fields_temp = 'fields'

os.system('xsdata generate --config %s/tools/fieldconf.xsdata.xml %s/SchemaCombined_v%s.xsd' % (package_root, package_root, version))
os.system('xsdata generate --config %s/tools/tempconf.xsdata.xml %s/SchemaCombined_v%s.xsd' % (package_root, package_root, version))

if __name__ == '__main__':
    with open("./names/__init__.py") as trueNames:
        trueNames.readline()
        with open("./classes/__init__.py") as trueClasses:
            with open("fields.py", "w") as fields:
                fields.write(trueClasses.readline().replace('classes', 'vantivsdk'))
                for line in trueClasses:
                    if not line.find(',') == -1:
                        aliased = '\t' + line.replace(',', '').strip() + ' as ' + trueNames.readline().strip(' ')
                        fields.write(aliased)
                    else:
                        fields.write(line)
                        break


print('Copy fields.py to package')
gen_field_py_abs_path = os.path.join(package_root,'tools', 'fields.py')
target_field_py_abs_path = os.path.join(package_root, 'vantivsdk', 'fields.py')
os.system('cp %s %s' % (gen_field_py_abs_path, target_field_py_abs_path))

gen_combined_abs_path = os.path.join(package_root,'tools', 'classes', 'SchemaCombined*')
target_combined_abs_path = os.path.join(package_root, 'vantivsdk', 'SchemaCombined*')
os.system('cp %s %s' % (gen_combined_abs_path, target_combined_abs_path))

# Run postgen
print('delete absolute path in field.py and gen docs rst')
post_gen_path = os.path.join(package_root, 'tools', 'postGeneration.py')
os.system('python %s' % post_gen_path)

docs_abs_path = os.path.join(package_root, 'docs')
makefile_abs_path = os.path.join(package_root, 'docs', 'Makefile')

print('Deleting artifacts of generation')
os.system('rm -rf %s.py' % new_fields_temp)
os.system('rm -rf names')
os.system('rm -rf classes')

# not work, have to go terminal
# print('Generate html docs')
# os.system('make -f %s -C %s clean' % (makefile_abs_path, docs_abs_path))
# os.system('make -f %s -C %s html' % (makefile_abs_path, docs_abs_path))
