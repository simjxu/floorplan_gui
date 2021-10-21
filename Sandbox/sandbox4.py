import tkinter
from tkinter import *


def myfunction(event):
    canvas1.configure(scrollregion=canvas1.bbox("all"))

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    x = 0
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item %d: "%s"' % (index, value))

    for y in enable:
        for item in list_for_listbox:
            checkbuttons[item][y][1].grid_forget()
        checkbuttons[value][y][1].grid(row=x, column=0)
        # Label(frame2, text="some text").grid(row=x, column=1)
        x += 1

def printcommand():
    for item in list_for_listbox:
        for y in enable:
            print(item + " [" + y + "] " + str(checkbuttons[item][y][0].get()))

def create_new_window():
    global new_window
    new_window = tkinter.Toplevel()
    new_window.geometry("750x500")
    new_window_commands()

master = tkinter.Tk()
master.title("Checkboxes test")
master.geometry("750x500")

button1 = Button(master, command =create_new_window,text="View")
button1.place(x=50,y=250)

def new_window_commands():
    # enable = ['button 1', 'button 2', 'button 3', 'button 4', 'button 5', 'button 6', 'button 7']
    global list_for_listbox
    global enable
    global checkbuttons
    global canvas1
    enable = []
    for x_number_of_items in range(1, 15):
        enable.append("button " + str(x_number_of_items))

    list_for_listbox = ["one", "two", "three", "four"]

    listbox = Listbox(new_window)
    listbox.place(x=5, y=5, width=100, height=10 + 16*len(list_for_listbox))
    listbox.update()

    frame1 = Frame(new_window, borderwidth=1, relief=GROOVE, highlightthickness=1, highlightbackground="black",
                   highlightcolor="black")
    frame1.place(x=listbox.winfo_width() + 10, y=5, width=300, height=listbox.winfo_height())
    canvas1 = Canvas(frame1)
    frame2 = Frame(canvas1, height=500)
    scrollbar1 = Scrollbar(frame1, orient="vertical", command=canvas1.yview)
    canvas1.configure(yscrollcomman=scrollbar1.set)
    scrollbar1.pack(side="right", fill="y")
    canvas1.pack(side="left")
    canvas1.create_window((0, 0), window=frame2, anchor='nw')
    frame2.bind("<Configure>", myfunction)

    printbutton = Button(new_window, text="Print", command=printcommand)
    printbutton.place(x=100, y=250)

    checkbuttons = {}
    for item in list_for_listbox:
        listbox.insert(END, item)
        checkbuttons[item] = (dict())
        for y in enable:
            temp_var = BooleanVar()
            checkbuttons[item][y] = [temp_var, Checkbutton(frame2, text=y, variable=temp_var)]

    listbox.bind('<<ListboxSelect>>', onselect)

    print(enable)

mainloop()

printcommand()