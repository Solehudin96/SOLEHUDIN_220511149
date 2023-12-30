print("Konversi Suhu Reamur")

suhu = input("Masukkan suhu dalam Reamur : ")

C = (5/4 * float(suhu))
F = (9/4 * float(suhu)) + 32
K = (5/4 * float(suhu)) + 273

print(suhu + "Reamur sama dengan ")
print(str(C) + " Celcius")
print(str(F) + " Fahrenheit")
print(str(K) + " Kelvin")
