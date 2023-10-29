print("Progam Menghitung Luas dan volume kerucut")
"""
Nama  : SOLEHUDIN
NIM   : 220511149
Kelas : TI22L
PBO   : Tugas Pertemuan 1

Keterangan:
L = Luas permukaan kerucut
r = Jari-jari
T = Tinggi
s = Garis pelukis
phi = 3,14
"""
# Atur Nilai
phi = 3.14
r = 6
s = 7
T = 8

# Rumus
luas_selimut = phi * r * s
luas_permukaan = (phi * r * s) + (phi * r**2)
volume = 1/3 * phi * r**2 * T

# Output
print("Phi:", phi)
print("Jari-Jari:", r)
print("Tinggi:", T)
print("Garis Pelukis:", s)
print("Luas Selimut:", luas_selimut)
print("Luas Permukaan:", luas_permukaan)
print("Volume:", volume)