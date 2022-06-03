import unittest
import obliczanie

class TestObl(unittest.TestCase):
    def test_obliczanie(self):
        self.assertEqual(obliczanie.nwd(5,15), 5)
        self.assertEqual(obliczanie.nww(5, 10), 10)
if __name__ == '__main__':  
    unittest.main()  
