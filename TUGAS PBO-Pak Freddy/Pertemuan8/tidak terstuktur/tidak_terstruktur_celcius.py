print("Konversi Suhu Celcius")

suhu = input("Masukkan suhu dalam Celcius : ")

F = (9/5 * float(suhu)) + 32
R = (4/5 * float(suhu))
K = float(suhu) + 273

print(suhu + "celcius sama dengan ")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")