screen_width = 1920
screen_height = 1080
min_dimension = min(screen_width, screen_height)
margin = int(min_dimension * 0.015) # 16

cell_size_x = margin * 2 # 32
cell_size_y = cell_size_x
num_cols = (screen_width - margin * 2) // cell_size_x # 59
num_rows = (screen_height - margin * 2) // cell_size_y # 32

# Create offsets to center the maze when screen resolution is not a square
maze_width = num_cols * cell_size_x + (margin * 2)
maze_height = num_rows * cell_size_y + (margin * 2)
maze_x_offset = (screen_width - maze_width) // 2
maze_y_offset = (screen_height - maze_height) // 2