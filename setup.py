from setuptools import setup

from CloudFormationGraph import version

setup(
    name='cloudformation-graph',
    version=version.VERSION,
    author='Tiger Toes',
    author_email='thatrascaltiger@gmail.com',
    license='Apache 2',
    install_requires=['graphviz'],
    setup_requires=['flake8'],
    packages=['CloudFormationGraph'],
    test_suite='test',
    entry_points={
        'console_scripts': ['cfd = CloudFormationGraph.cfd:main']
    }
)
