import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W
from math import pi

def hitung_luas_volume():
    try:
        # Ambil panjang alas, tinggi alas, dan tinggi prisma dari input pengguna
        panjang_alas = float(panjang_alas_entry.get())
        tinggi_alas = float(tinggi_alas_entry.get())
        tinggi_prisma = float(tinggi_prisma_entry.get())
        
        # Hitung luas permukaan dan volume prisma segitiga
        luas_permukaan = (0.5 * panjang_alas * tinggi_alas * 2) + (3 * panjang_alas * tinggi_prisma)
        volume = (0.5 * panjang_alas * tinggi_alas) * tinggi_prisma
        
        # Update label hasil
        luas_permukaan_var.set(f"Luas Permukaan Prisma Segitiga: {luas_permukaan:.2f}")
        volume_var.set(f"Volume Prisma Segitiga: {volume:.2f}")
    except ValueError:
        luas_permukaan_var.set("Masukkan angka valid")
        volume_var.set("Masukkan angka valid")

# Membuat jendela tkinter
window = tk.Tk()
window.title("Menghitung Luas Permukaan dan Volume Prisma Segitiga")

# Frame utama
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Label panjang alas, tinggi alas, dan tinggi prisma
panjang_alas_label = tk.Label(frame, text="Panjang Alas Prisma:")
panjang_alas_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

tinggi_alas_label = tk.Label(frame, text="Tinggi Alas Prisma:")
tinggi_alas_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

tinggi_prisma_label = tk.Label(frame, text="Tinggi Prisma:")
tinggi_prisma_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Input panjang alas, tinggi alas, dan tinggi prisma
panjang_alas_entry = tk.Entry(frame)
panjang_alas_entry.grid(row=0, column=1, padx=10, pady=10)

tinggi_alas_entry = tk.Entry(frame)
tinggi_alas_entry.grid(row=1, column=1, padx=10, pady=10)

tinggi_prisma_entry = tk.Entry(frame)
tinggi_prisma_entry.grid(row=2, column=1, padx=10, pady=10)

# Tombol hitung
hitung_button = tk.Button(frame, text="Hitung", command=hitung_luas_volume)
hitung_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="we")

# Hasil luas permukaan dan volume
luas_permukaan_var = tk.StringVar()
luas_permukaan_label = tk.Label(frame, textvariable=luas_permukaan_var)
luas_permukaan_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")

volume_var = tk.StringVar()
volume_label = tk.Label(frame, textvariable=volume_var)
volume_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="w")

window.mainloop()