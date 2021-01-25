from setuptools import find_packages, setup

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name = 'alphabet',
    version = '0.0.8',
    description = 'Uses various methods to recognize text',
    long_description = readme,
    #license = license,
    packages=find_packages(exclude=('tests', 'docs')),
    author = 'Roberto Reale',
    author_email = 'roberto@reale.me',
    url = 'https://github.com/reale/alphabet',
    keywords = [ ],
    install_requires = [ 'googletrans', 'filemagic', 'pygments', ],
    test_suite = 'nose.collector',
    tests_require = ['nose'],
)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
