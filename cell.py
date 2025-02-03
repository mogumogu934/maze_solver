from graphics import Point, Line

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        if self.has_left_wall:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_wall)
            
        else:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_wall, "white")
            
        if self.has_right_wall:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_wall)
            
        else:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_wall, "white")
            
        if self.has_top_wall:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_wall)
            
        else:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_wall, "white")
            
        if self.has_bottom_wall:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_wall)
            
        else:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_wall, "white")
    
    def draw_move(self, to_cell, undo=False):
        from_half_length1 = abs(self._x2 - self._x1) // 2
        to_half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        
        from_center_x = self._x1 + from_half_length1
        from_center_y = self._y1 + from_half_length1
        
        to_center_x = to_cell._x1 + to_half_length2
        to_center_y = to_cell._y1 + to_half_length2
        
        line = Line(Point(from_center_x, from_center_y), Point(to_center_x, to_center_y))
        fill_color = "grey" if undo else "red"
        self._win.draw_line(line, fill_color)
