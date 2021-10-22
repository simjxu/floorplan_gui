import tkinter as tk

class MainApplication:
  def __init__(self, parent):
    my_canvas1 = tk.Canvas(parent, bg='green', height=200, width=100)
    my_canvas1.grid(row=0, column=0)

    my_frame1 = tk.Frame(my_canvas1)
    my_frame1.grid(row=0,column=0)

    my_canvas2 = tk.Canvas(parent, bg='blue', height=200, width=100)
    my_canvas2.grid(row=0, column=1)

    my_frame2 = tk.Frame(my_canvas2)
    my_frame2.grid(row=0, column=0)

    for i in range(5):
      my_frame1.rowconfigure(i, minsize=100)
      my_frame2.rowconfigure(i, minsize=100)
    
    a = tk.Label(my_frame1, text="TEST")
    a.grid(row=1, column=0)
    b = tk.Label(my_frame2, text="TEST2")
    b.grid(row=0,column=0)

if __name__ == "__main__":
  root = tk.Tk()
  root.geometry("1200x800")
  app = MainApplication(root)
  root.mainloop()