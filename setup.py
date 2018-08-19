#!/usr/bin/python3

from distutils.core import setup

setup(
    name='cdi_cardinality',
    version='0.1.0',
    description='Command line tool to get cardinality from CSV files columns',
    author='Pedro',
    author_email='pedroghcode@gmail.com',
    url='https://github.com/plainas/tq',
    packages= ['cdi_cardinality'],
    scripts=['bin/cdi_cardinality'],
    install_requires=[]
)
