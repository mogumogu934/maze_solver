screen_width = 1920
screen_height = 1080
min_dimension = min(screen_width, screen_height)
margin = int(min_dimension * 0.012) # 12

num_rows = int(screen_height * 0.03) # 32
num_cols = int(num_rows * (screen_width / screen_height)) # 56
cell_size_x = (screen_width - margin) / (num_rows * 2) # int((min_dimension - 2 * margin) / num_cols) # 29
cell_size_y = cell_size_x # int((min_dimension - 2 * margin) / num_rows) # 24

# Create offsets to center the maze when screen resolution is not a square
# maze_width = num_cols * cell_size_x + (2 * margin)
# maze_height = num_rows * cell_size_y + (2 * margin)
# maze_x_offset = (screen_width - maze_width) // 2
# maze_y_offset = (screen_height - maze_height) // 2