from graphics import Point, Line

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

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
            self._win.draw_line(left_wall, "black")
        if self.has_right_wall:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_wall)
        else:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_wall, "black")
        if self.has_top_wall:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_wall)
        else:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_wall, "black")
        if self.has_bottom_wall:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_wall)
        else:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_wall, "black")
    
    def draw_move(self, to_cell, undo=False):
        from_half_length = abs(self._x2 - self._x1) // 2
        to_half_length = abs(to_cell._x2 - to_cell._x1) // 2
        
        x_center_1 = self._x1 + from_half_length
        y_center_1 = self._y1 + from_half_length
        
        x_center_2 = to_cell._x1 + to_half_length
        y_center_2 = to_cell._y1 + to_half_length
        
        fill_color = "#acfec0"
        if undo:
            fill_color = "red"
            
        line = Line(Point(x_center_1, y_center_1), Point(x_center_2, y_center_2))
        self._win.draw_line(line, fill_color)
