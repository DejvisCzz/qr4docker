import unittest
from qrr_c import QR, NegativeRootError


class TestQR(unittest.TestCase):

    def test_platny_vstup(self):
        qr = QR(1, -3, 2)
        koreny = qr.koreny()
        self.assertEqual(koreny, (2.0, 1.0))

    def test_nula_vstup(self):
        with self.assertRaises(ValueError) as hlaska:
            qr = QR(0, 2, 3)
        self.assertIn("Koefficient 'a' nesmí být nula.", str(hlaska.exception))

    def test_negativni_koreny(self):
        with self.assertRaises(NegativeRootError) as hlaska:
            qr = QR(1, 3, 3)  # Koeficienty tak, aby kořeny byly záporné
            koreny = qr.koreny()
        self.assertIn("Vyšel negativní diskriminant, tudíž kořeny budou negativní.", str(hlaska.exception))

    def test_neplatny_vstup(self):
        with self.assertRaises(ValueError) as hlaska:
            qr = QR('a', 2, 3)
        self.assertIn("Neplatný vstup", str(hlaska.exception))

    def test_dis_nula(self):
            qr = QR(1, 2, 1)
            koreny = qr.koreny()
            self.assertEqual(koreny, (-1.0, -1.0))

if __name__ == '__main__':
    unittest.main()
