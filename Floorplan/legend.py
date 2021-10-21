import tkinter as tk

class Legend:
  def __init__(self, parent, **kwargs):
    self.savefile = "./Sample_YAML/savefile.yaml"
    self.testtext = "ABC"   # For testing, delete
    self.parent = parent

    # New window for the Legend
    self.window = tk.Tk()
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
    print("reload")

class MainApplication:
	def __init__(self, parent, **kwargs):
		self.legend = Legend()

if __name__ == "__main__":
  root = tk.Tk()
  app = MainApplication(root)
  root.mainloop()