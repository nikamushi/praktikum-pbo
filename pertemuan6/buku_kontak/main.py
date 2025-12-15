from models.kontak import Kontak

if __name__ == "__main__":
    daftar_kontak = []
    kontak1 = Kontak("Baskara", "082154168846")
    kontak2 = Kontak("Saputra", "082166914449")
    kontak3 = Kontak("Kara", "082144915466")

    kontak1.set_nama("Bas")
    kontak1.set_nomor("082154168846")
    
    kontak2.set_nama("Kara")
    kontak2.set_nomor("082166914449")
    
    kontak3.set_nama("Saputra")
    kontak3.set_nomor("082154168846")
    
    daftar_kontak.append(kontak1)
    daftar_kontak.append(kontak2)
    daftar_kontak.append(kontak3)
    
    for kontak in daftar_kontak:
        kontak.tampilkan_info()