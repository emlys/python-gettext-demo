from distutils.core import setup

setup(
    name='a',
    version='0.1',
    packages=['a',],
    package_data={
        'a': [
            'locales/ll/LC_MESSAGES/messages.mo'
        ]
    }
)
