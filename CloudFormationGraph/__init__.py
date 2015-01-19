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

from graphviz import Digraph


class CloudFormationGraph():
    def __init__(self):
        self.stack = []
        self.graph = Digraph()

    def add_stack(self, stack):
        """ Add a parsed stack into the pile """
        # TODO: Support multiple stacsk, do self.push() etc
        self.stack = stack

    def build(self):
        """ Generate the graph
        In order to find the things that relate to one another, we expect your
        average template to be using `Ref()`  somewhere within each one of
        a resource entity.
        """
        if 'Parameters' in self.stack.keys():
            self.add_parameters()

        if 'Resources' in self.stack.keys():
            for resource in self.stack['Resources']:
                self.graph.node(resource, resource)
                references = self.get_reference(
                    self.stack['Resources'][resource])
                for ref in references:
                    self.graph.edge(resource, ref)

        return self.graph.source

    def add_parameters(self):
        """Add the parameters, this should be done before anything else"""
        for param in self.stack['Parameters']:
            self.graph.node(param, param)

    def get_reference(self, resource):
        """For a given resource, recurse and find any references to other
        resources or parameters.

        Lifted and shifted from http://stackoverflow.com/a/20254842
        """
        references = []
        for key, value in resource.iteritems():

            if key == 'Ref':
                references.append(value)

            elif isinstance(value, dict):
                results = self.get_reference(value)
                for result in results:
                    references.append(result)

            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        more_results = self.get_reference(item)
                        for another_result in more_results:
                            references.append(another_result)

        return references
