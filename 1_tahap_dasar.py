def kalk():
    print("\n=== KALKULATOR ===")
    print("Pilih Operasi:\n")
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. kali (x)")
    print("4. Bagi (:)")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan in ['1', '2', '3', '4']:
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))

            if pilihan == '1':
                hasil = angka1 + angka2
                print(f"{angka1} + {angka2} = {hasil}")
            elif pilihan == '2':
                hasil = angka1 - angka2
                print(f"{angka1} - {angka2} = {hasil}")
            elif pilihan == '3':
                hasil = angka1 * angka2
                print(f"{angka1} x {angka2} = {hasil}")
            elif pilihan == '4':
                try:
                    hasil = angka1 / angka2
                    print(f"{angka1} : {angka2} = {hasil}")
                except ZeroDivisionError:
                    print(f"{angka1} : {angka2} = Tak terdefinisi.")
        except ValueError:
            print("Error: Input harus berupa angka.")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    kalk()
