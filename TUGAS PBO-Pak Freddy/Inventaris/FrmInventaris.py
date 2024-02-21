# filename : FrmInventaris.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Inventaris import Inventaris
class FormInventaris:   
    def __init__(self, parent, title, update_main_window):
        self.parent = parent       
        self.parent.geometry("500x500")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.update_main_window = update_main_window
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10, bg='light blue')
        mainFrame.pack(fill=BOTH, expand=YES)
        
        
         # varchar 
        Label(mainFrame, text='KODE_BARANG:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox KODE_BARANG
        self.txtKODE_BARANG = Entry(mainFrame) 
        self.txtKODE_BARANG.grid(row=0, column=1, padx=10, pady=10) 
        self.txtKODE_BARANG.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # varchar 
        Label(mainFrame, text='NAMA_BARANG:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMA_BARANG
        self.txtNAMA_BARANG = Entry(mainFrame) 
        self.txtNAMA_BARANG.grid(row=1, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='RUANGAN:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Textbox RUANGAN
        self.txtRUANGAN = Entry(mainFrame) 
        self.txtRUANGAN.grid(row=2, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='KONDISI_BARANG:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Textbox KONDISI_BARANG
        self.txtKONDISI_BARANG = Entry(mainFrame) 
        self.txtKONDISI_BARANG.grid(row=3, column=1, padx=5, pady=5)
                
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','kode_barang','nama_barang','ruangan','kondisi_barang')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('kode_barang', text='kode_barang')
        self.tree.column('kode_barang', width="100")
        self.tree.heading('nama_barang', text='nama_barang')
        self.tree.column('nama_barang', width="150")
        self.tree.heading('ruangan', text='ruangan')
        self.tree.column('ruangan', width="100")
        self.tree.heading('kondisi_barang', text='kondisi_barang')
        self.tree.column('kondisi_barang', width="100")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtKODE_BARANG.delete(0,END)
        self.txtKODE_BARANG.insert(END,"")
                                
        self.txtNAMA_BARANG.delete(0,END)
        self.txtNAMA_BARANG.insert(END,"")
                                
        self.txtRUANGAN.delete(0,END)
        self.txtRUANGAN.insert(END,"")
                                
        self.txtKONDISI_BARANG.delete(0,END)
        self.txtKONDISI_BARANG.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data inventaris
        obj = Inventaris()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        kode_barang = self.txtKODE_BARANG.get()
        obj = Inventaris()
        res = obj.getByKODE_BARANG(kode_barang)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            
    def TampilkanData(self, event=None):
        kode_barang = self.txtKODE_BARANG.get()
        obj = Inventaris()
        res = obj.getByKODE_BARANG(kode_barang)
            
        self.txtNAMA_BARANG.delete(0,END)
        self.txtNAMA_BARANG.insert(END,obj.nama_barang)
                                
        self.txtRUANGAN.delete(0,END)
        self.txtRUANGAN.insert(END,obj.ruangan)
                                
        self.txtKONDISI_BARANG.delete(0,END)
        self.txtKONDISI_BARANG.insert(END,obj.kondisi_barang)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        kode_barang = self.txtKODE_BARANG.get()
        nama_barang = self.txtNAMA_BARANG.get()
        ruangan = self.txtRUANGAN.get()
        kondisi_barang = self.txtKONDISI_BARANG.get()       
        obj = Inventaris()
        obj.kode_barang = kode_barang
        obj.nama_barang = nama_barang
        obj.ruangan = ruangan
        obj.kondisi_barang = kondisi_barang
        if(self.ditemukan==True):
            res = obj.updateByKODE_BARANG(kode_barang)
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        kode_barang = self.txtKODE_BARANG.get()
        obj = Inventaris()
        obj.kode_barang = kode_barang
        if(self.ditemukan==True):
            res = obj.deleteByKODE_BARANG(kode_barang)
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
 
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormInventaris(root, "Aplikasi Data Inventaris", update_main_window)
    root.mainloop() 
    