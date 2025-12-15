class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.status_pinjam = False
        
    def tampilkan_info(self):
        print(f"Judul           : {self.judul}")
        print(f"Penulis         : {self.penulis}")
        print(f"Tahun terbit    : {self.tahun_terbit}")
        print(f"Status pinjam   : {self.status_pinjam}")
        
    def pinjam_buku(self):
        self.status_pinjam = True
        print(f"Buku '{self.judul}' telah dipinjam.")
        
    def kembalikan_buku(self):
        self.status_pinjam = False
        print(f"Buku '{self.judul}' telah dikembalikan.")
    
buku1 = Buku("Laskar Pelangi", "Andrea Hirata", 2005)
buku2 = Buku("Bumi Manusia", "Pramoedya Ananta Toer", 1980)

# tampilkan_info()
buku1.tampilkan_info()
print("="*40)
buku2.tampilkan_info()
print("\n")

# pinjam_buku()
buku1.pinjam_buku()
buku1.tampilkan_info()
print("="*40)

# kembalikan_buku()
buku1.kembalikan_buku()
buku1.tampilkan_info()