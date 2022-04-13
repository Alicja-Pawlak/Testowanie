import unittest
import bowling
from bowling import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game1 = Game([1,1,1])
        self.game2 = Game([10,6,3])
        self.game3 = Game([4,6,3])

    def test_sumPoints(self):
        result = self.game1.sumPoints()
        self.assertEqual(result,3)

    def test_firstStrike(self):
        result = self.game2.firstStrike()
        self.assertEqual(result,19)

    def test_spare(self):
        result = self.game3.spare()
        self.assertEqual(result,13)
        
    def tearDown(self):
        self.game1 = None
        self.game2 = None
        self.game3 = None

if __name__ == '__main__':  
    unittest.main()