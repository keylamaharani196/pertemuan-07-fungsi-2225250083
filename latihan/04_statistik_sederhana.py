
# Latihan 4: Statistik Sederhana

def statistik(data):
    total = 0
    minimum = data[0]
    maksimum = data[0]

    for x in data:
        total += x

        if x < minimum:
            minimum = x

        if x > maksimum:
            maksimum = x

    rata = total / len(data)

    return minimum, maksimum, rata


# Data nilai
data_nilai = [70, 80, 65, 90, 75]

mn, mx, rt = statistik(data_nilai)

print("Nama: Keyla Maharani")
print("Data nilai:", data_nilai)
print("Nilai minimum:", mn)
print("Nilai maksimum:", mx)
print("Nilai rata-rata:", rt)
