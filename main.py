from graphics import Window
from maze import Maze

def main():
    screen_width = 1080
    screen_height = 1080
    margin = int(screen_width * 0.05)
    num_rows = int(screen_width * 0.015)
    num_cols = int(screen_width * 0.015)
    cell_size_x = (screen_width - 2 * margin) / num_cols
    cell_size_y = (screen_height - 2 * margin) / num_rows
    
    win = Window(screen_width, screen_height)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()
