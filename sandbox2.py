import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os


# root window
root = tk.Tk()
root.geometry("1200x800")
root.title('Floor Plan')

# configure the grid
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)
root.grid_columnconfigure(0, minsize=100, weight=1, uniform="foo")
root.grid_columnconfigure(1, minsize=100, weight=1, uniform="foo")
root.grid_columnconfigure(2, minsize=100, weight=1, uniform="foo")
root.grid_columnconfigure(3, minsize=100, weight=1, uniform="foo")
root.grid_columnconfigure(4, minsize=100, weight=1, uniform="foo")
root.grid_columnconfigure(5, minsize=100, weight=1, uniform="foo")




# # Months going horizontal on top
# month1 = tk.Label(root, text="  Jan")
# month1.grid(column=1, row=0, padx=0, pady=0,)

# month2 = tk.Label(root, text="  Feb")
# month2.grid(column=2, row=0, padx=0, pady=0,)

# month3 = tk.Label(root, text="  Mar")
# month3.grid(column=3, row=0, padx=0, pady=0,)

# Same thing as above with an array
label_arr = []
label_arr.append(tk.Label(root, text="  Jan"))
label_arr[0].grid(column=1, row=0, padx=0, pady=0)

label_arr.append(tk.Label(root, text="  Feb"))
label_arr[1].grid(column=2, row=0, padx=0, pady=0)

label_arr.append(tk.Label(root, text="  Mar"))
label_arr[2].grid(column=3, row=0, padx=0, pady=0,)

label_arr.append(tk.Label(root, text="  Apr"))
label_arr[3].grid(column=4, row=0, padx=0, pady=0,)

# Builds going vertical on the left side
build1 = tk.Label(root, text="System")
build1.grid(column=0, row=1)

build1 = tk.Label(root, text="EVT")
build1.grid(column=0, row=2)




# Create the Canvas

my_canvas = tk.Canvas(root)
my_canvas.grid(column=1, row=1, columnspan=20)

my_canvas2 = tk.Canvas(root)
my_canvas2.grid(column=1, row=2, columnspan=20)

# Add the circle into the window
global blue_circle
blue_circle = tk.PhotoImage(file="./images/bluecircle.png")
blue_circle = blue_circle.subsample(30)
my_canvas.create_image(100,100,image=blue_circle)

global blue_circle2
blue_circle2 = tk.PhotoImage(file="./images/bluecircle.png")
blue_circle2 = blue_circle2.subsample(30)
my_canvas2.create_image(100,100,image=blue_circle2)

# Add the text
global my_text
my_text = my_canvas.create_text(100,100, text="hello", fill='white')

global my_text2
my_text2 = my_canvas2.create_text(100,100, text="hello", fill='white')

def move(e):
	global blue_circle
	blue_circle = tk.PhotoImage(file="./images/bluecircle.png")
	blue_circle = blue_circle.subsample(30)     # Since we have to copy these lines so frequently, recommend we create a class or function
	blue_circle_img = my_canvas.create_image(e.x,100, image=blue_circle) # now locaked to the 100 pixel mark

	# Update label position and coordinates
	my_canvas.coords(my_text, e.x, 120)
	my_canvas.tag_raise(my_text)            # Bring the text to the front, otherwise it is behind the circle.
	my_canvas.itemconfig(my_text, text=str(e.x) + "," + str(e.y))

	

def move2(e):
	global blue_circle2
	blue_circle2 = tk.PhotoImage(file="./images/bluecircle.png")
	blue_circle2 = blue_circle2.subsample(30)     # Since we have to copy these lines so frequently, recommend we create a class or function
	blue_circle_img2 = my_canvas2.create_image(e.x,100, image=blue_circle2) # now locaked to the 100 pixel mark

	# Update label position and coordinates
	my_canvas2.coords(my_text2, e.x, 120)
	my_canvas2.tag_raise(my_text2)            # Bring the text to the front, otherwise it is behind the circle.
	my_canvas2.itemconfig(my_text2, text=str(e.x) + "," + str(e.y))


my_canvas.bind('<B1-Motion>', move)
my_canvas2.bind('<B1-Motion>', move2)


root.mainloop()