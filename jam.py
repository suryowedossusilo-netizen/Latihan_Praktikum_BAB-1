
jam = int(input("Masukkan jam   : "))
menit = int(input("Masukkan menit : "))
detik = int(input("Masukkan detik : "))

total_detik = (jam * 3600) + (menit * 60) + detik

print(f"Total waktu dalam detik = {total_detik} detik")