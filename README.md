# python-gettext-demo
Minimal example of python gettext in an application, including packaging and language switching at runtime.

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

Project structure:
```
python-gettext-demo/
|-- a/
|   |-- __init__.py
|   |-- b.py
|   |-- c.py
|   |-- interface.py
|   |-- locales/
|       |-- ll/
|           |-- LC_MESSAGES
|               |-- messages.mo
|               |-- messages.po
|-- pyproject.toml
|-- setup.py
```
