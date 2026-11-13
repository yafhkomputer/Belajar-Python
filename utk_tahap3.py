def cari_nama_siswa(siswa):
    try:
        siswa_yang_dicari = input("Masukkan nama siswa: ")
        print(f"Nama: {siswa_yang_dicari}, Nilai: {siswa[siswa_yang_dicari]}")
    except KeyError:
        print("Siswa tidak ada dalam daftar_siswa.")

def cari_nilai_siswa(siswa):
    nilai_yang_dicari = int(input("Masukkan nilai siswa: "))
    for key, value in siswa.items():
        if value == nilai_yang_dicari:
            return key
    return None

def hitung_rata_rata(siswa):
    jumlah_siswa = len(siswa)
    total_nilai = sum(siswa.values())
    rata_rata = total_nilai / jumlah_siswa
    return rata_rata

def cek_kelulusan(siswa):
    for key, value in siswa.items():
        if value >= 80:
            print(f"Nama: {key}, Ket: LULUS")
        else:
            print(f"Nama: {key}, Ket: TIDAK LULUS")

def menu(siswa):
    while True:
        print("\n=== NILAI SISWA ===")
        print("1. Cari nama siswa")
        print("2. Cari nilai siswa")
        print("3. Menghitung rata-rata")
        print("4. mengecek kelulusan")
        print("5. Keluar")

        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == '1':
            cari_nama_siswa(siswa)
        elif pilihan == '2':
            hasil = cari_nilai_siswa(siswa)
            print(f"Yang memilki nilai tersebut: {hasil}")
        elif pilihan == '3':
            hasil = hitung_rata_rata(siswa)
            print(f"rata-rata keseluruhan: {hasil}")
        elif pilihan == '4':
            cek_kelulusan(siswa)
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid.")
