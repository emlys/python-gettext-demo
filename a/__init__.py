import builtins
import gettext
import os

LOCALE_DIR = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'locales')

# define the _() function if not already defined
# this will be executed when anything from package a is imported
# prevents a `NameError: name '_' is not defined` from happening
# before `install_language` is called
if not callable(getattr(builtins, '_', None)):
    def identity(x): return x
    builtins.__dict__['_'] = identity


def install_language(language_code):
    # globally install the _() function for the language
    language = gettext.translation(
        'messages',
        languages=[language_code],
        localedir=LOCALE_DIR,
        fallback=True)
    language.install()
