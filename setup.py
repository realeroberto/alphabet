from setuptools import setup

setup(
    name = 'alphabet',
    version = '0.0.3',
    description = 'A string class enhancement',
    packages = [ 'alphabet' ],
    author = 'Roberto Reale',
    author_email = 'rober.reale@gmail.com',
    url = 'https://github.com/robertoreale/alphabet',
    keywords = [ ],
    install_requires = [ 'googletrans', 'filemagic', 'pygments', ],
    test_suite = 'nose.collector',
    tests_require = ['nose'],
)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
