========
alphabet
========

.. image:: https://img.shields.io/pypi/v/alphabet.svg
   :alt: PyPI


``alphabet`` uses various methods to recognize text.

Installation
------------

The easiest way to install the package is via ``pip``::

    $ pip install alphabet

Usage
-----

**Obfuscation**

.. code:: python

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

**Identify a string**

.. code:: python

    from alphabet import alphabet
    
    alphabet('%!').identify()
    > 'PostScript document text'
    
    alphabet('import os').identify()
    > 'Python'
    
    alphabet('<div>foobar</div>').identify()
    > 'XML'
    
    alphabet('Привет').identify()
    > 'ru'
