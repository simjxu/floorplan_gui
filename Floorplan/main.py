import tkinter as tk
from tkinter import ttk
import os
import math
import calendar
import datetime
from YAMLoutput import YAMLoutput
from timeline import Timeline
from exception import *
from legend import Legend

ymlFile = '/Users/simonxu/Documents/Github-simjxu/floorplan_gui/YAMLs/x_sys.yaml'
# ymlFile = './Sample_YAML/savefile.yaml'
# ymlFile = './Sample_YAML/example.yaml'

# Input width of each cell
MIN_XLEN = 150
MIN_YLEN = 50

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

	MAX_ROWS = 14			# FIX: need to base this on the MIN_YLEN

	def __init__(self, parent):
		
		ROWS_DISP = self.MAX_ROWS  # Number of rows to display.
		COLS_DISP = 7  # Number of columns to display. FIX: need to base this on the MIN_XLEN

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
		self._NUMROWS = len(self.yaml_obj.BUILD_NAMES)
		
		# Need Frame for Builds
		self.buildframe = tk.Frame(parent, bg="white", height=10)
		self.buildframe.grid(row=0, column=0)

		# Need Container Frame, Canvas, and scrollable Frame 
		self.containerframe = tk.Frame(parent).grid(row=0, column=1)
		self.maincanvas = tk.Canvas(self.containerframe, bg="white", \
			height=14*50, width=7*150, highlightthickness=0)
		self.maincanvas.grid(row=0, column=1, sticky=tk.N)
		self.mainframe = tk.Frame(self.maincanvas, bg='white') # scrollable

		# Create a horizontal scrollbar linked to the container frame.
		self.hsbar = tk.Scrollbar(self.containerframe, orient=tk.HORIZONTAL, command=self.maincanvas.xview)
		self.hsbar.grid(row=1, column=1, sticky=tk.EW)
		self.maincanvas.configure(xscrollcommand=self.hsbar.set)

		self.mainframe.bind(
			"<Configure>",
			lambda e: self.maincanvas.configure(
					scrollregion=self.maincanvas.bbox("all")
				)
		)

		# Create canvas window.
		self.maincanvas.create_window((0,0), window=self.mainframe, anchor=tk.NW)

		# Configure size of the grid
		for i in range(self.MAX_ROWS):
			self.mainframe.rowconfigure(i, minsize=MIN_YLEN)
			self.buildframe.rowconfigure(i, minsize=MIN_YLEN+2)		# Added 2 because otherwise rows don't line up. Not sure why, need to fix
		for i in range(self._NUMCOLS):
			self.mainframe.columnconfigure(i, minsize=MIN_XLEN)
			# self.buildframe.columnconfigure(i, minsize=MIN_XLEN)
		
		# Create top row of months, get array of days, set column/rowspan
		self._NUMBER_OF_MONTHS = self.get_num_months()
		try:
			if self._NUMBER_OF_MONTHS >= 24:
				raise ValueTooLargeError
		except ValueTooLargeError:
			print("program doesn't work for span of >= 24 months")
		self._NUMBER_OF_DAYS = []
		self.create_months()
		
		# # Create Timeline objects
		self.timeline_arr = []
		self.builds_arr = []
		self.checkbox_arr = []
		for i in range(len(self.yaml_obj.BUILD_NAMES)):
			self.checkbox_arr.append(1)
		self.load_builds() # Builds on the left side
		self.load_timelines()

		# parent.line_style = ttk.Style()
		# parent.line_style.configure("Line.TSeparator", background="#000000")
		# ttk.Separator(parent, orient=tk.VERTICAL, style="Line.TSeparator").grid(column=2, row=0, rowspan=5, sticky='ns')

	def load_builds(self):
		# Clear builds
		for build in self.builds_arr:
			if isinstance(build, tk.Label):
				build.destroy()
		self.builds_arr.clear()

		rowptr = 0
		for i in range(self._NUMROWS):
		# for i in range(len(self.yaml_obj.BUILD_NAMES)):
			if rowptr >= self.MAX_ROWS-1:			# Off by 1: Builds start one row down so we want to delete extra
				break
			if self.checkbox_arr[i] == 0:
				self.builds_arr.append(type('empty', (object,), {})())		# append empty object
			# For transparency, use the parent background color
			# self.build = tk.Label(self.mainframe, text=self.yaml_obj.BUILD_NAMES[i], fg="black", bg="white")
			else:
				self.builds_arr.append(tk.Label(self.buildframe, text=self.yaml_obj.BUILD_NAMES[i], \
					fg=self.TEXT_COLOR, bg='white', wraplength=100))
				self.builds_arr[i].grid(column=0, row=rowptr+1, sticky=tk.N)
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
			if rowptr >= self.MAX_ROWS-1:
				break
			if self.checkbox_arr[i] == 0:
				# pass
				self.timeline_arr.append(type('empty', (object,), {})())		# append empty object
			else:
				self.timeline_arr.append(Timeline(self, column=0, row=rowptr+1, columnspan=self._NUMCOLS-1, rowspan=1, \
					num_days=self._NUMBER_OF_DAYS, num_months=self._NUMBER_OF_MONTHS, \
					start_month=self.yaml_obj.START_MONTH, \
					start_year=self.yaml_obj.START_YEAR, min_xlen=MIN_XLEN, min_ylen=MIN_YLEN, \
					date_array=self.yaml_obj.DATE_ARRAYS[i], label_array=self.yaml_obj.LABEL_ARRAYS[i], \
					color_array=self.yaml_obj.COLOR_ARRAYS[i], build_name=self.yaml_obj.BUILD_NAMES[i]))
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

			# label_arr.append(tk.Label(self.mainframe, \
			# 	text=calendar.month_abbr[month], fg=self.TEXT_COLOR, bg='white'))
			# # MAGIC NUMBER: padx on right needs to be 15 to have the marker match well on label
			# label_arr[i].grid(column=i+START_COL, row=0+START_ROW)
			self.round_rectangle_text(self.mainframe, 5, 5, MIN_XLEN, 40, radius=25, \
				row=START_ROW, col=i+START_COL, _text=str(year)+'\n '+calendar.month_abbr[month], fill="gray")

			monthdays_arr.append(calendar.monthrange(year,month)[1])
			month += 1
		self._NUMBER_OF_DAYS=monthdays_arr

	def round_rectangle_text(self, _frame, x1, y1, x2, y2, radius=25, row=0, col=0, \
		 _text='default', **kwargs):
		canvas = tk.Canvas(_frame, height=y2, width=x2, bg="white", highlightthickness=0)
		canvas.grid(row=row, column=col, padx=0)
		points = [x1+radius, y1,
							x1+radius, y1,
							x2-radius, y1,
							x2-radius, y1,
							x2, y1,
							x2, y1+radius,
							x2, y1+radius,
							x2, y2-radius,
							x2, y2-radius,
							x2, y2,
							x2-radius, y2,
							x2-radius, y2,
							x1+radius, y2,
							x1+radius, y2,
							x1, y2,
							x1, y2-radius,
							x1, y2-radius,
							x1, y1+radius,
							x1, y1+radius,
							x1, y1]
		new_poly = canvas.create_polygon(points, **kwargs, smooth=True)
		new_text = canvas.create_text((x1+x2)/2,(y1+y2)/2, text=_text)      # center the text


if __name__ == "__main__":
	root = tk.Tk()
	root.title("X1981 Floorplan")
	root.geometry("1200x800")
	root.configure(bg='white')
	app = MainApplication(root)
	root.mainloop()