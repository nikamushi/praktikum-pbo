class Notifikasi:
    def kirim(self, pesan):
        raise NotImplementedError(pesan)

class Email(Notifikasi):
    def kirim(self, pesan):
        print(f"[EMAIL] Mengirim: '{pesan}'")

class SMS(Notifikasi):
    def kirim(self, pesan):
        print(f"[SMS] Mengirim: '{pesan}'")

class PushNotif(Notifikasi):
    def kirim(self, pesan):
        print(f"[PUSH] Mengirim: '{pesan}'")

pesan = "Diskon Spesial! Hanya untuk Anda!"
daftar = [Email(), SMS(), PushNotif()]

for notif in daftar:
    notif.kirim(pesan)