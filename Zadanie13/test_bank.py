import unittest
from bank import Bank

class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank(2000)
    def test_sum(self):
        self.assertEqual(self.bank.sum(100), 2100)
    def test_minus(self):
        self.assertEqual(self.bank.sum(-100), 1900)
    def test_error(self):
        self.assertEqual(self.bank.debt('test'), 'Błąd')

if __name__ == '__main__':
    unittest.main()