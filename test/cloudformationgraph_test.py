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

import unittest
from CloudFormationGraph import CloudFormationGraph
from pprint import pprint


class CloudFormationGraphTest(unittest.TestCase):
    def setUp(self):
        self.cfg = CloudFormationGraph()


class AddParameterTest(CloudFormationGraphTest):
    def runTest(self):
        params = {
            'Parameters': {
                'TestParameter':{}
            }
        }
        expected_graph =  "digraph {\n\tTestParameter [label=TestParameter]\n}"
        self.cfg.add_stack(params)
        graph = self.cfg.build()
        self.assertEqual(self.cfg.graph.source, expected_graph)


class ResourceTraverseTest(CloudFormationGraphTest):
    def runTest(self):
        stack = {
            'Parameters':{
                'TestParameter': {
                    'Type': 'String'
                }
            },
            'Resources':{
                'TestResource':{
                    'AnotherDepth':{
                        'Ref': 'TestParameter'
                    }
                }
            }
        }
        self.cfg.add_stack(stack)
        refs = self.cfg.get_reference(stack['Resources'])
        self.assertItemsEqual(refs, ['TestParameter'])


class BuildGraphTest(CloudFormationGraphTest):
    def runTest(self):
        stack = {
            'Parameters':{
                'TestParameter': {
                    'Type': 'String'
                }
            },
            'Resources':{
                'TestResource':{
                    'AnotherDepth':{
                        'Ref': 'TestParameter'
                    }
                }
            }
        }
        self.cfg.add_stack(stack)
        self.cfg.build()
        expected = ("digraph {\n\tTestParameter [label=TestParameter]"
        "\n\tTestResource [label=TestResource]\n\t\tTestResource -> TestParameter\n}")
        self.assertEquals(self.cfg.graph.source, expected)
