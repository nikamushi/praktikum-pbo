class Kontak:
    def __init__(self, nama, nomor_telepon):
        self.__nama = nama
        self.__nomor_telepon = nomor_telepon

    def tampilkan_info(self):
        print(f"Nama: {self.get_nama()}")
        print(f"Nomor Telepon: {self.get_nomor()}")
        
    def get_nama(self):
        return self.__nama
    
    def get_nomor(self):
        return self.__nomor_telepon
    
    def set_nama(self, nama):
        self.__nama = nama
        
    def set_nomor(self, nomor):
        self.__nomor_telepon = nomor

