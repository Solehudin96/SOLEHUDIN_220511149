from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W, font

class FrmAdmin:
    def _init_(self, parent, title):
        self.parent = parent
        self.parent.geometry ("600x600")
        self.parent.title(title)
        self.parent.protocol ("WM_DELETE_WINDOW", self.onkeluar) 
        self.aturKomponen()

    def aturKomponen (self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack (fill=BOTH, expand=YES)

        label = Label (mainFrame, text="Admin Content", font=font. Font(size=40))
        label.pack (padx=20, pady=20)

    def onkeluar (self, event=None):
        # memberikan perintah menutup aplikasi 
        self.parent.destroy()

if __name__ == '__main__':
    def update_main_window (result):
        print(result)

    root = Tk()
    aplikasi = FrmAdmin (root, "Windows Admin")
    root.mainloop()