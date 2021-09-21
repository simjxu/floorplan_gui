from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Test Coordinates')
root.geometry("800x600")

w = 600
h = 400
x = w/2
y = h/2

my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(fill=BOTH, expand=True)

img = ImageTk.PhotoImage(file="./layout.png")
my_image = my_canvas.create_image(260,125,image=img)

def resize_image(e):
    global image, resized, image2
    # open image to resize it
    image = Image.open("./layout.png")
    # resize the image with width and height of root
    resized = image.resize((e.width, e.height), Image.ANTIALIAS)

    image2 = ImageTk.PhotoImage(resized)
    my_canvas.create_image(0,0, image=image2, anchor='nw')


def move(e):
    my_label.config(text="Coordinate: x:" + str(e.x) + " " + " y:" + str(e.y))


my_label = Label(root, text="")
my_label.pack(pady=20)

# Button of mouse tracking
my_canvas.bind('<B1-Motion>', move)
my_canvas.bind("<Configure>", resize_image)

root.mainloop()