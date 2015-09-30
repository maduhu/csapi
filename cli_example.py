#!/usr/bin/env python

# Author: Will Stevens (CloudOps) - wstevens@cloudops.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Usage:
  cli_example.py [--json=<arg>] [--api_key=<arg> --secret_key=<arg>] [options]
  cli_example.py (-h | --help)

Options:
  -h --help                 Show this screen.
  --json=<arg>              Path to a JSON config file with the same names as the options (without the -- in front).
  --api_key=<arg>           CS Api Key.
  --secret_key=<arg>        CS Secret Key.
  --endpoint=<arg>          CS Endpoint [default: http://127.0.0.1:8080/client/api].
  --poll_interval=<arg>     Interval, in seconds, to check for a result on async jobs [default: 5].
  --logging=<arg>           Boolean to turn on or off logging [default: True].
  --log=<arg>               The log file to be used [default: logs/cs_api.log].
  --clear_log=<arg>         Removes the log each time the API object is created [default: True].
"""

from csapi import CLI
import pprint

if __name__ == '__main__':
    api = CLI(__doc__) # call the constructor with the __doc__ value...
    res = api.request({
        'command':'listAccounts'
    })
    pprint.pprint(res)
