CloudFormationGraph
===================
This tooling generates a visual representation of AWS CloudFormation templates
and outputs them into Graphviz's DOT syntax. If you have the Graphviz tooling
installed this can be then stylised, converted into SVG/PostScript etc.

Requirements
------------
* Python 2
* graphviz module.

Installation
------------
Since I'm too lazy to push this onto pypi, for now at least you'll have to
install it directly::

    pip install graphviz
    pip install git+http://github.com/tigertoes/CloudFormationGraph

cfd
---
cfd is the command-line tool for converting. Assuming your template lives in a
file somewhere on disk::

    cfd --in=stack.json --out=stack.dot

CloudFormationGraph
-------------------
CloudFormationGraph is the API which you can use programmatically::

    from CloudFormationGraph import CloudFormationGraph

    cfg = CloudFormationGraph()
    cfg.add_stack(open('stack.json', 'r').read())
    # To get the raw graphviz in DOT format:
    dot = cfg.build()
    # or after calling .build(), you can fetch the graphviz object:
    graph = cfg.graph

This API might be useful, particulary if you use tools like troposphere to
generate your templates.

TODO
----
* Fix the API and standarise things
* Supporting having multiple stacks generated into a single output (subgraphs)

License
-------

Copyright 2015 CloudFormationGraph authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
