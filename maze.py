from cell import Cell
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
        seed=None,
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
        self._reset_cells_visited()
    
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
        x1 = self._x1 + (i * self._cell_size_x) # i = column number (x position)
        y1 = self._y1 + (j * self._cell_size_y) # j = row number (y position)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_x
        
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate(0.0125)
    
    def _animate(self, wait_length):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(wait_length)
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True    # i = column number (x position), j = row number (y position)
        
        while True:
            possible_directions = {}
            if j > 0 and not self._cells[i][j - 1].visited:   # cell above
                possible_directions["up"] = (i, j - 1)
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:  # cell below
                possible_directions["down"] = (i, j + 1)
            if i > 0 and not self._cells[i - 1][j].visited:   # cell left
                possible_directions["left"] = (i - 1, j)
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:  # cell right
                possible_directions["right"] = (i + 1, j)
                
            if not possible_directions:
                self._draw_cell(i, j)
                return
            
            else:
                direction = random.choice(list(possible_directions.keys()))
                next_cell_i = possible_directions[direction][0]
                next_cell_j = possible_directions[direction][1]
                
                if direction == "down":
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[next_cell_i][next_cell_j].has_top_wall = False
                elif direction == "right":
                    self._cells[i][j].has_right_wall = False
                    self._cells[next_cell_i][next_cell_j].has_left_wall = False
                elif direction == "up":
                    self._cells[i][j].has_top_wall = False
                    self._cells[next_cell_i][next_cell_j].has_bottom_wall = False
                elif direction == "left":
                    self._cells[i][j].has_left_wall = False
                    self._cells[next_cell_i][next_cell_j].has_right_wall = False
                    
                self._break_walls_r(next_cell_i, next_cell_j)
                
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
                
    def solve(self):
        return self._solve_r(0, 0)
        
    def _solve_r(self, i, j):
        self._animate(0.025)
        self._cells[i][j].visited = True    # i = column number (x position), j = row number (y position)
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        if j < self._num_rows - 1 and not self._cells[i][j + 1].has_top_wall and not self._cells[i][j + 1].visited:  # cell below
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)
                
        if i < self._num_cols - 1 and not self._cells[i + 1][j].has_left_wall and not self._cells[i + 1][j].visited:  # cell right
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)
                
        if j > 0 and not self._cells[i][j - 1].has_bottom_wall and not self._cells[i][j - 1].visited:   # cell above
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)
                
        if i > 0 and not self._cells[i - 1][j].has_right_wall and not self._cells[i - 1][j].visited:   # cell left
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True               
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)
                
        return False
    