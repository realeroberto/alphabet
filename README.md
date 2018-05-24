# alphabet

[![PyPI](https://img.shields.io/pypi/v/alphabet.svg)](https://pypi.python.org/pypi/alphabet)

`alphabet` is a Python string class enhancement.

## Install

Just do

```
pip3 install alphabet
```

## Example

### Obfuscate

```
from alphabet import alphabet

key = "foobar"
s = alphabet.alphabet("python")

print(s)
> python

t = s.obfuscate(key)
print(bytes(t, 'utf-8'))
> b'\x16\x16\x1b\n\x0e\x1c'

print(t.obfuscate(key))
> python
```

### Identify a string

```
from alphabet import alphabet

alphabet('%!').identify()
> 'PostScript document text'

alphabet('import os').identify()
> 'Python'

alphabet('<div>foobar</div>').identify()
> 'XML'

alphabet('Привет').identify()
> 'ru'
```
