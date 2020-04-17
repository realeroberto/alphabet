========
alphabet
========

.. image:: https://img.shields.io/pypi/v/alphabet.svg
   :alt: PyPI


``alphabet`` is a Python string class enhancement (a mixin).

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

**Checking against a hash to the basic string class**

 The hash can be automatically recognized.

.. code:: python

    from alphabet import alphabet

    s =  alphabet('the tragicall historye of romeus and juliet')

    len(s)
    > 43

    s.title()
    > 'The Tragicall Historye Of Romeus And Juliet'

    from hashlib import sha256
    print(s.get_algorithm(sha256(s.encode('utf-8')).hexdigest()))
    > 'sha256'

    print(s.check(sha256(s.encode('utf-8')).hexdigest()))
    > True
