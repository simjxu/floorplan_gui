import tkinter as tk
from tkinter import ttk
from tkinter.constants import ANCHOR, W

class Legend:
  def __init__(self, parent, **kwargs):
    self.savefile = './YAMLs/x_sys.yaml'
    self.testtext = "ABC"   # For testing, delete
    self.parent = parent

    # New window for the Legend
    self.window = tk.Toplevel()     # Top level needed, don't totally understand why not tk.Tk()
    self.window.geometry("200x700+1210+100")
    self.window.title("Legend")

    # Buttons must be under a frame
    save_frame = tk.Frame(self.window)
    save_frame.pack()

    # Create save button
    save_button = tk.Button(save_frame, text="SAVE", fg="black", command=self.save)
    save_button.pack(pady=(0,20))

    # Create Checkboxes
    self.checkarray = []
    self.checkboxes = []
    
    for i in range(len(parent.yaml_obj.BUILD_NAMES)):
      build_name = parent.yaml_obj.BUILD_NAMES[i]
      self.checkarray.append(tk.IntVar())
      self.checkboxes.append(ttk.Checkbutton(self.window, text=build_name, variable=self.checkarray[i], \
        onvalue=1, offvalue=0))
      self.checkboxes[i].pack(side=tk.TOP, anchor=tk.W, pady=(10,0), padx=(50,0))

    # Buttons for update frame
    update_frame = tk.Frame(self.window)
    update_frame.pack(pady=20)

    # Create reload button
    reload_button = tk.Button(update_frame, text="UPDATE", fg="black", command=self.reload, pady=10)
    reload_button.pack()

    # Create clear checks button
    clearcheck_button = tk.Button(update_frame, text="CLEAR", fg="black", command=self.clear)
    clearcheck_button.pack()

    # Create clear checks button
    selectall_button = tk.Button(update_frame, text="SELECT ALL", fg="black", command=self.select_all)
    selectall_button.pack()


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
    # Set the parent checkbox array equal to this one
    for i in range(len(self.checkarray)):
      self.parent.checkbox_arr[i] = self.checkarray[i].get()
    self.parent.load_builds()
    self.parent.load_timelines()
  
  def clear(self):
    for checkbox in self.checkarray:
      checkbox.set(0)

  def select_all(self):
    for checkbox in self.checkarray:
      checkbox.set(1)

class MainApplication:
  def __init__(self, parent, **kwargs):
    self.legend = Legend(self)

if __name__ == "__main__":
  root = tk.Tk()
  app = MainApplication(root)
  root.mainloop()