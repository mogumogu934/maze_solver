from constants import maze_x_offset, maze_y_offset
from cell import Cell
import time
from enum import Enum
import random

class Maze:
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
        self._x1 = x1 + maze_x_offset
        self._y1 = y1 + maze_y_offset
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
    
    def _create_cells(self):
        if self._num_rows < 3 or self._num_cols < 3:
            raise ValueError("Screen resolution is too small. Cannot create a valid maze.")
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_x
        
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True    # i = column number (x position), j = row number (y position)
        
        while True:
            to_visit = {}
            if j > 0 and not self._cells[i][j - 1].visited:   # cell above
                to_visit["up"] = (i, j - 1)
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:  # cell below
                to_visit["down"] = (i, j + 1)
            if i > 0 and not self._cells[i - 1][j].visited:   # cell left
                to_visit["left"] = (i - 1, j)
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:  # cell right
                to_visit["right"] = (i + 1, j)
                
            if not to_visit:
                self._draw_cell(i, j)
                return
            
            else:
                direction = random.choice(list(to_visit.keys()))
                next_cell_i = to_visit[direction][0]
                next_cell_j = to_visit[direction][1]
                
                if direction == "up":
                    self._cells[i][j].has_top_wall = False
                    self._cells[next_cell_i][next_cell_j].has_bottom_wall = False
                elif direction == "down":
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[next_cell_i][next_cell_j].has_top_wall = False
                elif direction == "left":
                    self._cells[i][j].has_left_wall = False
                    self._cells[next_cell_i][next_cell_j].has_right_wall = False
                elif direction == "right":
                    self._cells[i][j].has_right_wall = False
                    self._cells[next_cell_i][next_cell_j].has_left_wall = False
                    
                self._break_walls_r(next_cell_i, next_cell_j)
                