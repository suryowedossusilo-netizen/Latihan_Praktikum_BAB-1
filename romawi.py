romawi = {
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
    6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X",
    11: "XI", 12: "XII", 13: "XIII", 14: "XIV", 15: "XV",
    16: "XVI", 17: "XVII", 18: "XVIII", 19: "XIX", 20: "XX"
}

angka = int(input("Masukkan bilangan (1-20): "))

if 1 <= angka <= 20:
    print(f"Angka Romawi dari {angka} adalah {romawi[angka]}")
else:
    print("Error: Masukkan bilangan antara 1 sampai 20!")
