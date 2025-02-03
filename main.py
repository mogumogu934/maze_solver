from graphics import Window
from maze import Maze

def main():
    screen_width = 1080
    screen_height = 1080
    margin = 54
    num_rows = 18
    num_cols = 18
    cell_size_x = int((screen_width - 2 * margin) / num_cols) # 54
    cell_size_y = int((screen_height - 2 * margin) / num_rows) # 54
    
    win = Window(screen_width, screen_height)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()
