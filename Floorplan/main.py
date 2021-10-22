import tkinter as tk
import os
import math
import calendar
import datetime
from YAMLoutput import YAMLoutput
from timeline import Timeline
from exception import *
from legend import Legend

ymlFile = './YAMLs/x_sys.yaml'
# ymlFile = './Sample_YAML/savefile.yaml'
# ymlFile = './Sample_YAML/example.yaml'

# Input width of each cell
MIN_XLEN = 150
MIN_YLEN = 75

# # Input width of each cell
# MIN_XLEN = 10
# MIN_YLEN = 10

START_ROW = 0
START_COL = 0

# Add the _create_circle function ot the Canvas function, makes it easier to create a circle
def _create_circle(self, x, y, r, **kwargs):
	return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

class MainApplication:
	_NUMBER_OF_DAYS = []
	_NUMBER_OF_MONTHS = 0
	
	DATE_ARRAYS = []
	LABEL_ARRAYS = []

	TEXT_COLOR = 'black'

	def __init__(self, parent):
		

		# import the yaml file data
		self.yaml_obj = YAMLoutput(self, file=ymlFile)
		self.DATE_ARRAYS = self.yaml_obj.DATE_ARRAYS
		self.LABEL_ARRAYS = self.yaml_obj.LABEL_ARRAYS

		# Create legend window
		self.legend = Legend(self)

		# Update the number of columns
		self._NUMCOLS = 2		# Start at 1 to include the builds column, first month
		month_ptr = self.yaml_obj.START_MONTH
		year_ptr = self.yaml_obj.START_YEAR
		while month_ptr != self.yaml_obj.END_MONTH or year_ptr != self.yaml_obj.END_YEAR:
			self._NUMCOLS += 1
			if month_ptr == 12:
				month_ptr = 1
				year_ptr += 1
			else:
				month_ptr += 1

		# Update the number of rows
		self._NUMROWS = len(self.yaml_obj.BUILD_NAMES) + 1
		
		# Need Frame for Builds
		self.buildframe = tk.Frame(parent, bg="white")
		self.buildframe.grid(row=0, column=0)

		# Need Canvas for the scrollbar
		self.maincanvas = tk.Canvas(parent, bg="white", highlightthickness=0)
		self.maincanvas.grid(row=0, column=1)

		# Create a horizontal scrollbar linked to the canvas.
		self.hsbar = tk.Scrollbar(parent, orient=tk.HORIZONTAL, command=self.maincanvas.xview)
		self.hsbar.grid(row=1, column=1, sticky=tk.EW)
		self.maincanvas.configure(xscrollcommand=self.hsbar.set)

		# tk.Frame for the Main Application, for reference in child class Timeline
		# self.mainframe = tk.Frame(parent, width=1000, height=1000, bg='white')
		# self.mainframe.grid(column=0, row=0, rowspan=100, columnspan=100)		# max out at 20 rows, 20 cols right now
		self.mainframe = tk.Frame(self.maincanvas, bg="white", bd=2)

		ROWS_DISP = 10  # Number of rows to display.
		COLS_DISP = 7  # Number of columns to display.

		# Configure size of the grid
		for i in range(self._NUMROWS):
			self.mainframe.rowconfigure(i, minsize=MIN_YLEN)
			self.buildframe.rowconfigure(i, minsize=MIN_YLEN)
		for i in range(self._NUMCOLS):
			self.mainframe.columnconfigure(i, minsize=MIN_XLEN)
		
		# Create top row of months, get array of days, set column/rowspan
		self._NUMBER_OF_MONTHS = self.get_num_months()
		try:
			if self._NUMBER_OF_MONTHS >= 24:
				raise ValueTooLargeError
		except ValueTooLargeError:
			print("program doesn't work for span of >= 24 months")
		self._NUMBER_OF_DAYS = self.create_months()
		
		# Create Timeline objects
		self.timeline_arr = []
		self.builds_arr = []
		self.checkbox_arr = []
		for i in range(len(self.yaml_obj.BUILD_NAMES)):
			self.checkbox_arr.append(1)
		self.load_builds() # Builds on the left side
		self.load_timelines()
		
		# Create canvas window to hold the buttons_frame.
		self.maincanvas.create_window((0,0), window=self.mainframe, anchor=tk.NW)

		self.mainframe.update_idletasks()  # Needed to make bbox info available.
		bbox = self.maincanvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.

		# Define the scrollable region as entire canvas with only the desired
		# number of rows and columns displayed.
		w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
		dw, dh = int((w/self._NUMCOLS) * COLS_DISP), int((h/self._NUMROWS) * ROWS_DISP)
		self.maincanvas.configure(scrollregion=bbox, width=dw, height=dh)

	def load_builds(self):
		# Clear builds
		for build in self.builds_arr:
			if isinstance(build, tk.Label):
				build.destroy()
		self.builds_arr.clear()

		rowptr = 0
		for i in range(len(self.yaml_obj.BUILD_NAMES)):
			if self.checkbox_arr[i] == 0:
				self.builds_arr.append(type('empty', (object,), {})())		# append empty object
			# For transparency, use the parent background color
			# self.build = tk.Label(self.mainframe, text=self.yaml_obj.BUILD_NAMES[i], fg="black", bg="white")
			else:
				self.builds_arr.append(tk.Label(self.buildframe, text=self.yaml_obj.BUILD_NAMES[i], \
					fg=self.TEXT_COLOR, bg='white', wraplength=50))
				self.builds_arr[i].grid(column=0, row=rowptr, padx=10, pady=0)
				rowptr += 1
		

	def load_timelines(self):
		# print(self.checkbox_arr)
		for timeline in self.timeline_arr:
			# Check to see if it is a timeline object or an empty object
			if isinstance(timeline, Timeline):
				timeline.destroy_timeline()
		self.timeline_arr.clear()			# if the array is not empty, clear it
		rowptr = 0
		for i in range(len(self.yaml_obj.BUILD_NAMES)):
			if self.checkbox_arr[i] == 0:
				# pass
				self.timeline_arr.append(type('empty', (object,), {})())		# append empty object
			else:
				self.timeline_arr.append(Timeline(self, column=0, row=rowptr+1, columnspan=self._NUMCOLS-1, rowspan=1, \
					num_days=self._NUMBER_OF_DAYS, num_months=self._NUMBER_OF_MONTHS, \
					start_month=self.yaml_obj.START_MONTH, \
					start_year=self.yaml_obj.START_YEAR, min_xlen=MIN_XLEN, min_ylen=MIN_YLEN, \
					date_array=self.yaml_obj.DATE_ARRAYS[i], label_array=self.yaml_obj.LABEL_ARRAYS[i], \
					build_name=self.yaml_obj.BUILD_NAMES[i]))
				rowptr += 1

	def get_num_months(self):
		# print(self.yaml_obj.START_MONTH)
		# print(self.yaml_obj.START_YEAR)
		start_date = datetime.datetime(self.yaml_obj.START_YEAR,self.yaml_obj.START_MONTH,1)
		end_date = datetime.datetime(self.yaml_obj.END_YEAR, self.yaml_obj.END_MONTH, 1)
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
		year = self.yaml_obj.START_YEAR
		month = self.yaml_obj.START_MONTH
		for i in range(num_months):
			# Account for months rollover at end of year
			if month==13:
				month = 1
				year += 1

			label_arr.append(tk.Label(self.mainframe, \
				text=calendar.month_abbr[month], fg=self.TEXT_COLOR, bg='white'))
			# MAGIC NUMBER: padx on right needs to be 15 to have the marker match well on label
			label_arr[i].grid(column=i+START_COL, row=0+START_ROW, padx=(0,15), pady=0)
			monthdays_arr.append(calendar.monthrange(year,month)[1])
			month += 1

		return monthdays_arr

	def create_builds(self):
		a = 0
		return a


if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("1300x800")
	root.configure(bg='white')
	app = MainApplication(root)
	root.mainloop()