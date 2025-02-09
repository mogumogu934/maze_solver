from constants import *
from graphics import Window
from maze import Maze

def main():
    win = Window(screen_width, screen_height)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    num_cells = num_rows * num_cols
    print(f"Created a maze with {num_cells} cells.")
    maze.solve()
    
    win.wait_for_close()

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(4500)
    main()
