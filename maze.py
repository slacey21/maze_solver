from cell import Cell
from graphics import Point, Line
import random
import time
class Maze():
  def __init__(
      self,
      x1,
      y1,
      num_rows,
      num_cols,
      cell_size_x,
      cell_size_y,
      win=None,
      seed=None
    ):
    self._cells = []
    self._x1 = x1
    self._y1 = y1
    self._num_rows = num_rows
    self._num_cols = num_cols
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._win = win
    if seed:
      random.seed(seed)

    self._create_cells()
    self._break_entrance_and_exit()
    self._break_walls_r(0, 0)
    for col_list in self._cells:
      for cell in col_list:
        cell._reset_cells_visited()

  def _create_cells(self):
    for _ in range(self._num_cols):
      column_list = []
      for _ in range(self._num_rows):
        column_list.append(Cell(self._win))
      self._cells.append(column_list)

    for i in range(self._num_cols):
      for j in range(self._num_rows):
        self._draw_cell(i, j)

  def _draw_cell(self, i, j):
    if self._win is None:
      return
    x1 = self._x1 + (i * self._cell_size_x)
    y1 = self._y1 + (j * self._cell_size_y)
    x2 = x1 + self._cell_size_x
    y2 = y1 + self._cell_size_y
    self._cells[i][j].draw(x1, y1, x2, y2)
    self._animate()

  def _animate(self):
    if self._win is None:
      return
    self._win.redraw()
    time.sleep(.02)

  def _break_entrance_and_exit(self):
    self._cells[0][0].has_top_wall = False
    self._draw_cell(0, 0)
    self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
    self._draw_cell(self._num_cols - 1, self._num_rows - 1)
    
  def _break_walls_r(self, i, j):
    self._cells[i][j].visited = True

    while True:
      potential_cells_to_visit = []
      
      if i > 0 and not self._cells[i - 1][j].visited:
        potential_cells_to_visit.append((i - 1, j))
      if i < self._num_cols -1 and not self._cells[i + 1][j].visited:
        potential_cells_to_visit.append((i + 1, j))
      if j > 0 and not self._cells[i][j - 1].visited:
        potential_cells_to_visit.append((i, j - 1))
      if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
        potential_cells_to_visit.append((i, j + 1))

      if len(potential_cells_to_visit) == 0:
        self._draw_cell(i, j)
        return
    
      direction = random.randrange(0, len(potential_cells_to_visit))
      new_i, new_j = potential_cells_to_visit[direction][0], potential_cells_to_visit[direction][1]

      if new_i == i + 1:
        self._cells[i][j].has_right_wall = False
        self._cells[new_i][new_j].has_left_wall = False
      
      if new_i == i - 1:
        self._cells[i][j].has_left_wall = False
        self._cells[new_i][new_j].has_right_wall = False

      if new_j == j + 1:
        self._cells[i][j].has_bottom_wall = False
        self._cells[new_i][new_j].has_top_wall = False

      if new_j == j - 1:
        self._cells[i][j].has_top_wall = False
        self._cells[new_i][new_j].has_bottom_wall = False

      self._break_walls_r(new_i, new_j)

  def _draw_solved_maze_start(self):
    if self._win is None:
      return

    start_point_x = self._cells[0][0]._x1 + (self._cells[0][0]._x2 - self._cells[0][0]._x1) / 2
    start_point_y = self._cells[0][0]._y1
    end_point_x = self._cells[0][0]._x1 + (self._cells[0][0]._x2 - self._cells[0][0]._x1) / 2
    end_point_y = self._cells[0][0]._y1 + (self._cells[0][0]._y2 - self._cells[0][0]._y1) / 2
    
    start_point = Point(start_point_x, start_point_y)
    end_point = Point(end_point_x, end_point_y)

    start_line = Line(start_point, end_point)

    self._win.draw_line(start_line, fill_color="blue")

  def _draw_solved_maze_end(self):
    if self._win is None:
      return

    start_point_x = self._cells[-1][-1]._x1 + (self._cells[0][0]._x2 - self._cells[0][0]._x1) / 2
    start_point_y = self._cells[-1][-1]._y1 + (self._cells[-1][-1]._y2 - self._cells[-1][-1]._y1) / 2
    end_point_x = self._cells[-1][-1]._x1 + (self._cells[-1][-1]._x2 - self._cells[-1][-1]._x1) / 2
    end_point_y = self._cells[-1][-1]._y2 
    
    start_point = Point(start_point_x, start_point_y)
    end_point = Point(end_point_x, end_point_y)

    start_line = Line(start_point, end_point)

    self._win.draw_line(start_line, fill_color="blue")

  def solve(self):
    self._draw_solved_maze_start()
    self._solve_r(0, 0)
    self._draw_solved_maze_end()

  def _solve_r(self, i, j):
    self._animate()
    self._cells[i][j].visited = True
    
    if i == self._num_cols - 1  and j == self._num_rows - 1:
      return True

    # check cell to left
    if (
      i > 0
      and not self._cells[i][j].has_left_wall
      and not self._cells[i - 1][j].visited
      ):
      
      self._cells[i][j].draw_move(self._cells[i - 1][j])

      if self._solve_r(i - 1, j):
        return True
      else:
        self._cells[i][j].draw_move(self._cells[i - 1][j], True)

    # check cell to right
    if (
      i < self._num_cols - 1
      and not self._cells[i][j].has_right_wall
      and not self._cells[i + 1][j].visited
      ):
      
      self._cells[i][j].draw_move(self._cells[i + 1][j])

      if self._solve_r(i + 1, j):
        return True
      else:
        self._cells[i][j].draw_move(self._cells[i + 1][j], True)

    # check cell above
    if (
      j > 0
      and not self._cells[i][j].has_top_wall
      and not self._cells[i][j - 1].visited
      ):
      
      self._cells[i][j].draw_move(self._cells[i][j - 1])

      if self._solve_r(i, j - 1):
        return True
      else:
        self._cells[i][j].draw_move(self._cells[i][j - 1], True)

    # check cell below
    if (
      j < self._num_rows - 1
      and not self._cells[i][j].has_bottom_wall
      and not self._cells[i][j + 1].visited
      ):
      
      self._cells[i][j].draw_move(self._cells[i][j + 1])

      if self._solve_r(i, j + 1):
        return True
      else:
        self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)
    
    return False


