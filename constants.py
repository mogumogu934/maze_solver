screen_width = 1080
screen_height = 1080
min_dimension = min(screen_width, screen_height)
margin = int(min_dimension * 0.025) # 27

num_rows = 6 # int(min_dimension * (0.025 * 2 / 3)) # 18
num_cols = 6 # int(min_dimension * (0.025 * 2 / 3)) # 18
cell_size_x = int((min_dimension - 2 * margin) / num_cols) # 54
cell_size_y = int((min_dimension - 2 * margin) / num_rows) # 54

# Create offsets to center the maze when screen resolution is not a square
maze_width = num_cols * cell_size_x + (2 * margin)
maze_height = num_rows * cell_size_y + (2 * margin)
maze_x_offset = (screen_width - maze_width) // 2
maze_y_offset = (screen_height - maze_height) // 2