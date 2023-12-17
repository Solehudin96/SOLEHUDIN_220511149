from tkinter import Tk, Label, Entry, Button
from gtts import gTTS
import os

def text_to_speech():
    text = entry_text.get()

    # Gunakan bahasa yang diinginkan (dalam contoh ini, bahasa Inggris)
    language = 'en'

    # Buat objek gTTS
    tts = gTTS(text=text, lang=language, slow=False)

    # Simpan file suara sebagai "output.mp3"
    tts.save("output.mp3")

    # Putar file suara menggunakan perintah sistem (menggunakan command-line)
    os.system("start output.mp3")

# Membuat GUI
root = Tk()
root.title("Text Menjadi Suara")

# Label
label = Label(root, text="Masukkan Teks:")
label.pack()

# Entry untuk memasukkan teks
entry_text = Entry(root, width=50)
entry_text.pack()

# Tombol untuk mengonversi teks menjadi suara
button_convert = Button(root, text="Konversi ke Suara", command=text_to_speech)
button_convert.pack()

# Menjalankan loop utama GUI
root.mainloop()
