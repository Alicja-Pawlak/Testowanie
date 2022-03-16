import unittest
import calculator

class TestCalc(unittest.TestCase):
    def test_dod(self):
        self.assertEqual(calculator.dod(3, 5), 8)
        self.assertEqual(calculator.dod(-1 ,2), 1)
    def test_odj(self):
        self.assertEqual(calculator.odj(1, 2), -1)
        self.assertEqual(calculator.odj(10, 5), 5)
    def test_mno(self):
        self.assertEqual(calculator.mno(1, 3), 3)
        self.assertEqual(calculator.mno(3, -2), -6)
    def test_dziel(self):
        self.assertEqual(calculator.dziel(3, 1), 3)
        self.assertEqual(calculator.dziel(4, -2), -2)
        with self.assertRaises(Exception) as exc:
            calculator.dziel(2,0)
    def test_pot(self):
        self.assertEqual(calculator.pot(2), 4)
        self.assertEqual(calculator.pot(-3), 9)
    def test_pier(self):
        self.assertEqual(calculator.pier(4), 2)
        self.assertEqual(calculator.pier(25), 5)
    def test_proc(self):
        self.assertEqual(calculator.proc(100,20), 20)
        self.assertEqual(calculator.proc(200,10), 20)

if __name__ == '__main__':  
    unittest.main()  
