import importlib

from a import b, install_language


def foo(): return _('foo')


while True:
    language = input('Enter your language: ')
    install_language(language)

    # translate by reloading dependencies in order
    from a import c
    importlib.reload(c)
    importlib.reload(b)

    # if the language is 'll', words will be 'translated' using the
    # translations in a/locales/ll/LC_MESSAGES/messages.mo
    # if any other value, it will fall back to 'foo bar baz'
    FOO_BAR_BAZ = f'{foo()} {b.BAR_BAZ}'
    print(f'foo bar baz in your language: {FOO_BAR_BAZ}')
