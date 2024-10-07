import tkinter as tk
from PIL import Image, ImageTk
import random


def load_image(path):
    img = Image.open(path)
    return ImageTk.PhotoImage(img)


def on_mouse_move(event):
    canvas.delete("text")
    canvas.create_text(event.x, event.y, text=current_country, fill="red", tags="text", anchor="nw")


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    
    window.geometry(f"{width}x{height}+{x}+{y}")

def set_next_country(pokus):
    global current_country
    if pokus < len(countries):
        current_country = countries[pokus]
        print(f"Hledej: {current_country}")
    else:
        print("Kvíz hotov")
        root.destroy()  

hodnoceni = 0

root = tk.Tk()
root.title("Kvíz o Africe")

window_width = 900
window_height = 1000
center_window(root, window_width, window_height)

def on_click(event):
    global hodnoceni
    global pokus
    if pokus >= len(countries):
        return  

    x, y = event.x, event.y
    print(f"Clicked at {x}, {y}")
    if current_country == "Egypt" and 575 <= x <= 682 and 114 <= y <= 228:
        print("Správně! Klikl jsi na Egypt!")
        hodnoceni += 1
    elif current_country == "Nigeria" and 324 <= x <= 405 and 343 <= y <= 420:
        print("Správně! Klikl jsi na Nigérii")
        hodnoceni += 1
    elif current_country == "Kenya" and 701 <= x <= 765 and 456 <= y <= 554:
        print("Správně! Klikl jsi na Keňu")
        hodnoceni += 1
    elif current_country == "South Africa" and 500 <= x <= 671 and 869 <= y <= 946:
        print("Správně! Klikl jsi na Jihoafrickou republiku")
        hodnoceni += 1
    else:
        print("Špatně, zkus to znovu.")
            
    pokus += 1

    set_next_country(pokus)


map_path = r"c:\Users\Tom\Desktop\skola\pcv\python-projekt-main\projekt-python-master\01-basics\africa.jpg"
img = load_image(map_path)

canvas = tk.Canvas(root, width=img.width(), height=img.height())
canvas.pack()

canvas.create_image(0, 0, image=img, anchor="nw")


countries = ["Egypt", "Nigeria", "South Africa", "Kenya"]
current_country = None


canvas.bind("<Motion>", on_mouse_move)


canvas.bind("<Button-1>", on_click)


pokus = 0
set_next_country(pokus)

root.mainloop()


vyhodnoceni = tk.Tk()
vyhodnoceni.title("Vyhodnocení kvízu")
window_width = 400
window_height = 200
center_window(vyhodnoceni, window_width, window_height)

hlaska = tk.Label(vyhodnoceni, text=f"Tvoje body: {hodnoceni}/4", font=("Helvetica", 18, "bold"))
hlaska.pack(pady=20)
odejit = tk.Button(vyhodnoceni, text="Odejít", command=lambda:vyhodnoceni.destroy())
odejit.pack(pady=40)
vyhodnoceni.mainloop()
