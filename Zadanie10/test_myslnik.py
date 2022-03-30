import unittest
import myslnik

class TestMyslnik(unittest.TestCase):

    def setUp(self):
        self.addresses = "Alicja Pawlak"

    def test_if_myslnik(self):
        self.assertEqual(myslnik.if_myslnik(self.addresses),False)
    
if __name__ == '__main__':  
    unittest.main()  