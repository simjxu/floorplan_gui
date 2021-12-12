import tkinter as tk

def popup(event):
    print("clicked")
    try:
      popup_menu.tk_popup(event.x_root, event.y_root, 0)
    finally:
      popup_menu.grab_release()

def delete_selected():
  print("delete")

def select_all():
  print("select")

root = tk.Tk()
root.geometry("800x600")
frame = tk.Frame(root,height=600,width=800, bg='red')
frame.pack()


canvas = tk.Canvas(frame,height=500,width=500, highlightbackground='green')
canvas.pack()

popup_menu = tk.Menu(tearoff=0)
popup_menu.add_command(label="Delete",
                                command=delete_selected)
popup_menu.add_command(label="Select All",
                            command=select_all)

canvas.bind("<Button-2>", popup)

root.mainloop()