import unittest
from portfel import Portfel

class TestPortfel(unittest.TestCase):
    def setUp(self):
        self.portfel = Portfel(200)
    def test_setInitialValue(self):
        self.portfel.setInitialValue(10)
        self.assertEqual(self.portfel.saldo, 10)
    def test_add(self):
        self.portfel.add(5)
        self.assertEqual(self.portfel.saldo, 205)
    def test_spend(self):
        self.portfel.spend(100)
        self.assertEqual(self.portfel.saldo, 100)
    def tearDown(self):
        self.portfel = 0

if __name__ == '__main__':  
    unittest.main()  