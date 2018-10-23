#!/usr/bin/env python

from setuptools import setup

exec(open("erc20token/version.py").read())

with open('requirements.txt') as f:
    requires = [line.strip() for line in f if line.strip()]
with open('requirements-dev.txt') as f:
    tests_requires = [line.strip() for line in f if line.strip()]

setup(
    name='erc20token-python',
    version=__version__,
    description='ERC20 token SDK for Python',
    author='imperchik',
    author_email='imperchik@gmail.com',
    maintainer='imperchik',
    maintainer_email='imperchik@gmail.com',
    url='https://github.com/growlot/erc20token-sdk-python',
    license='GPLv2',
    packages=["erc20token-python"],
    long_description=open("README.md").read(),
    keywords=["ethereum", "erc20", "blockchain", "cryptocurrency"],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    install_requires=requires,
    tests_require=tests_requires,
    python_requires='>=3.6.6',
)
