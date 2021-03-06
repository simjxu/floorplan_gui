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
ROWS_DISP = 4  # Number of rows to display.
COLS_DISP = 5  # Number of columns to display.

class MyApp(tk.Tk):
    GLOBAL_SIZE = 750

    def __init__(self, title="Sample App", *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.geometry(str(self.GLOBAL_SIZE)+"x550")
        print(self.GLOBAL_SIZE)

        # Add a canvas in that frame.
        canvas = tk.Canvas(self, bg="Yellow")
        canvas.grid(row=0, column=0)

        my_canvas2 = tk.Canvas(self, bg='blue', height=100, width=50)
        my_canvas2.grid(row=0, column=1)
        my_frame2 = tk.Frame(my_canvas2)
        my_frame2.grid(row=0, column=0, sticky=tk.N)
        text_label = []
        for i in range(ROWS):
            text_label.append(tk.Label(my_frame2, text="TESTER"))
            text_label[i].grid(column=0, row=i, columnspan=1, rowspan=1)
        # Create a vertical scrollbar linked to the canvas.
        vsbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=canvas.yview)
        vsbar.grid(row=0, column=1, sticky=tk.NS)
        canvas.configure(yscrollcommand=vsbar.set)
        canvas.yview_moveto(0)

        # Create a horizontal scrollbar linked to the canvas.
        hsbar = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=canvas.xview)
        hsbar.grid(row=1, column=0, sticky=tk.EW)
        canvas.configure(xscrollcommand=hsbar.set)

        # Create a frame on the canvas to contain the buttons.
        buttons_frame = tk.Frame(canvas, bg="Red", bd=2)

        # # Add the buttons to the frame.
        # for i in range(1, ROWS+1):
        #     for j in range(1, COLS+1):
        #         button = tk.Label(buttons_frame, padx=7, pady=7, relief=tk.RIDGE,
        #                            text="TESTER")
        #         button.grid(row=i, column=j, sticky='news')
        
        # Add the buttons to the frame.
        for i in range(1, ROWS+1):
            button = tk.Canvas(buttons_frame, height=25, width=25*COLS, bg='red')
            button.grid(row=i, columnspan=COLS, sticky='news')

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

        self.popupwin()

    def popupwin(self):
        #Create a Toplevel window
        top= tk.Toplevel()
        top.geometry("750x250")

        #Create an Entry Widget in the Toplevel window
        entry= tk.Entry(top, width= 25)
        entry.pack()

        #Create a Button to print something in the Entry widget
        tk.Button(top,text= "Insert", command= lambda:tk.insert_val(entry)).pack(pady= 5,side=tk.TOP)
        #Create a Button Widget in the Toplevel Window
        button1= tk.Button(top, text="Bigger", command=lambda:self.bigger())
        button1.pack(pady=5, side= tk.TOP)

        button2= tk.Button(top, text="Smaller", command=lambda:self.smaller())
        button2.pack(pady=5, side= tk.TOP)

    def nothing(self):
        print("test")

    def bigger(self):
        print("bigger ran")
        self.GLOBAL_SIZE = 800
        self.refresh()
    
    def smaller(self):
        self.GLOBAL_SIZE = 400
        self.refresh()

    def refresh(self):
        self.destroy()
        self.__init__(title="Sample App")

if __name__ == "__main__":
    app = MyApp("Scrollable Canvas")
    app.mainloop()