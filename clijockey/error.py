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

class ConnectionFailedError(Exception):
    def __init__(self, *args, **kwargs):
        super(ConnectionFailedError, self).__init__(*args, **kwargs)

class AuthenticationFailedError(Exception):
    def __init__(self, *args, **kwargs):
        super(AuthenticationFailedError, self).__init__(*args, **kwargs)

class ResponseFailException(Exception):
    def __init__(self, *args, **kwargs):
        super(ResponseFailException, self).__init__(*args, **kwargs)

class ExecuteTimeout(Exception):
    def __init__(self, *args, **kwargs):
        super(ExecuteTimeout, self).__init__(*args, **kwargs)

class UnexpectedConnectionClose(Exception):
    def __init__(self, *args, **kwargs):
        super(UnexpectedConnectionClose, self).__init__(*args, **kwargs)

## TraitTable errors

class TraitTableInvalidInput(Exception):
    def __init__(self, *args, **kwargs):
        super(TraitTableInvalidInput, self).__init__(*args, **kwargs)

## TraitType errors

class InvalidVlanError(Exception):
    def __init__(self, *args, **kwargs):
        super(InvalidVlanError, self).__init__(*args, **kwargs)

class InvalidMacError(Exception):
    def __init__(self, *args, **kwargs):
        super(InvalidMacError, self).__init__(*args, **kwargs)

class InvalidIPv4AddressError(Exception):
    def __init__(self, *args, **kwargs):
        super(InvalidIPv4AddressError, self).__init__(*args, **kwargs)

class InvalidUnicodeRegex(Exception):
    def __init__(self, *args, **kwargs):
        super(InvalidUnicodeRegex, self).__init__(*args, **kwargs)
