
nilai = int(input("Masukkan nilai (0–100): "))
if nilai >= 80 and nilai <= 100:
    kategori = "A"
elif nilai >= 70:
    kategori = "B"
elif nilai >= 60:
    kategori = "C"
elif nilai >= 50:
    kategori = "D"
elif nilai >= 0:
    kategori = "E"
else:
    kategori = "Nilai tidak valid"

print("Kategori nilai Anda adalah:", kategori)

