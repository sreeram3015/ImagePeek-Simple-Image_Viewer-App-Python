from tkinter import *

from PIL import Image, ImageTk

root= Tk()
root.title("ImagePeak")
# Load the icon image
icon_image = PhotoImage(file='icon.png')  # Replace 'icon.png' with your icon image file
# Set the icon for the application
root.iconphoto(True, icon_image)
root.geometry('600x600')


root.mainloop()