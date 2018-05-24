from setuptools import find_packages, setup

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

print readme

setup(
    name = 'alphabet',
    version = '0.0.4',
    description = 'A string class enhancement',
    long_description = readme,
    #license = license,
    packages=find_packages(exclude=('tests', 'docs')),
    author = 'Roberto Reale',
    author_email = 'rober.reale@gmail.com',
    url = 'https://github.com/robertoreale/alphabet',
    keywords = [ ],
    install_requires = [ 'googletrans', 'filemagic', 'pygments', ],
    test_suite = 'nose.collector',
    tests_require = ['nose'],
)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
