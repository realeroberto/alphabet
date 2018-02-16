# alphabet

[![PyPI](https://img.shields.io/pypi/v/alphabet.svg)](https://pypi.python.org/pypi/alphabet)

`alphabet` is a Python string class enhancement.

## Install

Just do

```
pip install alphabet
```

## Example

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
