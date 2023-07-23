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

button_menu= Button(root, text= "≡", bd= 0, font= ('Bold', 30))
button_menu.pack(side=TOP, anchor=W, pady= 20, padx= 10)
button_menu.bind('<Button-1>', popup_menu)

menu_bar = Menu(root, tearoff= False)
menu_bar.add_command(label = 'Open Folder')



root.mainloop()