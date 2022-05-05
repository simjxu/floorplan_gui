import tkinter as tk
from tkinter import ttk

class MainApplication:

   def __init__(self, parent):
      # # Frame containing everything
      # self.containerframe = tk.Frame(parent).grid(row=0, column=0)
      
      self.emptylabel = tk.Label(parent, borderwidth=1)

      # Canvas for the title
      self.titlecanvas = tk.Canvas(parent, \
         height=50, width=600, bg="white")
      self.titlecanvas.grid(row=0, column=0, columnspan=12)
      self.titlelabel = self.titlecanvas.create_text(300, 25, \
         text="D37 (X2834) | Battery Floorplan - P1 Detail", \
         font=("Helvetica Neue", "25"), fill="black")

      # Canvas for the blank spot
      self.canvas00 = tk.Canvas(parent, \
			height=50, width=100, bg="white", highlightthickness=1)
      self.canvas00.grid(row=1, column=0, rowspan=2, columnspan=2)

      #Canvas for the System build
      self.systemcanvas = tk.Canvas(parent, \
			height=50, width=100, bg="white", highlightthickness=1)
      self.systemcanvas.grid(row=4, column=0, columnspan=2)
      self.systemlabel = self.systemcanvas.create_text(0,0,text="System", fill="black")
      
      # COLUMN 1::::::::::::::::::::::::::::::::::::::::::::::::::::::::
      # Canvas for pack
      self.packcanvas = tk.Canvas(parent, \
			width=50, height=50, bg="white", highlightthickness=1)
      self.packcanvas.grid(row=5, column=0)
      self.packlabel = self.packcanvas.create_text(25,25,text="Pack", \
         font=("Helvetica", "18"), fill="black")

      # Canvas for Cell
      self.cellcanvas = tk.Canvas(parent, \
			height=50, width=50, bg="white", highlightthickness=1).grid( \
         row=6, column=0, rowspan=2)

      # Canvas for BMU
      self.bmucanvas = tk.Canvas(parent, \
			height=50, width=50, bg="white", highlightthickness=1).grid( \
         row=8, column=0, rowspan=3)

      # COLUMN 2::::::::::::::::::::::::::::::::::::::::::::::::::::::::
      # Canvas for Pack Vendor
      self.packvcanvas = tk.Canvas(parent, \
			width=50, height=50, bg="white", highlightthickness=1)
      self.packvcanvas.grid(row=5, column=1) 
      self.packvlabel = self.packvcanvas.create_text(25,25,text="SWD/SMP", \
         font=("Helvetica", "18"), fill="black")

      # Canvas for Cell Vendors
      self.cellatlcanvas = tk.Canvas(parent, \
			height=25, width=50, bg="white", highlightthickness=1).grid( \
         row=6, column=1)
      self.celllgcanvas = tk.Canvas(parent, \
			height=25, width=50, bg="white", highlightthickness=1).grid( \
         row=6, column=1)

def motion(event):
      x, y = event.x, event.y
      print('{}, {}'.format(x, y))

if __name__ == "__main__":
   
   root = tk.Tk()
   root.title("X2384 Floorplan")
   root.geometry("1280x720")
   # root.geometry("2560x1440")
   root.configure(bg='white')
   root.bind("<Motion>", motion)

   app = MainApplication(root)
   root.mainloop()