#Unitesting
import unittest


class TestStringMethods(unittest.TestCase):


    def test_equal(self):
        self.assertEqual('kulwinder'.upper(), 'KULWINDER')

    def test_notequal(self):
        self.assertNotEqual('Singh','SINGH')

    def test_truefalse(self):
        self.assertTrue('KULWINDER'.isupper())
        self.assertFalse('kulwinder'.isupper())

    def test_Greater(self):
        self.assertGreater(7,4)

    def test_less(self):
        self.assertLess(3,21)

