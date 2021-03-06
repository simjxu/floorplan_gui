# Floorplan GUI
Intended to make it easier to create floorplans

![alt text](https://github.com/simjxu/floorplan_gui/blob/main/x-screenshot.png?raw=true)


## Features
- CSV input: Use CSV file with inputs to indicate the different milestones that need to be mapped
- Image should resize with the window
- Adjustable/slidable milestone dates: Can adjust the dates by mouse
    - Dates should automatically adjust
- Today line: Vertical line available that marks today line
- Arrows and lines should be movable to point
- Depending on how many builds the user wants to include, the rows should adjust
- User can name the different builds based upon CSV file

## Updates
11/1/21:
- Have scroll center at today's date
- Right click functionality to add new markers, change color

10/26/21:
- Make mouse wheel scroll work for scroll bar [DONE]
- Add in dividers on the months [DONE]
- Add years on top of the months [DONE]
- Bug: 11/30 shows up as 11/29 when at a wider min_xlen (try 300) [DONE]
- Bug: fix scroll bar not working properly, need to only increase canvas size of timeline, but keep window size the same [DONE]

10/22/21: Fixed a lot of items. Remaining to do:
- Bug: 11/30 date marker in yaml shows up as 12/0 on table
10/17/21: Next step to add the marker labels in, maybe figure out how to move the Timeline object to another class
10/13/21: Next step to create a YAML input
10/11/21: Struggled to create a Marker class to control the different circle objects.
10/8/21: Issue with expanding the number of months. Need to figure out how to use frame properly to add additional columns.
10/6/21: Need to fix update_date to account for month rollover. Variable _NUMBER_OF_DAYS is not being shared with the class Timeline
10/4/21: Update the Circle to use the built in circles. If here's time, add in calendar conversion
Create input for the calendar range
Next time: use the calendar library to input dates. Also, parse a text file (yaml?) for dates and be able to save them

10/3/21: Updated main.py to at least be working. I'm not sure why I have to use parent (tk.Tk()) for the Label, but it won't work if I try to createa  label within the Frame.
Next steps is to add the calendar library into the application, and translate a coordinate (100)--> a date
Also, the class Timeline needs to take in arguments in order for me to define what grid placement the timeline should be on.
Also, working with an image for a circle is too hard. We are going to switch to the build in circles
https://stackoverflow.com/questions/17985216/simpler-way-to-draw-a-circle-with-tkinter 

9/26/21: Moving towards having more classes in tkinter. Check out this link for two windows: https://stackoverflow.com/questions/16115378/tkinter-example-code-for-multiple-windows-why-wont-buttons-load-correctly
- https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
9/23/21: Looks like I have to copy quite a few lines just to get it working. I should consider creating a class or function so that I don't have to copy all those lines to maintain the size
Next item to do is see if we can lock the bluecircle to a line