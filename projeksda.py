import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
 
class AplikasiTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Tkinter Sederhana")
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

       
        self.photo_background_default = None
        self.photo_background_new_page = None 
        self.default_bg_path = "background.png"
        self.new_page_bg_path = "bg2.png"        

    def tampilkan_gambar(self):
        img = Image.open("sehun.png") 
        img = img.resize((400,250))
        self.root.configure(bg="#D9F2F4")  

        self.photo = ImageTk.PhotoImage(img)

        self.label_gambar = tk.Label(self.root, image=self.photo, bg="#D9F2F4")

        self.label_gambar.pack(pady=10)
     
        self.button =tk.Button(
    self.root,
    text="Login",
    command=self.tampilkan_pesan,
    font=("Poppins", 14),  
    width=20,                
    height=2                 
).pack(pady=10)

        self.button =tk.Button(
    self.root,
    text="Register",
    command=self.tampilkan_pesan,
    font=("Poppins", 14), 
    width=20,                
    height=2                 
).pack(pady=10)

self.button = tk.Button(
    self.root,
    text="Menu",
    command=self.tampilkan_pesan,
    font=("Poppins", 14, ),
    width=20,                
    height=2                 
).pack(pady=10)

    def tampilkan_pesan(self):
        tk.messagebox.showinfo("Informasi", "Coming Soon!")
if _name_ == "_main_":
    root = tk.Tk()
    app = AplikasiTkinter(root)
    root.mainloop()
