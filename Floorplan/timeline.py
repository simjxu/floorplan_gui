import tkinter as tk
import math
class Timeline:
  
	MARKER_RADIUS = 8 # All marker radii will be the same

	def __init__(self, parent, **kwargs):
		self.START_MONTH = parent.START_MONTH

		# Pull in variables from the parent class, MainApplication
		self.num_days = kwargs['num_days']
		self.num_months = kwargs['num_months']
		self._MINSIZE = kwargs['minsize']
		
		# This needs to move into the __init__ function, from reading from the yaml
		self.marker_ypos = self._MINSIZE/2+self.MARKER_RADIUS/2	# marker needs to be in the middle of the row
		self.array = [(25,self.marker_ypos),(50,self.marker_ypos),(75,self.marker_ypos)]

		self.canvas = tk.Canvas(parent.mainframe)
		# self.canvas.pack()
		self.canvas.grid(column=kwargs['column'], row=kwargs['row'], rowspan=kwargs['rowspan'], \
				columnspan=kwargs['columnspan'])
		self.canvas.configure(width=self._MINSIZE*(self.num_months), height=self._MINSIZE, bg='green')

		# to keep all IDs and its start position
		self.ovals = {}
		self.texts = {}

		# Create markers for every item in the array
		for item in self.array:
			# create oval and get its ID
			item_id = self.canvas.create_circle(item[0], item[1], self.MARKER_RADIUS, \
				fill='blue', outline='white', tags='id')
			# remember ID and its start position
			self.ovals[item_id] = item

			# Create texts and store the text tag id for reference during move
			self.texts[item_id] = self.canvas.create_text(item[0], item[1]+2*self.MARKER_RADIUS, \
				text="hello", fill='white')

			self.canvas.tag_bind('id', '<ButtonPress-1>', self.start_move)
			self.canvas.tag_bind('id', '<B1-Motion>', self.move)
			self.canvas.tag_bind('id', '<ButtonRelease-1>', self.stop_move)

			# # to remember selected item
			# self.selected = None

	def update_date(self, x):
		# Create the text that goes under the marker indicating the date
		# x is the position that the mouse moves the marker to
		# 1. Divide the pixel count by 100
		# 2. Round down to integer
		# 3. Map the integer to the month Start Month + integer
		month_iter = math.floor(x/100)
		month_num = self.START_MONTH+month_iter
		month_num = month_num if month_num <= 12 else month_num-12  # Rollover to January

		return str(month_num) + "/" + \
			str(math.ceil((x+1-100*month_iter)/100*self.num_days[month_iter]))
		# TODO: Set bounds so that the marker doesn't go out of bounds

	def start_move(self, event):
		# find all clicked items
		self.selected = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
		# get first selected item
		self.selected = self.selected[0]

		# get selected text tag
		self.selected_text = self.canvas.find_withtag(self.texts[self.selected])

	def move(self, event):
		circle_coords = self.canvas.coords(self.selected)
		x0 = circle_coords[0]   # currently unused, go off of the mouse position
		y0 = circle_coords[1]
		x1 = circle_coords[2]   # currently unused, go off of the mouse position
		y1 = circle_coords[3]

		# move selected item, hold y position
		self.canvas.coords(self.selected, event.x-self.MARKER_RADIUS, \
				y0, event.x+self.MARKER_RADIUS,y1)

		# Also move the label position and date
		self.canvas.coords(self.selected_text, event.x, \
				self.marker_ypos+2*self.MARKER_RADIUS)
		self.canvas.tag_raise(self.selected_text)
		self.canvas.itemconfig(self.selected_text, text=str(self.update_date(event.x)))

	def stop_move(self, event):
		pass