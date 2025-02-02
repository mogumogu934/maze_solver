from window import Window
from line import *

def main():
    win = Window(800, 600)
    point1 = Point(100, 100)
    point2 = Point(500, 500)
    point3 = Point(100, 100)
    point4 = Point(100, 300)
    lines = [Line(point1, point2), Line(point3, point4)]
    for line in lines:
        win.draw_line(line, "red")
    
    win.wait_for_close()

if __name__ == "__main__":
    main()
