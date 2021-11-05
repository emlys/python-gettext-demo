# interface.py
import sys
from a import b, install_language

def foo(): return _('foo')

while True:
    language = input('Enter your language: ')
    install_language(language)

    # DO SOMETHING TO UPDATE c.DATA TO NEW LANGUAGE

    # each word should be translated to the chosen language
    FOO_BAR_BAZ = f'{foo()} {b.BAR_BAZ}'
    print(f'foo bar baz in your language: {FOO_BAR_BAZ}')
