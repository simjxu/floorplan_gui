import tkinter as tk
from tkinter import ttk
import os
import time

class Legend:
  def __init__(self, parent, **kwargs):
    self.savefile = parent.yaml_file
    self.parent = parent

    # Create an empty text file in the Floorplan folder that will hold the selected items
    # so the next time it opens it reloads from that file
    self.checkbox_selected_file = \
      '/Users/simonxu/Documents/Github-simjxu/floorplan_gui/checkbox_selected.txt'
    with open(self.checkbox_selected_file) as f:
      comma_string = f.readline()
    self.checkbox_selected = [int(x) for x in comma_string.split(',')]
    f.close()

    # New window for the Legend
    self.window = tk.Toplevel()     # Top level needed, don't totally understand why not tk.Tk()
    self.window.geometry("200x700+1210+100")
    self.window.title("Legend")
    self.window.attributes('-topmost', True)

    # Buttons must be under a frame
    save_frame = tk.Frame(self.window)
    save_frame.pack()

    # Create save button
    save_button = tk.Button(save_frame, text="SAVE", fg="black", command=self.save)
    save_button.pack(pady=(0,20))

    # Create the scrollable frame
    self.containerframe = tk.Frame(self.window)
    self.containerframe.pack()
    self.maincanvas = tk.Canvas(self.containerframe, \
			height=500, width=150, highlightthickness=0)
    self.maincanvas.pack(side=tk.LEFT)
    # self.maincanvas.bind("<MouseWheel>", self._on_mousewheel)

    # Create a horizontal scrollbar linked to the container frame.
    self.vsbar = tk.Scrollbar(self.containerframe, orient=tk.VERTICAL, command=self.maincanvas.yview)
    self.vsbar.pack(side=tk.LEFT, fill='y')

    self.mainframe = tk.Frame(self.maincanvas) # scrollable
    self.mainframe.pack()

  
    self.maincanvas.configure(yscrollcommand=self.vsbar.set)

    self.mainframe.bind(
			"<Configure>",
			lambda e: self.maincanvas.configure(
					scrollregion=self.maincanvas.bbox("all")
				)
		)
    self.maincanvas.create_window((0,0), window=self.mainframe, anchor=tk.NW)

    # Create Checkboxes
    self.checkarray = []
    self.checkboxes = []
    
    for i in range(len(parent.yaml_obj.BUILD_NAMES)):
      build_name = parent.yaml_obj.BUILD_NAMES[i]
      self.checkarray.append(tk.IntVar())
      self.checkboxes.append(ttk.Checkbutton(self.mainframe, text=build_name, variable=self.checkarray[i], \
        onvalue=1, offvalue=0))
      self.checkboxes[i].pack(side=tk.TOP, anchor=tk.W, pady=(10,0), padx=(0,0))

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

    # Select the initial builds to show
    self.set_initial_checkboxes()


  # Pass in all YAML data into Legend object
  # Can be called when move is made
  def update_yaml(self, **kwargs):
    build_name = kwargs['build_name']
    label = kwargs['label']
    date = kwargs['date']
    self.parent.yaml_obj.update_dates(build_name=build_name, label=label, \
      date=date)
  
  def save(self):
    # Only sort the yaml object on save, which allows a new marker to be moved around
    self.parent.yaml_obj.sort_all_dates()
    self.parent.yaml_obj.save_current(self.savefile)
    # Update dates in git repo
    os.system("cd /Users/simonxu/Documents/Github-simjxu/floorplan_gui/Floorplan_YAMLs && make git")

  def update_canvas(self):
    print("update")

  def reload(self):
    open(self.checkbox_selected_file, 'w').close()
    # Set the parent checkbox array equal to this one
    with open(self.checkbox_selected_file, 'w') as f:
      for i in range(len(self.checkarray)):
        self.parent.checkbox_arr[i] = self.checkarray[i].get()
      
        if i==0:
          f.write(str(self.checkarray[i].get()))
        else:
          f.write(',')
          f.write(str(self.checkarray[i].get()))

    self.parent.load_builds()
    self.parent.load_timelines()

  def clear(self):
    for checkbox in self.checkarray:
      checkbox.set(0)
  
  def set_initial_checkboxes(self):
    for i in range(len(self.checkbox_selected)):
      self.checkarray[i].set(self.checkbox_selected[i])
    self.reload()

  def select_all(self):
    for checkbox in self.checkarray:
      checkbox.set(1)

  # This doesn't work
  # def _on_mousewheel(self, event):
  #   self.maincanvas.yview_scroll(-1*event.delta, "units")

class MainApplication:
  def __init__(self, parent, **kwargs):
    self.legend = Legend(self)

if __name__ == "__main__":
  root = tk.Tk()
  app = MainApplication(root)
  root.mainloop()