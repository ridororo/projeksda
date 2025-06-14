import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
import os

waktu_kiri = 0
running_kiri = False
label_kiri = None

waktu_kanan = 0
running_kanan = False
label_kanan = None

def update_kiri():
    global waktu_kiri, running_kiri, label_kiri
    if running_kiri:
        waktu_kiri += 1
        menit = (waktu_kiri % 3600) // 60
        detik = waktu_kiri % 60
        label_kiri.config(text=f"{menit:02}:{detik:02}")
        label_kiri.after(1000, update_kiri)

def mulai_kiri():
    global running_kiri
    if not running_kiri:
        running_kiri = True
        update_kiri()

def stop_kiri():
    global running_kiri
    running_kiri = False

def reset_kiri():
    global running_kiri, waktu_kiri
    running_kiri = False
    waktu_kiri = 0
    label_kiri.config(text="00:00")

def update_kanan():
    global waktu_kanan, running_kanan, label_kanan
    if running_kanan:
        waktu_kanan += 1
        menit = (waktu_kanan % 3600) // 60
        detik = waktu_kanan % 60
        label_kanan.config(text=f"{menit:02}:{detik:02}")
        label_kanan.after(1000, update_kanan)

def mulai_kanan():
    global running_kanan
    if not running_kanan:
        running_kanan = True
        update_kanan()

def stop_kanan():
    global running_kanan
    running_kanan = False

def reset_kanan():
    global running_kanan, waktu_kanan
    running_kanan = False
    waktu_kanan = 0
    label_kanan.config(text="00:00")

def mulai_kedua():
    mulai_kiri()
    mulai_kanan()

def stop_kedua():
    stop_kiri()
    stop_kanan()

def reset_kedua():
    reset_kiri()
    reset_kanan()

 
