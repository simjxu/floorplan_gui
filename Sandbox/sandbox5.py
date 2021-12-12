checkbox_selected_file = \
      '/Users/simonxu/Documents/Github-simjxu/floorplan_gui/checkbox_selected.txt'

with open(checkbox_selected_file, 'w') as f:
    for i in range(5):
    
        if i==0:
          f.write(str(1))
        else:
          f.write(',')
          f.write(str(0))