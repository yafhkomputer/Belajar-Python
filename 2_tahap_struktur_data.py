daftar_belanja = ["tepung", "telur", "mentega"]

daftar_belanja.append(input("Nama barang yang ditambahkan: "))
daftar_belanja.remove(input("Nama barang yang dikeluarkan: "))
print(daftar_belanja)
posisi = daftar_belanja.index(input("Nama barang yang dicari: "))
print(f"Ada di index {posisi}")
