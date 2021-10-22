# import tkinter as tk

# LABEL_BG = "#ccc"  # Light gray.
# ROWS, COLS = 10, 6  # Size of grid.
# ROWS_DISP = 3  # Number of rows to display.
# COLS_DISP = 4  # Number of columns to display.

# class MyApp(tk.Tk):
#     def __init__(self, title="Sample App", *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)

#         # Add a canvas in that frame.
#         canvas = tk.Canvas(self, bg="Yellow")
#         canvas.grid(row=0, column=0)

#         # Create a horizontal scrollbar linked to the canvas.
#         hsbar = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=canvas.xview)
#         hsbar.grid(row=1, column=0, sticky=tk.EW)
#         canvas.configure(xscrollcommand=hsbar.set)

#         # Create a frame on the canvas to contain the buttons.
#         buttons_frame = tk.Frame(canvas, bg="Red", bd=2)

#         # Add 9-by-5 buttons to the frame
#         rows = 9
#         columns = 15
#         buttons = [[tk.Button() for j in range(columns)] for i in range(rows)]
#         for i in range(0, rows):
#             for j in range(0, columns):
#                 buttons[i][j] = tk.Button(buttons_frame, text="TESTERTESTER")
#                 buttons[i][j].grid(row=i, column=j, sticky='news')

#         # Create canvas window to hold the buttons_frame.
#         canvas.create_window((0,0), window=buttons_frame, anchor=tk.NW)

#         buttons_frame.update_idletasks()  # Needed to make bbox info available.
#         bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
#         #print('canvas.bbox(tk.ALL): {}'.format(bbox))

#         # Define the scrollable region as entire canvas with only the desired
#         # number of rows and columns displayed.
#         w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
#         dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
#         canvas.configure(scrollregion=bbox, width=dw, height=dh)



# if __name__ == "__main__":
#     app = MyApp("Scrollable Canvas")
#     app.mainloop()



import tkinter as tk

ROWS, COLS = 10, 10  # Size of grid.
ROWS_DISP = 10  # Number of rows to display.
COLS_DISP = 5  # Number of columns to display.

class MyApp(tk.Tk):
    def __init__(self, title="Sample App", *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Add a canvas in that frame.
        canvas = tk.Canvas(self, bg="Yellow")
        canvas.grid(row=0, column=0)

        # # Create a vertical scrollbar linked to the canvas.
        # vsbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=canvas.yview)
        # vsbar.grid(row=0, column=1, sticky=tk.NS)
        # canvas.configure(yscrollcommand=vsbar.set)

        # Create a horizontal scrollbar linked to the canvas.
        hsbar = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=canvas.xview)
        hsbar.grid(row=1, column=0, sticky=tk.EW)
        canvas.configure(xscrollcommand=hsbar.set)

        # Create a frame on the canvas to contain the buttons.
        buttons_frame = tk.Frame(canvas, bg="Red", bd=2)

        # Add the buttons to the frame.
        for i in range(1, ROWS+1):
            for j in range(1, COLS+1):
                button = tk.Label(buttons_frame, padx=7, pady=7, relief=tk.RIDGE,
                                   text="TESTER")
                button.grid(row=i, column=j, sticky='news')

        # Create canvas window to hold the buttons_frame.
        canvas.create_window((0,0), window=buttons_frame, anchor=tk.NW)

        buttons_frame.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
        #print('canvas.bbox(tk.ALL): {}'.format(bbox))

        # Define the scrollable region as entire canvas with only the desired
        # number of rows and columns displayed.
        w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
        dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
        canvas.configure(scrollregion=bbox, width=dw, height=dh)


if __name__ == "__main__":
    app = MyApp("Scrollable Canvas")
    app.mainloop()