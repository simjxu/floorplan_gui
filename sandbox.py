from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title('Test Coordinates')
root.geometry("800x600")

w = 600
h = 400
x = w/2
y = h/2

# Create the canvas
my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(fill=BOTH, expand=True)

# Add the first image to the canvas
layout_img = PhotoImage(file="./images/layout.png")
my_canvas.create_image(1,1, image=layout_img, anchor='nw')

# Add the 2nd image to the canvas, subsample makes the image smaller.
blue_circle = PhotoImage(file="./images/bluecircle.png")
blue_circle = blue_circle.subsample(10)
my_canvas.create_image(1,1, image=blue_circle, anchor='nw')


# # Puts the image of the layout into the canvas and resizes it based upon the window size
# def resize_image(e):
#     global image, resized, image2
#     # open image to resize it
#     image = Image.open("./images/layout.png")
#     # resize the image with width and height of root
#     resized = image.resize((e.width, e.height), Image.ANTIALIAS)

#     image2 = ImageTk.PhotoImage(resized)
#     my_canvas.create_image(0,0, image=image2, anchor='nw')

#     # Add the blue circle to the canvas
#     blue_circle = PhotoImage(file="./images/bluecircle.png")
#     my_canvas.create_image(100,100, image=blue_circle, anchor='nw')

# def move(e):
#     blue_circle = PhotoImage(file="./images/bluecircle.png")
#     blue_circle_img = my_canvas.create_image(e.x,e.y, image=blue_circle)

#     my_label.config(text="Coordinate: x:" + str(e.x) + " " + " y:" + str(e.y))


# my_label = Label(root, text="")
# my_label.pack(pady=20)

# # Button of mouse tracking
# my_canvas.bind('<B1-Motion>', move)
# my_canvas.bind("<Configure>", resize_image)

root.mainloop()