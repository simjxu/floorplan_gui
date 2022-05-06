import tkinter as tk
from tkinter import PhotoImage, ttk

root = tk.Tk()
root.geometry("1000x800")
w = 800
h = 600
x = w/2
y = h/2

img = PhotoImage(file="/Users/simonxu/Documents/Github-simjxu/floorplan_gui/fp_images/test.png")

# Make image half as small
img = img.subsample(2)

my_canvas = tk.Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)
my_canvas.create_image(0,0, anchor="nw", image=img)

def move(e):
    my_label.config(text="Coords: "+str(e.x)+","+str(e.y))

my_label = tk.Label(root, text="", fg="white")
my_label.pack(pady=20)

my_canvas.bind("<B1-Motion>", move)

# Text box placement
new_label = my_canvas.create_text(206, 162,text="TESTER",fill="black")
# new_label.place(x=100, y=100)

# Create a diamond
points = [5,1, 3,4, 5,7, 7,4]
scaled_points = [i*3 for i in points]

shape = my_canvas.create_polygon(scaled_points, fill="gray")

def change_position(points, x, y):
    # Find center coords of the polygon
    x0 = (points[7]+points[3])/2
    y0 = (points[6]+points[1])/2

    # Calculate x and y distance to new position
    xdiff = x - x0
    ydiff = y - y0

    # Add x difference to x, y difference to y
    points[::2] = [i+xdiff for i in points[::2]]        # Add xdiff to odd points
    points[1::2] = [i+ydiff for i in points[1::2]]      # add ydiff to even points

    return points

newshape = my_canvas.create_polygon(change_position(scaled_points, 100,100), fill="gray")

# root.configure(bg="white")
root.mainloop()
