from constants import maze_x_offset, maze_y_offset
from cell import Cell
from graphics import Window
import time
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
        self._x1 = x1 + maze_x_offset
        self._y1 = y1 + maze_y_offset
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self.seed = seed
        
        if seed:
            random.seed(seed)
            
        self._create_cells()
    
    def _create_cells(self):
        if self._num_rows < 3 or self._num_cols < 3:
            raise ValueError("Screen resolution is too small. Cannot create a valid maze.")
        self._cells = []
        for i in range(self._num_rows):
            self._cells.append([])
            for j in range(self._num_cols):
                self._cells[i].append(Cell(self._win))
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        cell_x1 = self._x1 + (i * self._cell_size_x) # i = row number
        cell_y1 = self._y1 + (j * self._cell_size_y) # j = column number
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_x
        
        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
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
        current_cell = self._cells[i][j]  # i = row number, j = column number
        current_cell.visited = True
        
        while True:
            possible_directions = []
            cell_above = None
            cell_below = None
            cell_left = None
            cell_right = None
            
            if i > 0 and not self._cells[i-1][j].visited:
                cell_above = self._cells[i-1][j]
                possible_directions.append(cell_above)
                
            if i < self._num_rows - 1 and not self._cells[i+1][j].visited:
                cell_below = self._cells[i+1][j]
                possible_directions.append(cell_below)
                
            if j > 0 and not self._cells[i][j-1].visited:
                cell_left = self._cells[i][j-1]
                possible_directions.append(cell_left)
                
            if j < self._num_cols - 1 and not self._cells[i][j+1].visited:
                cell_right = self._cells[i][j+1]
                possible_directions.append(cell_right)
            
            if possible_directions:
                next_cell = random.choice(possible_directions)
                if next_cell == cell_above:
                    current_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False
                    new_i = i - 1
                    new_j = j
                    
                elif next_cell == cell_below:
                    current_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False
                    new_i = i + 1
                    new_j = j
                    
                elif next_cell == cell_left:
                    if not (i == 0 and j == 0):
                        current_cell.has_left_wall = False
                        next_cell.has_right_wall = False
                    new_i = i
                    new_j = j - 1
                    
                elif next_cell == cell_right:
                    if not (i == self._num_rows - 1 and j == self._num_cols - 1):
                        current_cell.has_right_wall = False
                        next_cell.has_left_wall = False
                    new_i = i
                    new_j = j + 1
                    
                self._break_walls_r(new_i, new_j)
            
            else:
                self._draw_cell(i, j)
                return
            