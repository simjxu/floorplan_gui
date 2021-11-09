import tkinter as tk

class RCMenu:
	def __init__(self, parent, *args, **kwargs):
		self.popup_menu = tk.Menu(tearoff=0)
		self.popup_menu.add_command(label="Delete",
																command=self.delete_selected)
		self.popup_menu.add_command(label="Select All",
																command=self.select_all)

		parent.parent.bind("<Button-2>", self.popup) # Button-2 on Aqua

	def popup(self, event):
		print("clicked")
		try:
			self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
		finally:
			self.popup_menu.grab_release()

	def delete_selected(self):
		print("delete")

	def select_all(self):	
		print("select all")

class MainApplication:
  def __init__(self, parent, **kwargs):
    self.legend = RCMenu(self)
  
if __name__ == "__main__":
  root = tk.Tk()
  app = MainApplication(root)
  root.mainloop()