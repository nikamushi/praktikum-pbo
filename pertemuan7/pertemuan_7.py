import datetime # Impor pustaka datetime

class LogPesan:
    def __init__(self, pengirim, isi_pesan):
        self.__pengirim = pengirim
        self.__isi_pesan = isi_pesan
        # Secara otomatis mendapatkan waktu saat ini ketika objek dibuat
        self.__timestamp = datetime.datetime.now()
        
    def tampilkan_log(self):
        # Memformat timestamp menjadi string yang mudah dibaca
        waktu_terformat = self.__timestamp.strftime("%d %B %Y, Pukul %H:%M:%S")
        print("--- Log Pesan Masuk ---")
        print(f"Pengirim : {self.__pengirim}")
        print(f"Waktu    : {waktu_terformat}")
        print(f"Pesan    : {self.__isi_pesan}")

# --- Bagian Utama Program ---
pesan_1 = LogPesan("Admin", "Server akan segera di-restart untuk maintenance")
pesan_1.tampilkan_log()

# Tunggu beberapa detik dan buat pesan lain
# (Untuk simulasi, kita bisa tambahkan time.sleep jika diinginkan)
pesan_2 = LogPesan("User01", "Pekerjaan saya sudah disimpan, silahkan restart.")
pesan_2.tampilkan_log()