#!/usr/bin/env python
from setuptools import find_packages, setup

from __version__ import VERSION

readme = open("README.md").read()

required = [
    "urllib3"
]

extras = {
    'dev': [
        "erppeek",
        "environs",
        "isort",
        "autoflake",
    ],
    "tests": ["pytest", ]
}

setup(
	name = "pool_transport",
	version = VERSION,
	description = "Concurrent xmlrpc requests",
	author = "Som Energia SCCL",
	author_email = "info@somenergia.coop",
	url = 'https://github.com/Som-Energia/pool_transport',
	long_description = readme,
    long_description_content_type='text/markdown',
	license = 'GNU Affero General Public License v3 or later (AGPLv3+)',
	packages=find_packages(exclude=['*[tT]est*']),
	python_requires="!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
    zip_safe=True,
    setup_requires=[],
    install_requires=required,
    extras_require=extras,
    scripts=[],
	include_package_data = True,
	test_suite = 'nosetests',
	classifiers = [
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Intended Audience :: Developers',
		'Development Status :: 2 - Pre-Alpha',
		'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
		'Operating System :: OS Independent',
	],
)

