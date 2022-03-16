import unittest
import temp

class TestTemp(unittest.TestCase):
    def test_C_to_K(self):
        self.assertEqual(temp.C_to_K(-6), 267.15)
        self.assertEqual(temp.C_to_K(8.5), 281.65)
    def test_C_to_F(self):
        self.assertEqual(temp.C_to_F(16), 60.8)
        self.assertEqual(temp.C_to_F(-4), 24.8)

if __name__ == '__main__':  
    unittest.main() 