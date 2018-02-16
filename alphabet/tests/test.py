from unittest import TestCase

from alphabet import alphabet

class Test(TestCase):
    def test(self):
        key = "foobar"
        s = alphabet.alphabet("python")
        t = s.obfuscate(key).obfuscate(key)
        self.assertTrue(s == t)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
