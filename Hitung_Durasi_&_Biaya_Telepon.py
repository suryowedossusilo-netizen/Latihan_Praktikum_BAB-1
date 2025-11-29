def waktu_ke_detik(waktu):
    jam, menit, detik = map(int, waktu.split(":"))
    return jam * 3600 + menit * 60 + detik
waktu_awal = input("Masukkan waktu awal (hh:mm:ss) : ")
waktu_akhir = input("Masukkan waktu akhir (hh:mm:ss): ")
awal_detik = waktu_ke_detik(waktu_awal)
akhir_detik = waktu_ke_detik(waktu_akhir)

durasi = akhir_detik - awal_detik

if durasi < 0:
    durasi += 24 * 3600 

print(f"Durasi telepon: {durasi} detik")
tarif_awal = 15  
tarif_selanjutnya = 1
batas_awal = 180

if durasi <= batas_awal:
    biaya = durasi * tarif_awal
else:
    biaya = (batas_awal * tarif_awal) + ((durasi - batas_awal) * tarif_selanjutnya)

print(f"Total biaya telepon: Rp {biaya}")
