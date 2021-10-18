import tkinter as tk
import os
import math
import calendar
import datetime
from YAMLoutput import YAMLoutput

ymlFile = './Sandbox/example.yaml'

# Input width of each cell
_MINSIZE = 100

# Add the _create_circle function ot the Canvas function, makes it easier to create a circle
def _create_circle(self, x, y, r, **kwargs):
	return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

class MainApplication:
	_NUMBER_OF_DAYS = []
	_NUMBER_OF_MONTHS = 0
	START_MONTH = 0
	START_YEAR = 0
	END_MONTH = 0
	END_YEAR = 0

	def __init__(self, parent):
		# import the yaml file data
		self.yaml_dateobj = YAMLoutput(self, file=ymlFile)

		self.START_MONTH = self.yaml_dateobj.START_MONTH
		self.START_YEAR = self.yaml_dateobj.START_YEAR
		self.END_MONTH = self.yaml_dateobj.END_MONTH
		self.END_YEAR = self.yaml_dateobj.END_YEAR

		# print(START_YEAR)
		# print(START_MONTH)

		# Update the number of columns
		self._NUMCOLS = 2		# Start at 1 to include the builds column, first month
		month_ptr = self.START_MONTH
		year_ptr = self.START_YEAR
		while month_ptr != self.END_MONTH or year_ptr != self.END_YEAR:
			self._NUMCOLS += 1
			if month_ptr == 12:
				month_ptr = 1
				year_ptr += 1
			else:
				month_ptr += 1

		# Update the number of rows
		self._NUMROWS = len(self.yaml_dateobj.BUILD_NAMES) + 1
		
		# tk.Frame for the Main Application, for reference in child class Timeline
		self.mainframe = tk.Frame(parent, width=1000, height=1000)
		self.mainframe.grid(column=0, row=0, rowspan=20, columnspan=20)		# max out at 20 rows, 20 cols right now

		# Configure size of the grid on root
		for i in range(self._NUMCOLS):
			root.columnconfigure(i, minsize=_MINSIZE)
		for i in range(self._NUMROWS):
				root.columnconfigure(i, minsize=_MINSIZE)


		# print(self.START_MONTH)
		# print(self.START_YEAR)
		# print(END_MONTH)
		# print(END_YEAR)
		# Create top row of months, get array of days, set column/rowspan
		self._NUMBER_OF_MONTHS = self.get_num_months()
		self._NUMBER_OF_DAYS = self.create_months()

		# print(self._NUMBER_OF_MONTHS)
		# print(self._NUMBER_OF_DAYS)
		
		# Create Timeline opbjects
		self.timeline_arr = []
		for i in range(len(self.yaml_dateobj.BUILD_NAMES)):
			self.timeline_arr.append(Timeline(self, column=1, row=i+1, columnspan=self._NUMCOLS-1, rowspan=1, \
				num_days=self._NUMBER_OF_DAYS, num_months=self._NUMBER_OF_MONTHS))

		# Builds going vertical on the left side
		for i in range(len(self.yaml_dateobj.BUILD_NAMES)):
			self.build = tk.Label(self.mainframe, text=self.yaml_dateobj.BUILD_NAMES[i])
			self.build.grid(column=0, row=i+1, padx=10, pady=0)


	def get_num_months(self):
		# print(self.START_MONTH)
		# print(self.START_YEAR)
		start_date = datetime.datetime(self.START_YEAR,self.START_MONTH,1)
		end_date = datetime.datetime(self.END_YEAR, self.END_MONTH, 1)
		# print(start_date)
		# print(end_date)
		return (end_date.year - start_date.year) * 12 \
			+ (end_date.month - start_date.month) + 1

    # Function to get the months and create array of days
	def create_months(self):
		monthdays_arr = []
		num_months = self._NUMBER_OF_MONTHS

		# Create the month labels on the first row
		label_arr = []
		year = self.START_YEAR
		month = self.START_MONTH
		for i in range(num_months):
			# Account for months rollover at end of year
			if month==13:
				month = 1
				year += 1

			label_arr.append(tk.Label(self.mainframe, \
				text=calendar.month_abbr[month]))
			# MAGIC NUMBER: padx on right needs to be 15 to have the marker match well on label
			label_arr[i].grid(column=i+1, row=0, padx=(0,15), pady=0)
			monthdays_arr.append(calendar.monthrange(year,month)[1])
			month += 1

		return monthdays_arr

	def create_builds(self):
		a = 0
		return a

class Timeline(MainApplication):
  
	MARKER_RADIUS = 8 # All marker radii will be the same
	marker_ypos = _MINSIZE/2+MARKER_RADIUS/2	# marker needs to be in the middle of the row

	# This needs to move into the __init__ function, from reading from the yaml
	array = [(25,marker_ypos),(50,marker_ypos),(75,marker_ypos)]

	def __init__(self, parent, **kwargs):
		self.START_MONTH = parent.START_MONTH

		self.num_days = kwargs['num_days']
		self.num_months = kwargs['num_months']

		self.canvas = tk.Canvas(parent.mainframe)
		# self.canvas.pack()
		self.canvas.grid(column=kwargs['column'], row=kwargs['row'], rowspan=kwargs['rowspan'], \
				columnspan=kwargs['columnspan'])
		self.canvas.configure(width=_MINSIZE*(self.num_months), height=_MINSIZE, bg='green')

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
		print(x)
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


if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("800x600")
	d = MainApplication(root)
	root.mainloop()