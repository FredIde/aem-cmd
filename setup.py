# coding: utf-8
from setuptools import setup

from acmd import __version__

classifiers = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development',

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2.7',
]

config = {
    'name': 'aem-cmd',
    'version': __version__,
    'description': 'AEM Command line tools',
    'long_description': 'A set of tools to administer an Adobe AEM content management installation from the command line.',
    'license': 'MIT',
    'author': 'Björn Skoglund',
    'author_email': 'bjorn.skoglund@icloud.com',
    'url': 'https://github.com/bjorns/aem-cmd',
    'download_url': 'https://github.com/bjorns/aem-cmd',
    'classifiers': classifiers,

    # Build specs
    'install_requires': ['requests', 'lxml'],
    'packages': ['acmd', 'acmd.tools'],
    'package_data': {'acmd': ['data/acmd.rc.template', 'data/acmd.bash_completion']},
    'scripts': ['bin/acmd']
}

setup(**config)
