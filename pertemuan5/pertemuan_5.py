# Parent Class
class Bentuk:
    def gambar(self):
        # Method ini sengaja dibuat umum dan akan di-override
        raise NotImplementedError("Subclass harus mengimplementasikan method ini!")
    
# Child Class 1
class Persegi(Bentuk):
    def gambar(self):
        print("Menggambar Persegi: [][][]")
        
# Child Class 2
class Lingkaran(Bentuk):
    def gambar(self):
        print("Menggambar Lingkaran: OOOOOO")
        
# Child Class 3
class Segitiga(Bentuk):
    def gambar(self):
        print("Menggambar Segitiga: /\\")
        
# Class Yang Tidak Berhubungan
class Teks:
    def gambar(self):
        print("Menulis Teks: 'Hello, Polymorphism'")

# Sebuah fungsi ynag menunjukkan perilaku polimorfik
def render_objek(objek_untuk_gambar):
    print("Mencoba me-render objek...")
    objek_untuk_gambar.gambar()
        
daftar_bentuk = [Persegi(), Lingkaran(), Persegi(), Lingkaran()]

print("--- Memanggil method yang sama pada objek yang berbeda ---")
for bentuk in daftar_bentuk:
    bentuk.gambar()

persegi = Persegi()
lingkaran = Lingkaran()
segitiga = Segitiga()
teks_biasa = Teks() # Objek ini bukan turunan dari bentuk

print("\n--- Menggunakan fungsi polimorfik ---")
render_objek(persegi)
render_objek(lingkaran)
render_objek(segitiga)

print("\n--- Demonstrasi Duck Typing ---")
render_objek(teks_biasa) # Fungsi tetap bekerja
