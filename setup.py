#!/usr/bin/env python
"""
Setup script
"""

from setuptools import setup

setup(
    name='rfpkgdb-cli',
    description='A command line tool to access the Rpmfusion Package Database.',
    version='2.15.0',
    license='GPLv2+',
    download_url='https://github.com/rpmfusion-infra/rfpkgdb-cli',
    url='https://github.com/rpmfusion-infra/rfpkgdb-cli',
    author='Pierre-Yves Chibon',
    author_email='pingou@pingoured.fr',
    maintainer='RPMFusion rfpkgdb-cli Maintainers',
    maintainer_email='rfpkgdb-cli-maint@rpmfusion.org',
    packages=['rfpkgdb2client'],
    entry_points={
        'console_scripts': [
            "rfpkgdb-cli=rfpkgdb2client.cli:main",
            "rfpkgdb-admin=rfpkgdb2client.admin:main",
        ]
    },
    install_requires=[
        'requests', 'python-bugzilla', 'python-fedora', 'setuptools', 'six',
        'beautifulsoup4'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later '
        '(GPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
    ],
)
