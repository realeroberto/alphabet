from unittest import TestCase

from alphabet import alphabet

class TestAlphabet(TestCase):
    def test(self):

        key = "foobar"
        s = alphabet("python")
        t = s.obfuscate(key).obfuscate(key)
        self.assertTrue(s == t)

        s = alphabet("python")
        self.assertTrue(s.check("23eeeb4347bdd26bfc6b7ee9a3b755dd"))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
