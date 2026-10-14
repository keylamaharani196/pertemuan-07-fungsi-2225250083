
# Latihan 3: Jumlah 1 sampai n

def jumlah_n(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


# Menguji nilai n
for n in [1, 5, 10, 100]:
    hasil = jumlah_n(n)
    rumus = n * (n + 1) / 2

    print(f"n = {n}")
    print(f"Hasil perulangan = {hasil}")
    print(f"Hasil rumus = {rumus:.0f}")
    print("-" * 30)
