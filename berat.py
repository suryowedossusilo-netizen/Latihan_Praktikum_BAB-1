gram = float(input("Masukkan berat dalam gram : "))

kilogram = gram / 1000
pon = gram / 453.59237   
ons = gram / 28.3495    

print("\n=== HASIL KONVERSI ===")
print(f"Kilogram : {kilogram:.4f} kg")
print(f"Pon      : {pon:.4f} pound")
print(f"Ons      : {ons:.4f} ons")