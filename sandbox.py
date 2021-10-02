

# https://www.pythontutorial.net/tkinter/tkinter-grid/
# https://pythonguides.com/python-tkinter-frame/ 


import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("800x600")
root.title('Login')


# configure the grid
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=3)


# # username
# username_label = ttk.Label(root, text="Username:")
# username_label.grid(column=1, row=2, sticky=tk.W)

# username_entry = ttk.Entry(root)
# username_entry.grid(column=2, row=2, sticky=tk.E, padx=5, pady=5)

# # password
# password_label = ttk.Label(root, text="Password:")
# password_label.grid(column=1, row=3, sticky=tk.W)

# password_entry = ttk.Entry(root,  show="*")
# password_entry.grid(column=2, row=3, sticky=tk.E, padx=5, pady=5)

# # login button
# login_button = ttk.Button(root, text="Login")
# login_button.grid(column=2, row=5, sticky=tk.E, padx=5, pady=5)

def info():
    print(button1.winfo_width())
    print(root.winfo_geometry())
    # dimension_label = Label(root, text=root.winfo_geometry())

button1=tk.Button(root, text="", width=10, command=info)
button1.grid(row=1,column=1, padx=0)

button2=tk.Button(root, text="Feb", width=10, bg='#000000')
button2.grid(row=1,column=2, padx=0)

button3=tk.Button(root, text="Mar", width=10, bg='blue')
button3.grid(row=1,column=3, padx=0)

button4=tk.Button(root, text="Apr", width=10, bg='blue')
button4.grid(row=1,column=4, padx=0)

button5=tk.Button(root, text="May", width=10, bg='blue')
button5.grid(row=1,column=5, padx=0)

buttonbuild1=tk.Button(root, text="EVT", width=10, height=10)
buttonbuild1.grid(row=2,column=0)

root.mainloop()