from tkinter import *
from PIL import ImageTk, Image
import os


root = Tk()
root.title('Test Coordinates')
root.geometry("800x600")

tk_legend = Tk()
tk_legend.title('Selector')
tk_legend.geometry("150x400")

w = 600
h = 400
x = w/2
y = h/2

# Create the canvas
my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(fill=BOTH, expand=True)

leg_canvas = Canvas(tk_legend, width=w, height=h, bg="white")
leg_canvas.pack(fill=BOTH, expand=True)

# Add the image to the canvas


# Puts the image of the layout into the canvas and resizes it based upon the window size
def resize_window_cb(e):
    # Resize the floorplan layout
    global layout, layout_resized, layout2
    # open image to resize it
    layout = Image.open("./images/layout.png")
    # resize the image with width and height of root
    layout_resized = layout.resize((e.width, e.height), Image.ANTIALIAS)

    layout2 = ImageTk.PhotoImage(layout_resized)
    my_canvas.create_image(0,0, image=layout2, anchor='nw')


    # Add the blue circle to the canvas, also resize, and reposition
    global blue_circle
    blue_circle = PhotoImage(file="./images/bluecircle.png")
    blue_circle = blue_circle.subsample(10)
    my_canvas.create_image(100,100, image=blue_circle)

    # Create a text
    global my_text
    my_text = my_canvas.create_text(100,100, text="hello", fill='#000000')


def move(e):
    # Update circle position
    global blue_circle
    blue_circle = PhotoImage(file="./images/bluecircle.png")
    blue_circle = blue_circle.subsample(10)     # Since we have to copy these lines so frequently, recommend we create a class or function
    blue_circle_img = my_canvas.create_image(e.x,100, image=blue_circle) # now locaked to the 100 pixel mark


    # Update label position and coordinates
    my_canvas.coords(my_text, e.x, 100)
    my_canvas.tag_raise(my_text)            # Bring the text to the front, otherwise it is behind the circle.
    my_canvas.itemconfig(my_text, text=str(e.x) + "," + str(e.y))
    
    # Update label coordinates
    my_label.config(text="Coordinate: x:" + str(e.x) + " " + " y:" + str(e.y))

my_label = Label(root, text="")
my_label.pack(pady=20)

# Button of mouse tracking
my_canvas.bind('<B1-Motion>', move)
my_canvas.bind("<Configure>", resize_window_cb)

root.mainloop()