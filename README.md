# python-gettext-demo
Minimal example of python gettext in an application, including packaging and language switching at runtime.

Project structure:
```
python-gettext-demo/
|-- a/
|   |-- __init__.py              # installs languages
|   |-- b.py                     # module with translated strings
|   |-- c.py                     # module with translated strings
|   |-- interface.py             # entrypoint
|   |-- locales/                 # locale directory with structure that gettext expects
|       |-- ll/                  # translation data for language 'll'
|           |-- LC_MESSAGES      # gettext expects this directory to exist
|               |-- messages.po  # human-readable message catalog for language 'll'
|-- pyproject.toml               # tells pip to install babel before installing this package
|-- setup.py                     # includes message catalog in wheel distribution
```

## packaging

### wheel
```
$ git clone https://github.com/emlys/python-gettext-demo.git
$ cd python-gettext-demo
$ pip install .
$ demo_gettext
Enter your language: ll
foo bar baz in your language: fσσ вαя вαz
Enter your language: en
foo bar baz in your language: foo bar baz
```

### pyinstaller executable
```
$ git clone https://github.com/emlys/python-gettext-demo.git
$ cd python-gettext-demo
$ pyinstaller \   # include compiled message catalog in executable bundle
    --add-data \  # you can also add this data with a hook or spec file
    a/locales/ll/LC_MESSAGES/messages.mo:a/locales/ll/LC_MESSAGES \
    a/interface.py
$ dist/interface/interface
Enter your language: ll
foo bar baz in your language: fσσ вαя вαz
Enter your language: en
foo bar baz in your language: foo bar baz
```

## about language switching

The `_(...)` function translates strings. The definition of `_` depends on which language is installed: calling `gettext.install` updates the definition of `_`. So to translate to a language, you need to be sure that every use of `_` is evaluated after installing the desired language. 

If a program only needs to execute in one language per run (such as a command line tool that takes a `--language` argument) it's easy enough to guarantee this. Translated strings might be defined in places that complicate the order of execution. Module-level strings are evaluated at import time. Class attributes are evaluated when an object is instantiated. There's lots of ways that a translated string can get evaluated before the right language is installed. For a single language, you can rearrange things to guarantee the right evaluation order.

Switching between multiple languages during execution (like in a server module, or a loop like in this example) is tricky because there's no getting around having to re-evaluate the translated strings. Some options are: 
* use `importlib.reload` to re-evaluate module-level variables
* use lazy strings like [this one from Flask-Babel](https://github.com/python-babel/flask-babel/blob/cc56bd9a4e7f614a4c1bf65c7f8b50b859359832/flask_babel/speaklater.py#L1)
* define strings within functions

None of the options are perfect and you have to design around the constraint of controlling when strings are evaluated. See [this stackoverflow post](https://stackoverflow.com/questions/69906944/approaches-to-changing-language-at-runtime-with-python-gettext) for details.
