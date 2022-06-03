from array import array
import unittest
import losowanie

class TestLos(unittest.TestCase):
    def test_losowanie(self):
        result = losowanie.wylosuj(5)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0]<result[1], True)
        self.assertEqual(result[2]<result[4], True)
if __name__ == '__main__':  
    unittest.main()  
