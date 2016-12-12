import unittest
class MeerSchweinTest(unittest.TestCase):
    
    def test_phaeno(self):
        Schnuffi = MeerSchwein({'color':'Ss', 'hairstyle': 'gG'},2)
        self.assertEqual(str(Schnuffi.phaenotype()),"{'color': 'S', 'hairstyle': 'G'}")
        
    def test_baby_meerschwein(self):
        # ist das Baby auch ein Meerschwein?
        Mama = MeerSchwein({'color':'Ss', 'hairstyle': 'gG'},2)
        Papa = MeerSchwein({'color':'Ss', 'hairstyle': 'gG'},2)
        Baby = mate(Mama,Papa)[0]
        self.assertEqual(str(type(Baby)),"<class '__main__.MeerSchwein'>")
    
meer_test = MeerSchweinTest()
meer_test.test_phaeno()
meer_test.test_baby_meerschwein()
