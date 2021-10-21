import tkinter as tk
from tkinter import ttk

class Legend:
  def __init__(self, parent, **kwargs):
    self.savefile = './YAMLs/x_sys.yaml'
    self.testtext = "ABC"   # For testing, delete
    self.parent = parent

    # New window for the Legend
    self.window = tk.Toplevel()     # Top level needed, don't totally understand why not tk.Tk()
    self.window.geometry("200x600+800+0")
    self.window.title("Legend")

    # Buttons must be under a frame
    button_frame = tk.Frame(self.window)
    button_frame.pack()

    # Create save button
    save_button = tk.Button(button_frame, text="SAVE", fg="black", command=self.save)
    save_button.pack()

    # Create reload button
    reload_button = tk.Button(button_frame, text="RELOAD", fg="black", command=self.reload)
    reload_button.pack()

    # Create Checkboxes
    self.checkarray = []
    self.checkboxes = []
    
    for i in range(5):
      self.checkarray.append(tk.IntVar())
      self.checkboxes.append(ttk.Checkbutton(self.window, text="TEST", variable=self.checkarray[i], \
        onvalue=1, offvalue=0))
      self.checkboxes[i].pack()

  # Pass in all YAML data into Legend object
  # Can be called when move is made
  def update_yaml(self, **kwargs):
    build_name = kwargs['build_name']
    label = kwargs['label']
    date = kwargs['date']
    self.parent.yaml_obj.update_dates(build_name=build_name, label=label, \
      date=date)
  
  def save(self):
    self.parent.yaml_obj.save_current(self.savefile)

  def update_canvas(self):
    print("update")

  def reload(self):
    for var in self.checkarray:
      print(var.get())

class MainApplication:
  def __init__(self, parent, **kwargs):
    self.legend = Legend(self)

    # # New window for the Legend
    # self.window = tk.Toplevel()
    # self.window.geometry("200x600+800+0")
    # self.window.title("Legend")
    # def boxstates():
    #   for var in vars:
    #       print (var.get())

    # names = ["Mike", "Harry", "Siti"]

    # labelName = tk.Label(self.window, text = "Name")
    # labelName.pack(anchor = tk.W)

    # vars = []

    # for i, checkboxname in enumerate(names):
    #   vars.append(tk.IntVar())
    #   check = ttk.Checkbutton(self.window, text=checkboxname, variable=vars[i])
    #   check.pack(anchor = tk.W)

    # btn = ttk.Button(self.window, text="Show", command = boxstates)
    # btn.pack(side=tk.RIGHT)

if __name__ == "__main__":
  root = tk.Tk()
  app = MainApplication(root)
  root.mainloop()