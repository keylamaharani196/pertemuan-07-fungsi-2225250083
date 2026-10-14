
# Praktik 2: Utilitas Matematika Modular
# Nama: Keyla Maharani
# Kelas: 3E

def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus bilangan bulat nonnegatif")

    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def faktorial(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus bilangan bulat nonnegatif")

    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil


def tampilkan_menu():
    print("\n=== UTILITAS MATEMATIKA ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("5. Keluar")


# Program utama
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        print("Luas persegi panjang =", luas_persegi_panjang(p, l))

    elif pilihan == "2":
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        print("Luas segitiga =", luas_segitiga(a, t))

    elif pilihan == "3":
        try:
            n = int(input("Masukkan bilangan bulat n: "))
            print("Jumlah 1 sampai", n, "=", jumlah_n(n))
        except ValueError:
            print("Input salah! Masukkan bilangan bulat nonnegatif.")

    elif pilihan == "4":
        try:
            n = int(input("Masukkan bilangan bulat n: "))
            print("Faktorial", n, "=", faktorial(n))
        except ValueError:
            print("Input salah! Masukkan bilangan bulat nonnegatif.")

    elif pilihan == "5":
        print("Terima kasih, Keyla Maharani!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1-5.")
