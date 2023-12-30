print("Konversi Suhu Fahrenheit")

suhu = input("Masukkan suhu dalam Fahrenheit : ")

C = (5/9 * (float(suhu) - 32))
R = (4/9 * (float(suhu) - 32))
K = (5/9 * (float(suhu) - 32)) + 273

print(suhu + "Reamur sama dengan ")
print(str(C) + " Celcius")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")
