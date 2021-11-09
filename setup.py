import os
import subprocess
from setuptools import setup

# compile human-readable PO message catalogs into the
# machine-readable MO message catalogs used by gettext
# the MO files are included as package data
locale_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'a/locales'))
for locale in os.listdir(locale_dir):
    subprocess.run([
        'pybabel',
        'compile',
        '--input-file', f'{locale_dir}/{locale}/LC_MESSAGES/messages.po',
        '--output-file', f'{locale_dir}/{locale}/LC_MESSAGES/messages.mo'])

setup(
    name='a',
    version='0.1',
    packages=['a'],
    package_data={
        # include the compiled MO files in the package
        'a': ['locales/*/LC_MESSAGES/messages.mo']
    },
    entry_points={
        # create a command-line entrypoint
        'console_scripts': [
            'demo_gettext = a.interface:main'
        ],
    }
)
