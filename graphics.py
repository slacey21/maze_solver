from tkinter import Tk, BOTH, Canvas

class Window():
  def __init__(self, width, height):
    self.__root = Tk()
    self.__root.geometry(f"{width}x{height}")
    self.__root.title = "Maze Window"
    self.__canvas = Canvas(self.__root, width=width, height=height)
    self.__canvas.pack()
    self.__window_running = False
    self.__root.protocol("WM_DELETE_WINDOW", self.close)
  
  def redraw(self):
    self.__root.update_idletasks()
    self.__root.update()
  
  def wait_for_close(self):
    self.__window_running = True
    while self.__window_running:
      self.redraw()

  def close(self):
    self.__window_running = False

  def draw_line(self, line, fill_color="red"):
    line.draw(self.__canvas, fill_color)


class Point():
  def __init__(self, x, y):
    self.x = x
    self.y = y


class Line():
  def __init__(self, first_point, second_point):
    self.__first_point = first_point
    self.__second_point = second_point

  def draw(self, canvas, fill_color):
    canvas.create_line(
      self.__first_point.x,
      self.__first_point.y,
      self.__second_point.x,
      self.__second_point.y,
      fill=fill_color,
      width=2
    )
    canvas.pack()