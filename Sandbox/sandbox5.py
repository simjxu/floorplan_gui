import tkinter as tk
from tkinter import PhotoImage, ttk

class MainApplication:

   def __init__(self, parent):

      # Canvas for the title
      self.slidecanvas = tk.Canvas(parent, height=720, width=1280, bg="white")
      self.slidecanvas.pack()
      
      img = PhotoImage(file="/Users/simonxu/Documents/Github-simjxu/floorplan_gui/fp_images/test.png")

      # self.slidecanvas.create_image(260,125, anchor="nw", image=img)
      self.loc_label = self.slidecanvas.create_text(500,500,text="",fill="black")

      self.slidecanvas.bind("<B1-Motion>", self.move)

   def move(self, event):
      self.slidecanvas.itemconfig(self.loc_label, \
         text="Coordinates"+str(event.x)+","+(event.y))


def motion(event):
      x, y = event.x, event.y
      print('{}, {}'.format(x, y))

if __name__ == "__main__":
   
   root = tk.Tk()
   root.title("X2384 Floorplan")
   root.geometry("1280x720")
   # root.geometry("2560x1440")
   root.configure(bg='white')

   app = MainApplication(root)
   root.mainloop()