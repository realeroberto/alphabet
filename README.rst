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
