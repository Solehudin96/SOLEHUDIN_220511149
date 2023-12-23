import tkinter as tk
from tkinter import filedialog
import pygame

def play_music():
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def choose_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        play_music()

def stop_music():
    pygame.mixer.music.stop()

root = tk.Tk()
root.title("MP3 Player")

file_path = ""

play_button = tk.Button(root, text="Pilih File MP3", command=choose_file)
play_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack(pady=10)

pygame.mixer.init()

root.mainloop()
