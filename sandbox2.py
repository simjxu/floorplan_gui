import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("800x600")
root.title('Login')

# configure the grid
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=3)


# # Months going horizontal on top
# month1 = ttk.Label(root, text="Jan")
# month1.grid(column=1, row=0, padx=40, pady=5)

# month2 = ttk.Label(root, text="Feb")
# month2.grid(column=2, row=0, padx=40, pady=5)

# month3 = ttk.Label(root, text="Mar")
# month3.grid(column=3, row=0, padx=40, pady=5)

# # Builds going vertical on the left side
# build1 = ttk.Label(root, text="System")
# build1.grid(column=0, row=1, padx=10, pady=80)

# build1 = ttk.Label(root, text="EVT")
# build1.grid(column=0, row=2, padx=10, pady=80)

# Insert Frame Starting at the bottom right corner of the 0,0 cell,
# Ending at the 

# timeline1 = tk.Frame(root, width=100, height=50, bg=="red", width=100)
timeline1 = tk.Frame(root,width=100,height=50,  
       highlightcolor="yellow",highlightbackground="red",  
       highlightthickness=10)
# timeline1.grid(column=1, row=1, columnspan=3, rowspan=1)

# topleft_ptr = 
# botright_ptr = 

# username_entry = ttk.Entry(root)
# username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# # password
# password_label = ttk.Label(root, text="Password:")
# password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

# password_entry = ttk.Entry(root,  show="*")
# password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# # login button
# login_button = ttk.Button(root, text="Login")
# login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


root.mainloop()