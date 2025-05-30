import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
 
class AplikasiTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Tkinter Sederhana")
        self.root.attributes("-fullscreen", True)

        

        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))

        image = Image.open("background.png")
        self.bg_image = ImageTk.PhotoImage(image)
        self.bg_label = tk.Label(self.root, image=self.bg_image)
     
     self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.root.resizable(True, True)

        self.tampilkan_gambar()
 

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