class AplikasiTkinter:

    def show_input_peserta_page(self, tim="biru"):
        self.clear_current_page()

        frame_input = tk.Frame(self.bg_label, bg="white")
        frame_input.place(relx=0.5, rely=0.5, anchor="center")
        self.current_page_widgets.append(frame_input)

        label_judul = tk.Label(frame_input, text=f"Input Peserta Tim {tim.capitalize()}", font=("Helvetica", 16, "bold"), bg="white")
        label_judul.pack(pady=10)

        tk.Label(frame_input, text="Nama:", font=("Helvetica", 12), bg="white").pack()
        self.entry_nama = tk.Entry(frame_input, font=("Helvetica", 12))
        self.entry_nama.pack(pady=5)

        tk.Label(frame_input, text="Asal:", font=("Helvetica", 12), bg="white").pack()
        self.entry_asal = tk.Entry(frame_input, font=("Helvetica", 12))
        self.entry_asal.pack(pady=5)

        btn_simpan = tk.Button(
            frame_input,
            text="Simpan",
            font=("Helvetica", 12),
            bg="#18AEB9",
            fg="white",
            command=lambda: self.simpan_peserta_csv(tim)
        )
        btn_simpan.pack(pady=10)

        btn_kembali = tk.Button(
            frame_input,
            text="Kembali",
            font=("Helvetica", 12),
            command=self.show_home_screen
        )
        btn_kembali.pack()

    def simpan_peserta_csv(self, tim):
        nama = self.entry_nama.get()
        asal = self.entry_asal.get()

        if not nama or not asal:
            messagebox.showwarning("Peringatan", "Nama dan Asal harus diisi.")
            return

        nama_file = f"peserta_{tim.lower()}.csv"
        file_baru = not os.path.isfile(nama_file)

        try:
            with open(nama_file, "a", newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                if file_baru:
                    writer.writerow(["Nama", "Asal"])
                writer.writerow([nama, asal])
            
            messagebox.showinfo("Sukses", f"Data '{nama}' berhasil disimpan ke tim {tim.capitalize()}!")

            self.entry_nama.delete(0, tk.END)
            self.entry_asal.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan data: {e}")





    def __init__(self, root):
        self.root = root

        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.default_bg_path = "background.png"
        self.new_page_bg_path = "terbaru2.png"



        self.photo_background_default = None
        self.photo_background_new_page = None
        self.content_bg_color = "#D9F2F4"

        try:
            bg_image = Image.open(self.default_bg_path).resize(
                (self.screen_width, self.screen_height), Image.LANCZOS
            )
            self.photo_background_default = ImageTk.PhotoImage(bg_image)

            new_bg_image = Image.open(self.new_page_bg_path).resize(
                (self.screen_width, self.screen_height), Image.LANCZOS
            )
            self.photo_background_new_page = ImageTk.PhotoImage(new_bg_image)

            self.bg_label = tk.Label(self.root, image=self.photo_background_default)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        except FileNotFoundError as e:
            print(f"Error: {e}")
            self.root.configure(bg=self.content_bg_color)
            self.bg_label = tk.Label(self.root, bg=self.content_bg_color)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

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
        button.bind("<Enter>", lambda e: button.config(bg=self.button_hover_bg))
        button.bind("<Leave>", lambda e: button.config(bg=self.button_normal_bg))


    def show_home_screen(self):
        self.clear_current_page()

        btn_input_biru = tk.Button(
            self.bg_label,
            text="Input Peserta Biru",
            command=lambda: self.show_input_peserta_page("biru"),
            font=("Poppins", 12),
            bg=self.button_normal_bg,
            fg=self.button_text_fg
        )
        btn_input_biru.pack(pady=5)
        self.current_page_widgets.append(btn_input_biru)

        btn_input_merah = tk.Button(
            self.bg_label,
            text="Input Peserta Merah",
            command=lambda: self.show_input_peserta_page("merah"),
            font=("Poppins", 12),
            bg=self.button_normal_bg,
            fg=self.button_text_fg
        )
        btn_input_merah.pack(pady=5)
        self.current_page_widgets.append(btn_input_merah)

       
        if self.photo_background_default:
            self.bg_label.config(image=self.photo_background_default)
        else: 
            self.bg_label.config(image='', bg=self.content_bg_color) 
 
        try:
            img = Image.open("sehun.png").resize((400, 250), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            label_gambar = tk.Label(self.bg_label, image=self.photo, bg=self.content_bg_color)
        except FileNotFoundError:
            print("Error: sehun.png tidak ditemukan.")
            label_gambar = tk.Label(self.bg_label, text="Gambar tidak ditemukan", bg=self.content_bg_color)

    
        label_gambar.pack(pady=10)
        self.current_page_widgets.append(label_gambar)

        start_button = tk.Button(
            self.bg_label,
            text="Start",
            command=self.on_start_button_click,
            font=("Poppins", 14),
            width=20,
            height=2,
            bg=self.button_normal_bg,
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        start_button.pack(pady=5)
        self.current_page_widgets.append(start_button)
        self.bind_hover_effects(start_button)

        about_button = tk.Button(
            self.bg_label,
            text="About",
            command=self.on_about_button_click,
            font=("Poppins", 14),
            width=20,
            height=2,
            bg=self.button_normal_bg,
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        about_button.pack(pady=5)
        self.current_page_widgets.append(about_button)
        self.bind_hover_effects(about_button)

        exit_button = tk.Button(
            self.bg_label,
            text="Exit",
            command=self.on_exit_button_click,
            font=("Poppins", 14),
            width=20,
            height=2,
            bg=self.button_normal_bg,
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        exit_button.pack(pady=5)
        self.current_page_widgets.append(exit_button)
        self.bind_hover_effects(exit_button)
    def reset_kedua_stopwatch(self):
        reset_kiri()
        reset_kanan()

    def load_peserta_dari_csv(self, path):
        data = []
        try:
            with open(path, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"File {path} tidak ditemukan.")
        return data
def show_new_page(self):
        self.clear_current_page()

       
        if self.photo_background_new_page:
            self.bg_label.config(image=self.photo_background_new_page)
        else: 
            self.bg_label.config(image='', bg=self.content_bg_color)
         
        foto_bendera = "bendera_merah.png"
        foto_bendera2 = "bendera_biru.png"
       
        try:
            img1 = Image.open("bendera_biru.png").resize((240, 270), Image.LANCZOS)
            foto1 = ImageTk.PhotoImage(img1)
            self.about_photo_refs.append(foto1)

            label1 = tk.Label(self.bg_label, image=foto1, bg=self.content_bg_color)
            label1.place(x=440, y=150)  
            self.current_page_widgets.append(label1)
        except FileNotFoundError:
            print("Error: bendera_biru.png tidak ditemukan.")
            label1 = tk.Label(self.bg_label, text="bendera_biru.png tidak ditemukan", bg=self.content_bg_color)
            label1.place(x=100, y=250)
            self.current_page_widgets.append(label1)


        try:
            img2 = Image.open("bendera_merah.png").resize((240, 270), Image.LANCZOS)
            foto2 = ImageTk.PhotoImage(img2)
            self.about_photo_refs.append(foto2)

            label2 = tk.Label(self.bg_label, image=foto2, bg=self.content_bg_color)
            label2.place(x=1220, y=150)  
            self.current_page_widgets.append(label2)
        except FileNotFoundError:
            print("Error: bendera_merah.png tidak ditemukan.")
            label2 = tk.Label(self.bg_label, text="bendera_merah.png tidak ditemukan", bg=self.content_bg_color)
            label2.place(x=100, y=250)
            self.current_page_widgets.append(label2)


        frame_kiri = tk.Frame(self.bg_label, bg="#5271ff")
        frame_kiri.place(x=350, y=500, width=400, height=300)
        self.current_page_widgets.append(frame_kiri)

        global label_kiri
        label_kiri = tk.Label(frame_kiri, text="00:00", font=("Helvetica", 70), bg="#5271ff", fg="white")
        label_kiri.pack(pady=20)


        frame_kanan = tk.Frame(self.bg_label, bg="#ff3131")
        frame_kanan.place(x=1150, y=500, width=400, height=300)
        self.current_page_widgets.append(frame_kanan)

        global label_kanan
        label_kanan = tk.Label(frame_kanan, text="00:00", font=("Helvetica", 70), bg="#ff3131", fg="white")
        label_kanan.pack(pady=20)
    

        tombol_mulai = tk.Button( text="Start", font=("Helvetica", 16), width=12, bg="#5bff52", fg="white", command=mulai_kedua)
        tombol_mulai.place(x=100, y=565)
        self.current_page_widgets.append(tombol_mulai)


        tombol_stop = tk.Button( text="Stop", command=stop_kedua,
        font=("Helvetica", 16), width=12, bg="#f44336", fg="white")
        tombol_stop.place(x=691, y=730)
        self.current_page_widgets.append(tombol_stop)


        tombol_reset = tk.Button( text="Reset", command=reset_kedua,
        font=("Helvetica", 16), width=12, bg="#2196F3", fg="white")
        tombol_reset.place(x=1300, y=730)
        self.current_page_widgets.append(tombol_reset)
                # === FRAME UNTUK SKOR DI TENGAH ===
        skor_frame2 = tk.Frame(self.bg_label, bg="#5271ff")
        skor_frame2.place(x=50, y=110, width=300, height=300)
        self.current_page_widgets.append(skor_frame2)

        self.skor2 = tk.IntVar(value=0)

        def tambah2():
            self.skor2.set(self.skor2.get() + 1)

        def kurang2():
            self.skor2.set(self.skor2.get() - 1)

        label = tk.Label(skor_frame2, textvariable=self.skor2, font=("Helvetica", 128), bg="#5271ff")
        label.place(x=10, y=50)

        tombol_tambah = tk.Button(skor_frame2, text="+1", font=("Helvetica", 24), width=5, bg="#5271ff",command=tambah2)
        tombol_tambah.place(x=0, y=230)

        tombol_kurang = tk.Button(skor_frame2, text="-1", font=("Helvetica", 24), width=5, bg="#5271ff", command=kurang2)
        tombol_kurang.place(x=150, y=230)

       
        skor_frame = tk.Frame(self.bg_label, bg="#ff3131")
        skor_frame.place(x=900, y=110, width=300, height=300)
        self.current_page_widgets.append(skor_frame)

        self.skor = tk.IntVar(value=0)

        def tambah():
            self.skor.set(self.skor.get() + 1)

        def kurang():
            self.skor.set(self.skor.get() - 1)

        label = tk.Label(skor_frame, textvariable=self.skor, font=("Helvetica", 128), bg="#ff3131")
        label.place(x=10, y=50)

        tombol_tambah = tk.Button(skor_frame, text="+1", font=("Helvetica", 24), width=5, bg="#ff3131",command=tambah)
        tombol_tambah.place(x=0, y=230)

        tombol_kurang = tk.Button(skor_frame, text="-1", font=("Helvetica", 24), width=5, bg="#ff3131", command=kurang)
        tombol_kurang.place(x=150, y=230)

            def sikaku1():
            messagebox.showinfo("info","Biru di diskualifikasi!")
        
        def kiken1():
            messagebox.showinfo("info", "Biru telah menyerah!")

        
        tombolkiken1 = tk.Button(self.bg_label, text="Kikken",font=("Helvetica", 16), command=kiken1, bg="green", fg="white")
        tombolkiken1.place(x=550, y=730, width=100, height=40)
        self.current_page_widgets.append(tombolkiken1)

        tombolsikaku1 = tk.Button(self.bg_label, text="Shikkaku",font=("Helvetica", 16), command=sikaku1, bg="green", fg="white")
        tombolsikaku1.place(x=400, y=730, width=100, height=40)
        self.current_page_widgets.append(tombolsikaku1)

        def sikaku2():
            messagebox.showinfo("info","Merah di diskualifikasi!")
        
        def kiken2():
            messagebox.showinfo("info", "Merah telah menyerah!")

        
        tombolkiken2 = tk.Button(root, text="Kikken",font=("Helvetica", 16), command=kiken2, bg="green", fg="white")
        tombolkiken2.place(x=1050, y=730, width=100, height=40)
        self.current_page_widgets.append(tombolkiken2)

        tombolsikaku2 = tk.Button(root, text="Shikkaku",font=("Helvetica", 16), command=sikaku2, bg="green", fg="white")
        tombolsikaku2.place(x=900, y=730, width=100, height=40)
        self.current_page_widgets.append(tombolsikaku2)
        

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

        # === PESERTA BIRU ===
        peserta_biru = self.load_peserta_dari_csv("peserta_biru.csv")
        peserta_biru_frame = tk.Frame(self.bg_label, bg="#5271ff")
        peserta_biru_frame.place(x=50, y=420)  # posisi bisa diatur
        self.current_page_widgets.append(peserta_biru_frame)

        judul_biru = tk.Label(peserta_biru_frame, text="Peserta Biru", font=("Helvetica", 14, "bold"), bg="#5271ff", fg="white")
        judul_biru.pack()

        for p in peserta_biru:
            label_peserta = tk.Label(peserta_biru_frame, text=f"{p['Nama']} - {p['Asal']}", bg="#5271ff", fg="white", font=("Helvetica", 10))
            label_peserta.pack(side=tk.RIGHT, padx=20)
        print(p)

        # === PESERTA MERAH ===
        peserta_merah = self.load_peserta_dari_csv("peserta_merah.csv")
        peserta_merah_frame = tk.Frame(self.bg_label, bg="#ff3131")
        peserta_merah_frame.place(x=1250, y=420)
        self.current_page_widgets.append(peserta_merah_frame)

        judul_merah = tk.Label(peserta_merah_frame, text="Peserta Merah", font=("Helvetica", 14, "bold"), bg="#ff3131", fg="white")
        judul_merah.pack()
       
        for p in peserta_merah:
            label_peserta = tk.Label(peserta_merah_frame, text=f"{p['Nama']} - {p['Asal']}", bg="#ff3131", fg="white", font=("Helvetica", 10))
            label_peserta.pack(side=tk.LEFT, padx=20)

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

try:
                img_path = foto_file
                img_pil = Image.open(img_path)
                img_pil = img_pil.resize((180, 210), Image.LANCZOS)
                
                photo_tk = ImageTk.PhotoImage(img_pil)
                self.about_photo_refs.append(photo_tk)

                photo_label = tk.Label(person_frame, image=photo_tk, bg=self.content_bg_color)
                photo_label.pack(pady=5)
                self.current_page_widgets.append(photo_label)

                name_label = tk.Label(person_frame, text=orang_names[i], font=("Basketball", 14), fg="white", bg="black")
                name_label.pack(pady=2)
                self.current_page_widgets.append(name_label)

            except FileNotFoundError:
                print(f"Error: {foto_file} tidak ditemukan. Menampilkan placeholder.")
                placeholder_label = tk.Label(person_frame, text=f"Foto {i+1}\nTidak Ditemukan", 
                                                font=("Arial", 10), width=20, height=10, 
                                                bg="lightgray", fg="red")
                placeholder_label.pack(pady=5)
                self.current_page_widgets.append(placeholder_label)
                
                name_label = tk.Label(person_frame, text=orang_names[i], font=("Arial", 12), bg=self.content_bg_color)
                name_label.pack(pady=2)
                self.current_page_widgets.append(name_label)
             except FileNotFoundError:
                print(f"Error: {foto_file} tidak ditemukan. Menampilkan placeholder.")
                placeholder_label = tk.Label(person_frame, text=f"Foto {i+1}\nTidak Ditemukan", 
                                                font=("Arial", 10), width=20, height=10, 
                                                bg="lightgray", fg="red")
                placeholder_label.pack(pady=5)
                self.current_page_widgets.append(placeholder_label)
                
                name_label = tk.Label(person_frame, text=orang_names[i], font=("Arial", 12), bg=self.content_bg_color)
                name_label.pack(pady=2)
                self.current_page_widgets.append(name_label)

        back_button = tk.Button(
            self.bg_label,
            text="Kembali ke Home",
            command=self.show_home_screen,
            font=("Arial", 12),
            pady=10,
            bg=self.button_normal_bg,
            fg=self.button_text_fg,
            relief="flat",
            activebackground=self.button_hover_bg
        )
        back_button.pack(pady=20)
        self.current_page_widgets.append(back_button)
        self.bind_hover_effects(back_button)
def on_start_button_click(self):
        self.show_new_page()

    def on_about_button_click(self):
        self.show_about_page()

    def on_exit_button_click(self):
        if messagebox.askyesno("Keluar", "Apakah Anda yakin ingin keluar dari aplikasi?"):
            self.root.quit()


if _name_ == "_main_":
    root = tk.Tk()
    app = AplikasiTkinter(root)
    root.mainloop()
