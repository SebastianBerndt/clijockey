#!/usr/bin/env python
## Ref https://docs.python.org/2/distutils/introduction.html
## Ref https://the-hitchhikers-guide-to-packaging.readthedocs.org/en/latest/
## Ref http://www.ibm.com/developerworks/library/os-pythonpackaging/

"""
   Copyright 2016-2019 David Michael Pennington

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from setuptools import setup, find_packages
import sys
import os
CURRENT_PATH=os.path.join(os.path.dirname(__file__))
sys.path.insert(1,CURRENT_PATH)

def read(fname):
    # Dynamically generate setup(long_description)
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='clijockey',
      version='0.3.1',
      description='Automate ssh and telnet sessions to network devices',
      url='https://github.com/mpenning/clijockey/',
      author='David Michael Pennington',
      author_email='mike@pennington.net',
      license='Apache License 2.0',
      platforms='linux',
      keywords='',
      entry_points = "",
      long_description=read('README.rst'),
      include_package_data=True, # See MANIFEST.in for explicit rules
      packages=find_packages(),
      use_2to3=True,
      zip_safe=False,
      install_requires = ['backports.functools_lru_cache==1.2.1', 
          'pexpect', 'transitions', 'textfsm', 
          'netaddr', 'enum34', 'traitlets', 'arrow', 
          'colorama'],   # Package dependencies here
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Plugins',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Intended Audience :: Information Technology',
          'Intended Audience :: Telecommunications Industry',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Communications',
          'Topic :: Internet',
          'Topic :: System :: Networking',
          'Topic :: System :: Networking :: Monitoring',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
     )

