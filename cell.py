from graphics import Point, Line

class Cell():
  def __init__(self, win):
    self._win = win
    self._x1 = None
    self._y1 = None
    self._x2 = None
    self._y2 = None
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True

  def draw(self, x1, y1, x2, y2):
    self._x1 = x1
    self._y1 = y1
    self._x2 = x2
    self._y2 = y2

    if self.has_left_wall:
      left_wall_line = Line(Point(x1, y1), Point(x1, y2))
      self._win.draw_line(left_wall_line)

    if self.has_right_wall:
      right_wall_line = Line(Point(x2, y1), Point(x2, y2))
      self._win.draw_line(right_wall_line)

    if self.has_top_wall:
      top_wall_line = Line(Point(x1, y2), Point(x2, y2))
      self._win.draw_line(top_wall_line)
      
    if self.has_bottom_wall:
      bottom_wall_line = Line(Point(x1, y1), Point(x2, y1))
      self._win.draw_line(bottom_wall_line)
