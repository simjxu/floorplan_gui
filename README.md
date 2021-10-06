# Floorplan GUI
Intended to make it easier to create floorplans

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