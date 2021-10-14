import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os

# class Circle(tk.Canvas):
# 	MARKER_RADIUS = 6

# 	def __init__(self, *args, **kwargs):
# 		# super().__init__(*args, **kwargs)
# 		self.canvas = tk.Canvas.__init__(self)
# 		self.place(relx=0,rely=1)
# 		self.grid(column=kwargs['column'], row=kwargs['row'], columnspan=1, rowspan=1)
# 		self.configure(bg='black', height=27, width=27, highlightthickness=0)

# 		self.my_circle = self.create_oval(2,2,25,25, fill="blue", outline="white", width=2)
# 		# self.my_circle = self.create_oval(kwargs['x0'], kwargs['x1'], kwargs['y0'], \
# 		# 	 kwargs['y1'], fill="blue", outline="white", width=2)
# 		self.make_draggable(self)

# 	# def make_draggable(self, widget):
# 	# 	widget.bind("<Button-1>", self.on_drag_start)
# 	# 	widget.bind("<B1-Motion>", self.on_drag_motion)

# 	# def on_drag_start(self, event):
# 	# 	widget = event.widget
# 	# 	widget._drag_start_x = event.x
# 	# 	widget._drag_start_y = event.y

# 	# def on_drag_motion(self, event):
# 	# 	widget = event.widget
# 	# 	x = widget.winfo_x() - widget._drag_start_x + event.x
# 	# 	y = widget.winfo_y() - widget._drag_start_y + event.y
# 	# 	widget.place(x=x, y=y)
	
# 	def make_draggable(self, widget):
# 		# widget.bind("<Button-1>", self.on_drag_start)
# 		widget.bind("<B1-Motion>", self.on_drag_motion)

# 	def on_drag_start(self, event):
# 		widget = event.widget
# 		widget._drag_start_x = event.x
# 		widget._drag_start_y = event.y

# 	def on_drag_motion(self, e):
# 		# Callback when moving the marker
# 		circle_coords = self.coords(self.my_circle)      # Returns top left and bottom right corners

# 		x0 = circle_coords[0]   # currently unused, go off of the mouse position
# 		y0 = circle_coords[1]
# 		x1 = circle_coords[2]   # currently unused, go off of the mouse position
# 		y1 = circle_coords[3]
# 		self.coords(self.my_circle, e.x-self.MARKER_RADIUS, y0, e.x+self.MARKER_RADIUS, y1)

#         # # Update label position and date
#         # self.coords(my_text, e.x, 60)
#         # self.tag_raise(my_text)            # Bring the text to the front, otherwise it is behind the circle.
#         # self.itemconfig(my_text, text=str(self.update_date(e.x)))
			
class Circle(tk.Canvas):
	MARKER_RADIUS = 6

	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent)

		my_circle = super().create_oval(2,2,25,25, fill="blue", outline="white", width=2)
		# self.my_circle = self.create_oval(kwargs['x0'], kwargs['x1'], kwargs['y0'], \
		# 	 kwargs['y1'], fill="blue", outline="white", width=2)
		# self.make_draggable(self)
	
	def make_draggable(self, widget):
		# widget.bind("<Button-1>", self.on_drag_start)
		widget.bind("<B1-Motion>", self.on_drag_motion)

	def on_drag_start(self, event):
		widget = event.widget
		widget._drag_start_x = event.x
		widget._drag_start_y = event.y

	def on_drag_motion(self, e):
		# Callback when moving the marker
		circle_coords = self.coords(self.my_circle)      # Returns top left and bottom right corners

		x0 = circle_coords[0]   # currently unused, go off of the mouse position
		y0 = circle_coords[1]
		x1 = circle_coords[2]   # currently unused, go off of the mouse position
		y1 = circle_coords[3]
		self.coords(self.my_circle, e.x-self.MARKER_RADIUS, y0, e.x+self.MARKER_RADIUS, y1)

        # # Update label position and date
        # self.coords(my_text, e.x, 60)
        # self.tag_raise(my_text)            # Bring the text to the front, otherwise it is behind the circle.
        # self.itemconfig(my_text, text=str(self.update_date(e.x)))
			

class MainCanvas(tk.Canvas):
	def __init__(self, *args, **kwargs):
		self.canvas = tk.Canvas.__init__(self)

		# Create canvas that covers the the entire row
		self.grid(column=0, row=0, columnspan=10, rowspan=1)
		self.configure(bg='white', height=50, width=500)

		my_circle = []
		# for i in range(2):
		# 	my_circle.append(Circle(self,column=i, row=0))

		my_circle1 = Circle(self)
		# self.my_circle2 = Circle(self)
		
		# my_circle = self.create_oval(2,2,25,25, fill="blue", outline="white", width=2)

if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("1200x800")
	new_canvas = MainCanvas(root)
	root.mainloop()
