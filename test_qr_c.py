import unittest
from qr_c import QR, NegativeRootError


class TestQR(unittest.TestCase):

    def test_valid_input(self):
        qr = QR(1, -3, 2)
        roots = qr.koreny()
        self.assertEqual(roots, (2.0, 1.0))

    def test_invalid_input_a_zero(self):
        with self.assertRaises(ValueError) as context:
            qr = QR(0, 2, 3)
        self.assertEqual(str(context.exception), "Koefficient 'a' nesmí být nula.")

    def test_negative_discriminant(self):
        with self.assertRaises(NegativeRootError) as context:
            qr = QR(2, 1, 5)
            qr.koreny()
        self.assertEqual(str(context.exception), "Vyšly negativní kořeny, což je špatně.")

    def test_invalid_input_non_numeric(self):
        with self.assertRaises(ValueError) as context:
            qr = QR('abc', 2, 3)
        self.assertEqual(str(context.exception), "Neplatný vstup pro koeficienty a, b, nebo c")


if __name__ == '__main__':
    unittest.main()
