# DEBUG REPORT — DiskonCalculator (PPN Ditambahkan Dua Kali)

Tujuan: Mendokumentasikan proses debugging dengan pdb untuk mengidentifikasi bug bahwa PPN 10% ditambahkan dua kali di `diskon_service_bug.py`.

## Lingkungan

- Python 3.10+
- File yang diuji: `diskon_service_bug.py`

## Langkah Reproduksi Bug

1. Jalankan program dengan pdb:
   ```
   python -m pdb diskon_service_bug.py
   ```
2. Set breakpoint pada baris perhitungan `harga_akhir`:
   ```
   (Pdb) b diskon_service_bug.py:15
   ```
3. Jalankan program:
   ```
   (Pdb) c
   ```
4. Saat berhenti di breakpoint, inspeksi variabel dengan `p`:

   Contoh input: `harga_awal=1000`, `persentase_diskon=10`

   ```
   (Pdb) p harga_awal
   1000
   (Pdb) p persentase_diskon
   10
   (Pdb) p jumlah_diskon
   100.0
   (Pdb) p harga_setelah_diskon
   900.0
   (Pdb) p ppn
   90.0
   ```

5. Bukti PPN dihitung dua kali:

   ```
   (Pdb) p harga_setelah_diskon + ppn
   990.0
   (Pdb) p harga_setelah_diskon + ppn + ppn
   1080.0
   ```

   Nilai 1080.0 menunjukkan PPN (90) ditambahkan DUA KALI (efektif 20%), padahal semestinya hanya sekali (990.0 jika memang ingin menambahkan PPN 10% satu kali).

6. Lanjutkan eksekusi untuk melihat output akhir:
   ```
   (Pdb) c
   Hasil (BUG): 1080.0
   ```

## Akar Masalah

Di fungsi:

```python
ppn = harga_setelah_diskon * 0.10
harga_akhir = harga_setelah_diskon + ppn + ppn  # BUG: PPN ditambahkan dua kali
```

## Perbaikan

Ganti implementasi menjadi hanya menghitung diskon (sesuai spesifikasi fungsi) atau bila perlu menambahkan PPN, tambahkan hanya sekali di lapisan lain:

```python
jumlah_diskon = harga_awal * persentase_diskon / 100
harga_akhir = harga_awal - jumlah_diskon
```

## Validasi Perbaikan

Jalankan unit test:

```
python -m unittest -v test_diskon_advanced.py
```

Hasil yang diharapkan: semua test PASSED (OK).
