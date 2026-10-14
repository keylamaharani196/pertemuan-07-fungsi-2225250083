
# Latihan 5: Eksperimen Scope

x = 10

def demo(x):
    y = x + 5
    print("di dalam fungsi:", x, y)
    return y


hasil = demo(20)

print("Nama: Keyla Maharani")
print("di luar fungsi:", x, hasil)
