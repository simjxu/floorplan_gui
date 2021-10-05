# import tkinter as tk
# from tkinter import ttk

# # root window
# root = tk.Tk()
# root.geometry("500x500")
# root.title('Test')

# month_label = tk.Label(root, width=10, text="", bg="white")
# month_label.pack(side="left", ipady=5)

# month_label0 = tk.Label(root, width=10, text="Jan", bg="red")
# month_label0.pack(side="left", ipady=5)

# month_label1 = tk.Label(root, width=10, text="Feb", bg="blue")
# month_label1.pack(side="left", ipady=5)

# month_label2 = tk.Label(root, width=10, text="Mar", bg="green")
# month_label2.pack(side="left", ipady=5)

# build_label0 = tk.Label(root, width=10, text="System", bg="black")
# build_label0.pack()


# root.mainloop()


# Pack Calendar line


# Pack System Line


# Pack first Build Line


try:
    from Tkinter import Frame, Entry, Tk
except ImportError:
    from tkinter import Frame, Entry, Tk
    

root = Tk()
frame1 = Frame(root, highlightbackground="green", highlightcolor="green", highlightthickness=1, width=100, height=100, bd= 0)
frame1.pack()
frame1.pack_propagate(False)

Entry(frame1).pack()


frame2 = Frame(root, highlightbackground="red", highlightcolor="red", highlightthickness=1, width=100, height=100, bd= 0)
frame2.pack()
frame2.pack_propagate(False)

Entry(frame2).pack()

root.mainloop()