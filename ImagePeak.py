import os
import tkinter.filedialog
import tkinter.ttk as ttk
from tkinter import *

from PIL import Image, ImageTk

# Create the main application window
root = Tk()
root.config(bg='#000000')  # Set the background color to black
root.resizable(False, False)  # Disable window resizing
root.title("ImagePeak")  # Set the title of the application

# Load the icon image
icon_image = PhotoImage(file='icon.png')  # Replace 'icon.png' with your icon image file
# Set the icon for the application
root.iconphoto(True, icon_image)
root.geometry('800x600')  # Set the initial window size

# Function to display the pop-up menu
def popup_menu(e):
    menu_bar.tk_popup(x=e.x_root, y=e.y_root)

# Initialize variables for images and their names
img_list = []
img_vars = []
VALID_IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg')

# Function to display the main image when a thumbnail is clicked
def display_images(index):
    image_dp_label.config(image=img_list[index][1])
    canvas.xview_moveto(0)  # Reset canvas view to show the whole main image

# Function to load images from the selected directory
def load_images():
    path = tkinter.filedialog.askdirectory()

    # Filter valid image files
    img_files = [f for f in os.listdir(path) if os.path.splitext(f)[1].lower() in VALID_IMAGE_EXTENSIONS]

    # Create thumbnail and main images and store them in img_list
    for r in range(0, len(img_files)):
        img_list.append([
            ImageTk.PhotoImage(Image.open(os.path.join(path, img_files[r])).resize((90, 90), Image.BILINEAR)),  # Increase thumbnail size

            ImageTk.PhotoImage(Image.open(os.path.join(path, img_files[r])).resize((500, 300), Image.BILINEAR))  # Increase main image size
        ])
        img_vars.append(f'img_{r}')

    # Create buttons with thumbnails for each image
    for n in range(len(img_vars)):
        globals()[img_vars[n]] = Button(slider, image=img_list[n][0], bd=0, command=lambda n=n: display_images(n),
                                        bg='black', fg='white', highlightthickness=0)
        globals()[img_vars[n]].pack(side=LEFT)

# Create the button_menu for the pop-up menu
button_menu = Button(root, text="≡", bd=0, font=('Bold', 30), bg='black', fg='white', highlightthickness=0)
button_menu.pack(side=TOP, anchor=W, pady=20, padx=10)
button_menu.bind('<Button-1>', popup_menu)

# Create the menu bar and add commands
menu_bar = Menu(root, tearoff=False)
menu_bar.add_command(label='Open Folder', command=load_images)

# Attach the menu bar to the root window
root.config(menu=menu_bar)

# Create the slider frame at the bottom of the window for the thumbnail images
slider = Frame(root, height=100, bg='black', highlightthickness=0)
slider.pack(side=BOTTOM, fill=X)

# Create the main image label and set background and foreground colors
image_dp_label = Label(root, bg='black', fg='white', highlightthickness=0)
image_dp_label.pack(side=TOP, fill=BOTH, expand=True)  # Use fill and expand to center the main image

# Create the canvas for displaying thumbnail images
canvas = Canvas(root, height=50, width=500, bg='black', highlightthickness=0)
canvas.pack(side=BOTTOM, fill=X)

# Create and configure the horizontal scroll bar
scroll_bar = ttk.Scrollbar(root, orient=HORIZONTAL, command=canvas.xview)
scroll_bar.pack(side=BOTTOM, fill=X)
scroll_bar.config(command=canvas.xview)

# Configure the canvas to respond to the scroll bar
canvas.configure(xscrollcommand=scroll_bar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

# Create a frame inside the canvas to hold the thumbnail images
slider = Frame(canvas, bg='black', highlightthickness=0)
canvas.create_window((0, 0), window=slider, anchor=NW)

# Start the main event loop
root.mainloop()
