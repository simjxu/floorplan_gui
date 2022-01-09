import tkinter as tk
import math
from YAMLoutput import YAMLoutput
class Timeline:
  
	MARKER_RADIUS = 8 # All marker radii will be the same
	TEXT_COLOR = 'black'
	MARKER_COLOR = 'orange'

	def __init__(self, parent, **kwargs):

		# Pull in variables from the parent class, MainApplication
		self.START_MONTH = kwargs['start_month']
		self.START_YEAR = kwargs['start_year']
		self.num_days = kwargs['num_days']
		self.num_months = kwargs['num_months']
		self.MIN_XLEN = kwargs['min_xlen']
		self.MIN_YLEN = kwargs['min_ylen']
		self.date_array = kwargs['date_array']
		self.label_array = kwargs['label_array']
		self.color_array = kwargs['color_array']
		self.build_name = kwargs['build_name']

		self.parent = parent
		
		# This needs to move into the __init__ function, from reading from the yaml
		self.array = []
		self.marker_ypos = self.MIN_YLEN/2+self.MARKER_RADIUS/2	# marker needs to be in the middle of the row
		for i in range(len(self.date_array)):
			# Append tuple into the array
			self.array.append((self.date2pos(self.date_array[i]),self.marker_ypos))

		self.canvas = tk.Canvas(parent.mainframe)
		self.canvas.grid(column=kwargs['column'], row=kwargs['row'], rowspan=kwargs['rowspan'], \
			columnspan=kwargs['columnspan'], sticky='news')
		self.canvas.configure(width=self.MIN_XLEN*(self.num_months), height=self.MIN_YLEN, bg='white', \
			highlightthickness=1)

		# to keep all IDs and its start position
		self.ovals = {}			# Holds the object IDs for circles
		self.dates = {}			# Holds the object IDs for dates that go under the marker
		self.labels = {}		# Holds the object IDs for labels that go over the marker

		# Create markers for every item in the array
		for item in self.array:
			i = self.array.index(item)			# Get the index of the item

			# create oval and get its ID
			item_id = self.canvas.create_circle(item[0], item[1], self.MARKER_RADIUS, \
				fill=self.color_array[i], \
					outline='black', width=4, tags='id')
			# remember ID and its start position
			self.ovals[item_id] = item

			# Create labels and store the label tag_id for reference during move
			self.labels[item_id] = self.canvas.create_text(item[0], item[1]-2*self.MARKER_RADIUS, \
				text=self.label_array[i], fill=self.TEXT_COLOR)

			# Create dates and store the date tag id for reference during move
			date_str = self.pos2date(item[0])
			# print(date_str)
			self.dates[item_id] = self.canvas.create_text(item[0], item[1]+2*self.MARKER_RADIUS, \
				text=date_str[:-3], fill=self.TEXT_COLOR)
			
			# # Print the date texts
			# print(self.canvas.itemcget(self.dates[item_id], 'text'))

			# Tie callback function to mouse actions
			self.canvas.tag_bind('id', '<ButtonPress-1>', self.start_move)
			self.canvas.tag_bind('id', '<B1-Motion>', self.move)
			self.canvas.tag_bind('id', '<ButtonRelease-1>', self.stop_move)

		# MENU TEST
		self.popup_menu = tk.Menu(tearoff=0)
		self.popup_menu.add_command(label="Create Marker",
																		command=self.create_marker)

		self.canvas.bind("<Button-2>", self.popup)
		# probably will need to create a second one for the markers

	def create_new_marker(self, pos_x, pos_y):
		print("placeholder")
		# move everything in the marker creation to this function so you can reuse it for the popup marker
		

	# def pos2date(self, pos):
	# 	# Takes position value (not integer right now) as an input and outputs a string 
	# 	# without the year, e.g. 9/11
	# 	month_idx = math.floor(pos/self.MIN_XLEN)
	# 	year = self.START_YEAR
	# 	month = self.START_MONTH + month_idx
	# 	if month/12 > 1:			# CAREFUL... Hopefully type(month)==int
	# 		year += math.floor(month/12)
	# 		month = month-12*math.floor(month/12)
	# 	day = self.num_days[month_idx] * ((pos-month_idx*self.MIN_XLEN)/self.MIN_XLEN)
	# 	day = math.ceil(day)

	# 	# # For Debug
	# 	# return str(math.floor(pos))

	# 	# # Show full year string
	# 	return str(month) + "/" + str(day) + "/" + str(year)[2:]
	# 	# return str(month) + "/" + str(day) 


	def date2pos(self, datestr):
		# Convert the date string into a pixel position
		# 1. Pull out the month, day, and year into integers
		# 2. Find Month index based upon start month and year
		# 3. Multiply month index by MINSIZE, then add days/number_days_in_month * MINSIZE
		m_d_y = datestr.split('/')
		m = int(m_d_y[0])
		d = int(m_d_y[1])
		y = int(m_d_y[2])+2000 # Need to add 2000 (won't work for after year 2099, but who cares)

		if m < self.START_MONTH:
			month_idx = m+12 - self.START_MONTH + (y-1-self.START_YEAR)*12
		else:
			month_idx = m - self.START_MONTH + (y-self.START_YEAR)*12

		# d-0.5 to avoid edge cases at the edge of month (12/0 when it should be 11/30)
		return self.MIN_XLEN*month_idx + (d-0.5)/self.num_days[month_idx]*self.MIN_XLEN

	def pos2date(self, x):
		# Create the text that goes under the marker indicating the date
		# x is the position that the mouse moves the marker to
		# 1. Divide the pixel count by 100
		# 2. Round down to integer
		# 3. Map the integer to the month Start Month + integer
		month_iter = math.floor(x/self.MIN_XLEN)
		month_num = self.START_MONTH+month_iter
		year = self.START_YEAR
		if month_num <= 12:
			month_num = month_num
		else: 
			# See how many years it is covering
			while month_num > 12:
				month_num -= 12
				year += 1
			# n_yrs = math.floor((month_num/12)) 
			# month_num = month_num-12*n_yrs 					# Rollover to January
			# year = self.START_YEAR + n_yrs

		return str(month_num) + "/" + \
			str(math.ceil((x+1-self.MIN_XLEN*month_iter)/self.MIN_XLEN*self.num_days[month_iter])) + \
			"/" + str(year)[2:]
		# TODO: Set bounds so that the marker doesn't go out of bounds

	def start_move(self, event):
		# find all clicked items
		self.selected = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
		# get first selected item
		self.selected_arr = []
		self.selected_arr.append(self.selected[0])

		# get selected label tag (add it to the first index in an array)
		self.selected_label = self.canvas.find_withtag(self.labels[self.selected[0]])
		
		# print(self.selected)
		# print(self.labels)
		# print(self.dates)
		# print(self.ovals)
		# print(self.selected_label)
		# print(self.labels.items())

		# NOTE: we are assumign that the labels, dates, and ovals dictionaries all have the same labels
		self.keys_list = list(self.ovals)
		self.selected_idx = self.keys_list.index(self.selected[0])
		self.selected_labels = {}
		self.selected_dates = {}

		# select all the items after the one selected
		for i in range(self.selected_idx, len(self.keys_list)):
			self.selected_labels[i] = self.canvas.find_withtag(self.labels[self.keys_list[i]])
			self.selected_dates[i] = self.canvas.find_withtag(self.dates[self.keys_list[i]])
		# find the index of the selected label  in the list array


		# get selected label and labels afterward


		# get selected text tag
		self.selected_date = self.canvas.find_withtag(self.dates[self.selected[0]])

		# find the index of the selected text tag

		# get selected text tag and text tag afterward


	def move(self, event):
		# Coordinates of the first marker
		circle_coords = self.canvas.coords(self.selected[0])
		x0 = circle_coords[0]   # currently unused, go off of the mouse position
		y0 = circle_coords[1]
		x1 = circle_coords[2]   # currently unused, go off of the mouse position
		y1 = circle_coords[3]
		distance_moved = event.x-self.MARKER_RADIUS-x0

		# Dictionary for new dates
		self.selected_dates_values = {}

		for i in range(self.selected_idx, len(self.keys_list)):

			# Move all markers after the selected marker
			circle_coords = self.canvas.coords(self.keys_list[i])
			self.canvas.coords(self.keys_list[i], \
				circle_coords[0]+distance_moved, \
				circle_coords[1], \
				circle_coords[2]+distance_moved, \
				circle_coords[3])
			
			# Move all the labels
			label_coords = self.canvas.coords(self.selected_labels[i])
			self.canvas.coords(self.selected_labels[i], \
				label_coords[0]+distance_moved, \
				self.marker_ypos-2*self.MARKER_RADIUS)
			self.canvas.tag_raise(self.selected_labels[i])

			# Move all the dates
			date_coords = self.canvas.coords(self.selected_dates[i])			# Original position of the date
			
			self.canvas.coords(self.selected_dates[i], \
				date_coords[0]+distance_moved, \
				self.marker_ypos+2*self.MARKER_RADIUS)
			self.canvas.tag_raise(self.selected_dates[i])
			# Update date
			self.selected_dates_values[i] = self.pos2date(round(date_coords[0]+distance_moved))
				# Rounding above due to an issue with subsecquent moved markers showing an extra date at end of month, eg 3/32
			self.canvas.itemconfig(self.selected_dates[i], text=self.selected_dates_values[i][:-3])
			# [:-3] slices the string to get rid of the year


	def stop_move(self, event):
		# print(self.canvas.itemcget(self.selected_label, 'text'))
		# print(self.canvas.itemcget(self.selected_date, 'text'))

		# # send the yaml build name over, the item array, the item, and the new date
		# self.parent.legend.update_yaml(build_name=self.build_name, \
		# 	label=self.canvas.itemcget(self.selected_label, 'text'), \
		# 	date=self.update_date(event.x))

		# Update all the dates
		for i in range(self.selected_idx, len(self.keys_list)):
			self.parent.legend.update_yaml(build_name=self.build_name, \
				label=self.canvas.itemcget(self.selected_labels[i], 'text'), \
				date=self.selected_dates_values[i])

	# For changing the text of a particular marker
	def change_text(self, posx, posy, text):
		print("placeholder")

	def destroy_timeline(self):
		self.canvas.delete('all')
		self.canvas.destroy()


	# TESTING popup menu
	def popup(self, event):
		self.popup_x = event.x
		self.popup_y = event.y
		try:
			self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
		finally:
			self.popup_menu.grab_release()

	def create_marker(self):
		# print(self.popup_x, self.popup_y)
		item_id = self.canvas.create_circle(self.popup_x, self.marker_ypos, self.MARKER_RADIUS, \
				fill='white', \
					outline='black', width=4, tags='id')

		# Add a label and date to the marker
		label = self.canvas.create_text(self.popup_x, self.marker_ypos-2*self.MARKER_RADIUS, \
				text="XX", fill=self.TEXT_COLOR)

		date_str = self.pos2date(self.popup_x)
		date = self.canvas.create_text(self.popup_x, self.marker_ypos+2*self.MARKER_RADIUS, \
			text=date_str[:-3], fill=self.TEXT_COLOR)

		# Append the marker item to the array of items
		self.array.append((self.popup_x, self.marker_ypos))
		self.ovals[item_id] = self.array[-1]
		self.labels[item_id] = label
		self.dates[item_id] = date

		# Update YAML
		self.parent.yaml_obj.add_label(self.build_name, "XX")


	