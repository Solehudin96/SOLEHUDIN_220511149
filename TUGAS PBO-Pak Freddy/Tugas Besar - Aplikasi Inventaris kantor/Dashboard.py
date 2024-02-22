import tkinter as tk
from tkinter import Menu, messagebox
from PIL import Image, ImageTk
from FrmLogin import *
from FrmInventaris import *
from Inventaris import Inventaris

class Dashboard:
    def __init__(self):
        # root window
        self.root = tk.Tk()
        self.root.title('APLIKASI INVENTARIS KANTOR')
        self.root.geometry("600x400")
        self.root.configure(background="light blue")
        self.__data = None
        self.__level = None
        self.image_path = r'D:\SOLEHUDIN 220511149\TUGAS PBO-Pak Freddy\Inventaris\Inventaris logo.jpg'

        self.img = Image.open(self.image_path)
        self.photo_img = ImageTk.PhotoImage(self.img)
        self.image_label = tk.Label(self.root, image=self.photo_img)
        self.image_label.pack()

        # create a menubar
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        # create menus
        self.file_menu = Menu(self.menubar)
        self.guest_menu = Menu(self.menubar)
        self.admin_menu = Menu(self.menubar)

        # add menu items to File menu
        self.file_menu.add_command(label='Login', command=lambda: self.new_window("APLIKASI INVENTARIS KANTOR", FormLogin))
        self.file_menu.add_command(label='Exit', command=self.root.destroy)

        # add menu items to menu Admin
        self.admin_menu.add_command(label='Admin-1', command=lambda: self.new_window("APLIKASI INVENTARIS KANTOR", FormInventaris))
        # add menus to the menubar
        self.menubar.add_cascade(label="START", menu=self.file_menu)
        

    def new_window(self, number, _class):
        new = tk.Toplevel(self.root)
        new.transient()
        new.grab_set()
        _class(new, number, self.update_main_window)

    def update_main_window(self, data):
        # Method to receive data from child windows
        self.__data = data
        level = self.__data[0]
        loginvalid = self.__data[1]
        if(loginvalid==True):
            index = self.file_menu.index('Login')
            # hapus menu login
            self.file_menu.delete(index)
            self.file_menu.add_command(label='Logout', command=self.Logout)

            # tambahkan menu sesuai level
            if(level=='admin'): 
                self.menubar.add_cascade(label="Admin", menu=self.admin_menu)
                self.__level = 'Admin'
            
            else:
                pass

    def Logout(self):
        index = self.file_menu.index('Logout')
        self.file_menu.delete(index)
        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", FormLogin))
        self.remove_all_menus()

    def remove_all_menus(self):
        index = self.menubar.index(self.__level)
        if index is not None:
            self.menubar.delete(index)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    menu_app = Dashboard()
    menu_app.run()
