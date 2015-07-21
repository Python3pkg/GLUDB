# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gludb',
    version='0.1.0',
    description='A simple database wrapper',
    long_description=long_description,
    url='https://github.com/memphis-iis/GLUDB',
    author='University of Memphis Institute for Intelligent Systems',
    author_email='cnkelly@memphis.edu',
    license='Apache Version 2.0',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'Topic :: Database',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Archiving :: Backup',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='database versioning backup dynamodb bigtable mongodb',
    packages=['gludb'],

    install_requires=[],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': [],
        'test': ['coverage', 'nose'],
        'dynamodb': ['boto']
    },

    package_data={},
    data_files=[],
    entry_points={},
)
