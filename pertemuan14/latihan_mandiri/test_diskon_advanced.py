import unittest
from diskon_service import DiskonCalculator

class TestDiskonLanjut(unittest.TestCase):
    def test_diskon_float_precision(self):
        calc = DiskonCalculator()
        harga_awal = 999.0
        diskon = 33
        expected = harga_awal * (1 - diskon/100)
        actual = calc.hitung_diskon(harga_awal, diskon)
        self.assertAlmostEqual(actual, expected, places=2)

    def test_edge_case_harga_awal_nol(self):
        calc = DiskonCalculator()
        self.assertEqual(calc.hitung_diskon(0.0, 50), 0.0)
        self.assertEqual(calc.hitung_diskon(0.0, 0), 0.0)
        self.assertEqual(calc.hitung_diskon(0.0, 100), 0.0)

if __name__ == "__main__":
    unittest.main()
