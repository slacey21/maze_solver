from graphics import Point, Line

class Cell():
  def __init__(self, win=None):
    self._win = win
    self._x1 = None
    self._y1 = None
    self._x2 = None
    self._y2 = None
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self.visited = False

  def draw(self, x1, y1, x2, y2):
    self._x1 = x1
    self._y1 = y1
    self._x2 = x2
    self._y2 = y2

    if self._win:
      left_wall_line = Line(Point(x1, y1), Point(x1, y2))
      right_wall_line = Line(Point(x2, y1), Point(x2, y2))
      top_wall_line = Line(Point(x1, y1), Point(x2, y1))
      bottom_wall_line = Line(Point(x1, y2), Point(x2, y2))

      if self.has_left_wall:
        self._win.draw_line(left_wall_line)
      else:
        self._win.draw_line(left_wall_line, fill_color=self._win.get_canvas_background())

      if self.has_right_wall:
        self._win.draw_line(right_wall_line)
      else:
        self._win.draw_line(right_wall_line, fill_color=self._win.get_canvas_background())

      if self.has_top_wall:
        self._win.draw_line(top_wall_line)
      else:
        self._win.draw_line(top_wall_line, fill_color=self._win.get_canvas_background())
        
      if self.has_bottom_wall:
        self._win.draw_line(bottom_wall_line)
      else:
        self._win.draw_line(bottom_wall_line, fill_color=self._win.get_canvas_background())

  def draw_move(self, to_cell, undo=False):
    if self._win is None:
      return
    
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

  def _reset_cells_visited(self):
    self.visited = False