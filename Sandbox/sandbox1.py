

START_MONTH = 12
START_YEAR = 2019
END_MONTH = 3
END_YEAR = 2020

_NUMCOLS = 1		# Start at 1 to include the builds column
month_ptr = START_MONTH
year_ptr = START_YEAR

while month_ptr != END_MONTH or year_ptr != END_YEAR:
	_NUMCOLS += 1
	if month_ptr == 12:
		month_ptr = 1
		year_ptr += 1
	else:
		month_ptr += 1
	print(month_ptr)
	print(year_ptr)


print(_NUMCOLS)