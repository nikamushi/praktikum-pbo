class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama # atribut public
        self.__gaji = gaji # atribut private, tidak bisa diakses langsung
        
    # Getter untuk mengakses gaji
    def get_gaji(self):
        return self.__gaji
    
    # Setter untuk mengubah gaji dengan validasi
    def set_gaji(self, gaji_baru):
        if gaji_baru < 0:
            print("Gaji tidak bisa negatif!")
        else:
            self.__gaji = gaji_baru
    
    # Method untuk menampilkan informasi karyawan
    def tampilkan_info(self):
        return f"Nama: {self.nama}, Gaji: {self.get_gaji()}"
    
# Membuat objek karyawan
karyawan1 = Karyawan("Andi", 5000000)

# Akses info karyawan
print(karyawan1.tampilkan_info())

# Mengubah gaji dengan setter 
karyawan1.set_gaji(6000000)
print(karyawan1.tampilkan_info())

# Mencoba mengubah gaji dengan nilai negatif
karyawan1.set_gaji(-1000)