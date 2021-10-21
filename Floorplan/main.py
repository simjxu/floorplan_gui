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
_MINSIZE = 100

START_ROW = 10
START_COL = 10

# Add the _create_circle function ot the Canvas function, makes it easier to create a circle
def _create_circle(self, x, y, r, **kwargs):
	return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

class MainApplication:
	_NUMBER_OF_DAYS = []
	_NUMBER_OF_MONTHS = 0
	
	DATE_ARRAYS = []
	LABEL_ARRAYS = []

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
		
		# tk.Frame for the Main Application, for reference in child class Timeline
		self.mainframe = tk.Frame(parent, width=1000, height=1000)
		self.mainframe.grid(column=0, row=0, rowspan=100, columnspan=100)		# max out at 20 rows, 20 cols right now

		# Configure size of the grid on root
		for i in range(self._NUMCOLS):
			root.columnconfigure(i, minsize=_MINSIZE)
		for i in range(self._NUMROWS):
				root.columnconfigure(i, minsize=_MINSIZE)


		# print(self.yaml_obj.START_MONTH)
		# print(self.yaml_obj.START_YEAR)
		# print(END_MONTH)
		# print(END_YEAR)
		# Create top row of months, get array of days, set column/rowspan
		self._NUMBER_OF_MONTHS = self.get_num_months()
		try:
			if self._NUMBER_OF_MONTHS >= 24:
				raise ValueTooLargeError
		except ValueTooLargeError:
			print("program doesn't work for span of >= 24 months")
		self._NUMBER_OF_DAYS = self.create_months()

		# print(self._NUMBER_OF_MONTHS)
		# print(self._NUMBER_OF_DAYS)
		
		# Create Timeline opbjects
		self.timeline_arr = []
		for i in range(len(self.yaml_obj.BUILD_NAMES)):
			self.timeline_arr.append(Timeline(self, column=1+START_COL, row=i+1+START_ROW, columnspan=self._NUMCOLS-1, rowspan=1, \
				num_days=self._NUMBER_OF_DAYS, num_months=self._NUMBER_OF_MONTHS, \
				start_month=self.yaml_obj.START_MONTH, \
				start_year=self.yaml_obj.START_YEAR, min_size=_MINSIZE, \
				date_array=self.yaml_obj.DATE_ARRAYS[i], label_array=self.yaml_obj.LABEL_ARRAYS[i], \
				build_name=self.yaml_obj.BUILD_NAMES[i]))

		# Builds going vertical on the left side
		for i in range(len(self.yaml_obj.BUILD_NAMES)):
			self.build = tk.Label(self.mainframe, text=self.yaml_obj.BUILD_NAMES[i])
			self.build.grid(column=0+START_COL, row=i+1+START_ROW, padx=10, pady=0)


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
				text=calendar.month_abbr[month]))
			# MAGIC NUMBER: padx on right needs to be 15 to have the marker match well on label
			label_arr[i].grid(column=i+1+START_COL, row=0+START_ROW, padx=(0,15), pady=0)
			monthdays_arr.append(calendar.monthrange(year,month)[1])
			month += 1

		return monthdays_arr

	def create_builds(self):
		a = 0
		return a


if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("1000x800")
	app = MainApplication(root)
	root.mainloop()