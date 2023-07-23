import os
import tkinter.filedialog as tk_file
import tkinter.ttk as ttk
from tkinter import *

from PIL import Image, ImageTk

root= Tk()
root.title("ImagePeak")
# Load the icon image
icon_image = PhotoImage(file='icon.png')  # Replace 'icon.png' with your icon image file
# Set the icon for the application
root.iconphoto(True, icon_image)
root.geometry('600x600')

def popup_menu(e):
    menu_bar.tk_popup(x=e.x_root, y=e.y_root)

img_list = []
img_vars = []

def load_images():
    path = tk_file.askdirectory()

    img_files = os.listdir(path)

    for r in range(0, len(img_files)):
        img_list.append([
            ImageTk.PhotoImage(Image.open(path+'/' +img_files[r]).resize((30,30),Image.ATIALIAS)),

            ImageTk.PhotoImage(Image.open(path+'/' +img_files[r]).resize(400,300))
        ])
        img_vars.append(f'img_{r}')

button_menu= Button(root, text= "≡", bd= 0, font= ('Bold', 30))
button_menu.pack(side=TOP, anchor=W, pady= 20, padx= 10)
button_menu.bind('<Button-1>', popup_menu)

menu_bar = Menu(root, tearoff= False)
menu_bar.add_command(label = 'Open Folder')

image_dp_label = Label(root)
image_dp_label.pack(anchor= CENTER)

canvas = Canvas(root, height= 50, width= 400)
canvas.pack(side = BOTTOM, fill= X)

scroll_bar = ttk.Scrollbar(root, orient= HORIZONTAL)
scroll_bar.pack(side = BOTTOM, fill= X)
scroll_bar.config(command = canvas.xview)


canvas.configure(xscrollcommand=scroll_bar.set)
canvas.bind('<Configure>', lambda e: canvas.bbox('all'))

slider = Frame(canvas)
canvas.create_window((0,0), window= slider, anchor= NW)
root.mainloop()root.mainloop()