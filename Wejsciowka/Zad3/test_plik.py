import unittest
from plik import Plik

class TestPlik(unittest.TestCase):

    def setUp(self):
        self.plik = Plik()
    def test_stworzPlik(self):
        plik = self.plik.stworzPlik()
        otwartyPlik = open("plik.txt")
        temp = otwartyPlik.readlines()
        print(temp)
        tablica = []
        
        for i in temp:
            record = i.strip()
            tablica.append(record)
            

        tablica.pop(0)
        tablica.insert(2,"5|")

        nowyPlik = open("plik2.txt","w+")
        nowyPlik.write(f"{tablica[0], tablica[1], tablica[2], tablica[3]}")
        nowyPlik.close()

        print(tablica)
        self.assertEqual(tablica[0],"2|Pogon Szczecin|Kosta")
        self.assertEqual(tablica[2],"5|")


if __name__ == '__main__':  
    unittest.main()  