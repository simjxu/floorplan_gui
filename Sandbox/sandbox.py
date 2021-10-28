import math

START_YEAR=2021
START_MONTH=7
MIN_XLEN=100

num_days=[31, 31, 30, 31, 30, 31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

def pos2date(pos):
  # Takes position value (not integer right now) as an input and outputs a string 
  # without the year, e.g. 9/11
  month_idx = math.floor(pos/MIN_XLEN)
  print("month_idx ", month_idx)
  year = START_YEAR
  month = START_MONTH + month_idx
  if month/12 > 1:			# CAREFUL... Hopefully type(month)==int
    year += math.floor(month/12)
    month = month-12*math.floor(month/12)
  day = num_days[month_idx] * ((pos-month_idx*MIN_XLEN)/MIN_XLEN)
  print("day unrounded ", day)
  day = math.ceil(day)
  print("day rounded ", day)

  # # For Debug
  # return str(math.floor(pos))

  # # Show full year string
  return str(month) + "/" + str(day) + "/" + str(year)[2:]
  # return str(month) + "/" + str(day) 


def date2pos(datestr):
  # Convert the date string into a pixel position
  # 1. Pull out the month, day, and year into integers
  # 2. Find Month index based upon start month and year
  # 3. Multiply month index by MINSIZE, then add days/number_days_in_month * MINSIZE
  m_d_y = datestr.split('/')
  m = int(m_d_y[0])
  d = int(m_d_y[1])
  y = int(m_d_y[2])+2000 # Need to add 2000 (won't work for after year 2099, but who cares)

  if m < START_MONTH:
    month_idx = m+12 - START_MONTH + (y-1-START_YEAR)*12
  else:
    month_idx = m - START_MONTH + (y-START_YEAR)*12

  # d-0.5 to avoid edge cases at the edge of month (12/0 when it should be 11/30)
  return MIN_XLEN*month_idx + (d-0.5)/num_days[month_idx]*MIN_XLEN


print(pos2date(98.38709677))

print(date2pos('7/31/21'))