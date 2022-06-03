import unittest
from vat import Osoba

class TestOsoba(unittest.TestCase):
    def setUp(self):
        self.daneOsoba = Osoba(200)
    def test_podatek(self):
        result = self.daneOsoba.podatek()
        self.assertEqual(result, 46)
    def test_netto(self):
        result = self.daneOsoba.netto()
        self.assertEqual(result, 154)
    def test_prog(self):
        result = self.daneOsoba.prog()
        self.assertEqual(result, "I prog")
    def tearDown(self):
        self.daneOsoba = None

if __name__ == '__main__':  
    unittest.main()  