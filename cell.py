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

  def draw_move(self, to_cell, undo=False):
    curr_width = self._x2 - self._x1
    curr_height = self._y2 - self._y1
    next_width = to_cell._x2 - to_cell._x1
    next_height = to_cell._y2 - to_cell._y1

    curr_center = Point(self._x1 + curr_width / 2, self._y1 + curr_height / 2)
    next_center = Point(to_cell._x1 + next_width / 2, to_cell._y1 + next_height / 2)

    move_line = Line(curr_center, next_center)

    if undo:
      self._win.draw_line(move_line, fill_color="gray")
    else:
      self._win.draw_line(move_line, fill_color="red")
