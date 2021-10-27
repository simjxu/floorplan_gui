from tkinter import *
root = Tk()


def round_rectangle(root, x1, y1, x2, y2, radius=25, col=0, **kwargs):
    canvas = Canvas(root,width=100)
    canvas.grid(row=0, column=col, padx=0)
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    new_poly = canvas.create_polygon(points, **kwargs, smooth=True)
    new_text = canvas.create_text(50,15, text="test")

# my_rectangle = round_rectangle(canvas, 10, 10, 100, 25, radius=20, fill="gray")

for i in range(5):
    round_rectangle(root, 10, 10, 100, 25, radius=20, col=i, fill="gray")


root.mainloop()