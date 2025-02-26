from constants import *
from graphics import Window
from maze import Maze

def main():
    win = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    maze = Maze(MARGIN, MARGIN, MAZE_NUM_COLS, MAZE_NUM_ROWS, MAZE_CELL_SIZE_X, MAZE_CELL_SIZE_Y, win)
    num_cells = MAZE_NUM_COLS * MAZE_NUM_ROWS
    print(f"Created a maze with {num_cells} cells.")
    maze.solve()
    
    win.wait_for_close()

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(6000)
    if MIN_DIMENSION > 1080:
        sys.setrecursionlimit(12000)
    if MIN_DIMENSION >= 2160:
        sys.setrecursionlimit(18000)
        
    main()
