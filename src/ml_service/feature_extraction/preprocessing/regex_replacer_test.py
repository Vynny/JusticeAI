import unittest
from feature_extraction.preprocessing.regex_replacer import RegexReplacer


class RegexTest(unittest.TestCase):

    def test_normalize_string(self):
        sent_1 = 'à compter du 3 septembre 2014;'
        sent_2 = "fixe le loyer, après arrondissement au dollar le plus près, à 622,00 $ par mois du 1er juillet 2016 au 30 juin 2017, comprenant le coût de l'espace de stationnement;"
        sent_3 = ", à compter du 24 avril 2015, plus les frais judiciaires de 80 $;"
        expected_1 = 'compter date'
        expected_2 = 'après argent arrondissement comprenant coût date date dollar espace fixe loyer mois plus près stationnement'
        expected_3 = 'argent compter date frais judiciaires plus'
        self.assertEqual(RegexReplacer.normalize_string(sent_1), expected_1)
        self.assertEqual(RegexReplacer.normalize_string(sent_2), expected_2)
        self.assertEqual(RegexReplacer.normalize_string(sent_3), expected_3)
