import unittest
import artDB
import os

class TestDB(unittest.TestCase):

    def setUp(self):
        artDB.create_database()

    def tearDown(self):
        os.remove("mydatabase.db")

    def test_select_all_sponsors(self):
        self.assertEqual(artDB.select_all_sponsors('Jan'), [('Manchester City', 'Maurycy Kowalski', 'Anglia', 28, 'Steward John', 'Jan')])
    
    def test_delete_club(self):
        artDB.delete_club('Manchester City')
        self.assertEqual(artDB.select_club('Manchester City'), [])

    def test_update_sponsor_glowny(self):
        artDB.update_sponsor_glowny('Bayern Monachium', 'T-mobile')
        self.assertEqual(artDB.select_club('Bayern Monachium'), [('Bayern Monachium','Julian Nagelsmann','Niemcy',25,'Robert Lewandowski','T-mobile')])


if __name__ == '__main__':  
    unittest.main()  