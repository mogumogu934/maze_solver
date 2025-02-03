from constants import *
from graphics import Window
from maze import Maze

def main():
    win = Window(screen_width, screen_height)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze._break_entrance_and_exit()
    
    win.wait_for_close()

if __name__ == "__main__":
    main()
