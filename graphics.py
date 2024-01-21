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

