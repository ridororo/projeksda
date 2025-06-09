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

   try:
            
            original_bg_image_pil = Image.open(self.default_bg_path)
            resized_bg_image_pil = original_bg_image_pil.resize((self.screen_width, self.screen_height), Image.LANCZOS)
            self.photo_background_default = ImageTk.PhotoImage(resized_bg_image_pil)
            
           
            original_new_page_bg_pil = Image.open(self.new_page_bg_path)
            resized_new_page_bg_pil = original_new_page_bg_pil.resize((self.screen_width, self.screen_height), Image.LANCZOS)
            self.photo_background_new_page = ImageTk.PhotoImage(resized_new_page_bg_pil)

            self.bg_label = tk.Label(self.root, image=self.photo_background_default) 
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.content_bg_color = "#D9F2F4" 
    
        except FileNotFoundError as e:
            print(f"Error: File background tidak ditemukan ({e}). Menggunakan warna latar belakang default.")
            self.content_bg_color = "#D9F2F4" 
            self.root.configure(bg=self.content_bg_color)
            self.bg_label = tk.Label(self.root, bg=self.content_bg_color)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.photo_background_default = None 
            self.photo_background_new_page = None

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
