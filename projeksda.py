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

self.current_page_widgets = []
        self.about_photo_refs = []

        self.button_normal_bg = "#18AEB9"
        self.button_hover_bg = "#14959E"
        self.button_text_fg = "white"

        self.show_home_screen()

    def clear_current_page(self):
        for widget in self.current_page_widgets:
            if widget.winfo_exists():
                widget.destroy()
        self.current_page_widgets.clear()
        self.about_photo_refs.clear()

    
    def bind_hover_effects(self, button):
        button.bind("<Enter>", lambda e: button.config(bg=self.button_hover_bg)) # Saat mouse masuk
        button.bind("<Leave>", lambda e: button.config(bg=self.button_normal_bg)) # Saat mouse keluar

    def show_home_screen(self):
        self.clear_current_page()

       
        if self.photo_background_default:
            self.bg_label.config(image=self.photo_background_default)
        else: 
            self.bg_label.config(image='', bg=self.content_bg_color) 
            
        try:
            img = Image.open("sehun.png")
            img = img.resize((400, 250), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            self.label_gambar = tk.Label(self.bg_label, image=self.photo, bg="#D9F2F4") 
            self.label_gambar.pack(pady=10)
            self.current_page_widgets.append(self.label_gambar)
        except FileNotFoundError:
            print("Error: sehun.png tidak ditemukan.")
            self.label_gambar = tk.Label(self.bg_label, text="Gambar tidak ditemukan", bg="#D9F2F4")
            self.label_gambar.pack(pady=10)
            self.current_page_widgets.append(self.label_gambar)
         
            self.start_button = tk.Button(
            self.bg_label,
            text="Start",
            command=self.on_start_button_click,
            font=("Basketball", 14),
            width=20,
            height=2,
            bg=self.button_normal_bg, 
            fg=self.button_text_fg,   
            relief="flat",           
            activebackground=self.button_hover_bg 
        )
        self.start_button.pack(pady=5)
        self.current_page_widgets.append(self.start_button)
        self.bind_hover_effects(self.start_button)

        self.about_button = tk.Button(
            self.bg_label,
            text="About",
            command=self.on_about_button_click,
            font=("Basketball", 14),
            width=20,
            height=2,
            bg=self.button_normal_bg,
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        self.about_button.pack(pady=5)
        self.current_page_widgets.append(self.about_button)
        self.bind_hover_effects(self.about_button)

        self.exit_button = tk.Button(
            self.bg_label,
            text="Exit",
            command=self.on_exit_button_click,
            font=("Basketball", 14),
            width=20,
            height=2,
            bg=self.button_normal_bg,
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        self.exit_button.pack(pady=5)
        self.current_page_widgets.append(self.exit_button)
        self.bind_hover_effects(self.exit_button)

def show_new_page(self):
        self.clear_current_page()

       
        if self.photo_background_new_page:
            self.bg_label.config(image=self.photo_background_new_page)
        else: 
            self.bg_label.config(image='', bg=self.content_bg_color)


        label_halaman_baru = tk.Label(self.bg_label, text="Ini Halaman Baru!", font=("Arial", 30), bg=self.content_bg_color)
        label_halaman_baru.pack(expand=True, pady=50)
        self.current_page_widgets.append(label_halaman_baru)

        back_button = tk.Button(
            self.bg_label,
            text="Kembali ke Home",
            command=self.show_home_screen,
            font=("Poppins", 12),
            pady=10,
            bg=self.button_normal_bg,
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        back_button.pack(pady=20)
        self.current_page_widgets.append(back_button)
        self.bind_hover_effects(back_button)

    def show_about_page(self):
        self.clear_current_page()

        
        if self.photo_background_default:
            self.bg_label.config(image=self.photo_background_default)
        else:
            self.bg_label.config(image='', bg=self.content_bg_color)

about_title_label = tk.Label(self.bg_label, text="About Us", font=("Basketball", 30,), bg=self.content_bg_color)
        about_title_label.pack(pady=20)
        self.current_page_widgets.append(about_title_label)

        photos_container = tk.Frame(self.bg_label, bg=self.content_bg_color) 
        photos_container.pack(pady=10)
        self.current_page_widgets.append(photos_container)

        foto_files = ["foto1.png", "foto2.png", "foto3.png", "foto4.png"]
        orang_names = ["Filuth Ridho Aji", "peri", "jahira", "talita"]

        for i, foto_file in enumerate(foto_files):
            person_frame = tk.Frame(photos_container, bg="white") 
            person_frame.pack(side=tk.LEFT, padx=5, pady=10)
            self.current_page_widgets.append(person_frame)
