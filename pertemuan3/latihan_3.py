class Karyawan:
    def __init__(self, nama, id_karyawan, gaji):
        self.__nama = nama
        self.__id_karyawan = id_karyawan
        self.__gaji = gaji
        
    def get_nama(self):
        return self.__nama
    
    def get_id(self):
        return self.__id_karyawan
    
    def get_gaji(self):
        return self.__gaji
    
    def set_nama(self, nama_baru):
        if nama_baru == "":
            print("Nama baru tidak boleh kosong")
        else:
            self.__nama = nama_baru
            print("Nama berhasil diubah")
    
    def set_gaji(self, gaji_baru):
        if gaji_baru <= 0:
            print("Error: Gaji baru harus lebih besar dari 0")
        else:
            self.__gaji = gaji_baru
            print("Gaji berhasil diubah")

karyawan1 = Karyawan("Baskara", "K001", 500000000)

print("\n--- Menampilkan Menggunakan Get ---")
print(f"Nama: {karyawan1.get_nama()}")
print(f"Id  : {karyawan1.get_id()}")
print(f"Gaji: {karyawan1.get_gaji()}")

print("\n--- Mengubah Gaji Karyawan (Negatif) ---")
karyawan1.set_gaji(-5000000)
print(f"Gaji sekarang: {karyawan1.get_gaji()}")

print("\n --- Mengubah Gaji Karyawan (Positif) ---")
karyawan1.set_gaji(6000000)
print(f"Gaji sekarang: {karyawan1.get_gaji()}")

print("\n--- Menampilkan Data Karyawan Terbaru ---")
print(f"Nama: {karyawan1.get_nama()}")
print(f"Id  : {karyawan1.get_id()}")
print(f"Gaji: {karyawan1.get_gaji()}")