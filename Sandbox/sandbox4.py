from tkinter import *
root = Tk()


def round_rectangle_text(_canvas, x1, y1, x2, y2, radius=25, row=0, col=0, _text='default', **kwargs):
    canvas = Canvas(_canvas, height=y2-y1/2, width=x2)
    canvas.grid(row=row, column=col, padx=0)
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
    new_text = canvas.create_text((x1+x2)/2,(y1+y2)/2, text=_text)      # center the text

# my_rectangle = round_rectangle(canvas, 10, 10, 100, 25, radius=20, fill="gray")

for i in range(5):
    round_rectangle_text(root, 5, 5, 100, 25, radius=20, row=0, col=i, _text="above", fill="gray")
    round_rectangle_text(root, 5, 5, 100, 25, radius=20, row=1, col=i, _text="A", fill="gray")


root.mainloop()