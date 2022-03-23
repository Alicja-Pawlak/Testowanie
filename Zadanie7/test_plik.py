import unittest
from plik import Plik

class TestPlik(unittest.TestCase):
    def setUp(self):
        self.kluby = Plik("Bayern","Manchester City")
    def test_stworzPlik(self):

        plik = self.kluby.stworzPlik("Kluby")
        otwartyPlik = open("Kluby.txt")
        temp = otwartyPlik.readlines()
        print(temp)
        tablica = []
        
        for i in temp:
            club_name = i.strip()
            tablica.append(club_name)

        self.assertEqual(tablica[0],"Bayern")
        self.assertEqual(tablica[1],"Manchester City")

    #def tearDown(self):
     #   self.kluby = None
      #  print("Dane wyczyszczone")

if __name__ == '__main__':  
    unittest.main()  