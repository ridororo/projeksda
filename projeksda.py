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
