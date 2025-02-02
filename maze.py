from constants import maze_x_offset, maze_y_offset
from cell import Cell
from graphics import Window
import time

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
    ):
        self._x1 = x1 + maze_x_offset
        self._y1 = y1 + maze_y_offset
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        
        self._create_cells()
    
    def _create_cells(self):
        if self._num_rows < 3 or self._num_cols < 3:
            raise ValueError("Screen resolution is too small. Cannot create a valid maze.")
        self._cells = []
        for i in range (self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                self._cells[i].append(Cell(self._win))
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        cell_x1 = self._x1 + (i * self._cell_size_x) # i = column number
        cell_y1 = self._y1 + (j * self._cell_size_y) # j = row number
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_x
        
        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.025)
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1) # _draw_cell needs the actual indices
        