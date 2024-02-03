from graphics import Window
from maze import Maze
import sys
import math

def get_maze_difficulty():
  cl_arguments = sys.argv
  difficulties = {'e': 6, 'm': 12, 'h': 18}
  if (
    len(cl_arguments) == 2
    and len(cl_arguments[1]) == 2
    and cl_arguments[1][0] == '-'
    and cl_arguments[1][1].lower() in ['e', 'm', 'h']
    ):
    difficulty = difficulties[cl_arguments[1][1].lower()]
  elif len(cl_arguments) == 1:
    difficulty = difficulties['m']
  else:
    print('ERROR: correct usage -> python main.py [-difficulty]')
    print('Difficulty flags are: -e (easy), -m (medium), or -h (hard)')    
    sys.exit()

  return difficulty

def main():
  num_rows, num_cols = get_maze_difficulty(), get_maze_difficulty()
  maze_start_x, maze_start_y = 10, 10

  window_width = 1000
  window_height = 800

  maze_total_width = window_width - 2 * maze_start_x
  maze_total_height = window_height - 2 * maze_start_y

  maze_cell_width = int(math.floor(maze_total_width / num_rows))
  maze_cell_height = int(math.floor(maze_total_height /  num_cols))

  win = Window(window_width, window_height)
  maze = Maze(maze_start_x,
              maze_start_y,
              num_rows,
              num_cols,
              maze_cell_width,
              maze_cell_height,
              win)
  maze.solve()

  win.wait_for_close()

if __name__ == "__main__":
  main()
