#!/usr/bin/env python

# Copyright 2015 CloudFormationGraph authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import json
from argparse import ArgumentParser
from CloudFormationGraph import GraphvizGenerator


def main():
    parser = ArgumentParser()
    parser.add_argument('--in', dest='stack', required=True, metavar='FILE',
                        help='File containing CloudFormation template',
                        type=lambda x: valid_file(parser, x))
    parser.add_argument('--out', dest='out', default=None,
                        help='File path to write out to, defaults to STDOUT')
    args = parser.parse_args()
    gg = GraphvizGenerator()
    stack = json.load(args.stack)  # TODO: try/catch to deal with broken JSON
    gg.add_stack(stack)
    dot = gg.build()
    if args.out is None:
        print dot
    else:
        f = open(args.out, 'w')
        f.write(dot)
        f.close()


def valid_file(parser, filepath):
    """Open the file if it's valid, else throw a parser error"""
    if os.path.isfile(filepath):
        return open(filepath, 'r')
    else:
        parser.error("%s doesn't appear to be a valid file!" % file)


if __name__ == '__main__':
    main()
