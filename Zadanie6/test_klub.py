import unittest
from klub import Club

class TestTrener(unittest.TestCase):
    def setUp(self):
        self.daneTrener = Club("Bayern")
    def test_isTrainer(self):
        result = self.daneTrener.isTrainer()
        self.assertEqual(result, False)
    def tearDown(self):
        self.daneTrener = None
        print("Dane wyczyszczone")

if __name__ == '__main__':  
    unittest.main()  