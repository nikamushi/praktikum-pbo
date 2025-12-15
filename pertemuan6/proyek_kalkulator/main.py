# main.py

# Mengimpor class dari modul-modul kita
from bangun_datar.lingkaran import Lingkaran
from bangun_datar.persegi import Persegi

def jalankan_program():
    print("--- Menghitung Luas Bangun Datar (Versi Monolitik) ---")

    lingkaran_A = Lingkaran(7)
    luas_lingkaran = lingkaran_A.hitung_luas()
    print(f"Luas lingkaran dengan radius 7 adalah {luas_lingkaran: .2f}")

    persegi_B = Persegi(5)
    luas_persegi = persegi_B.hitung_luas()
    print(f"Luas Persegi dengan sisi 5 adalah {luas_persegi}")

# Hanya jalankan fugnsi di atas jika file ini dieksekusi secar alangsung
if __name__ == "__main__":
    jalankan_program()