import unittest
from cell import Cell
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells_1(self):
        num_cols = 18
        num_rows = 18
        m1 = Maze(54, 54, num_rows, num_cols, 54, 54)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
        
    def test_maze_create_cells_2(self):
        num_cols = 4
        num_rows = 4
        m1 = Maze(54, 54, num_rows, num_cols, 54, 54)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
        
    def test_maze_create_cells_invalid_1(self):
        num_cols = 0
        num_rows = 0
        with self.assertRaises(ValueError):
            m1 = Maze(54, 54, num_rows, num_cols, 54, 54)

    def test_maze_create_cells_invalid_2(self):
        num_cols = -2
        num_rows = -2
        with self.assertRaises(ValueError):
            m1 = Maze(54, 54, num_rows, num_cols, 54, 54)
            
    def test_maze_create_cells_class_object(self):
        num_cols = 4
        num_rows = 4
        m1 = Maze(54, 54, num_rows, num_cols, 54, 54)
        for col in m1._cells:
            for cell in col:
                self.assertTrue(isinstance(cell, Cell))
                
    def test_maze_create_cells_check_walls(self):
        num_cols = 6
        num_rows = 6
        m1 = Maze(54, 54, num_rows, num_cols, 54, 54)
        for col in m1._cells:
            for cell in col:
                self.assertTrue(cell.has_left_wall)
                self.assertTrue(cell.has_right_wall)
                self.assertTrue(cell.has_top_wall)
                self.assertTrue(cell.has_bottom_wall)
        
    def test_maze_create_cells_check_visited_status(self):
        num_cols = 6
        num_rows = 6
        m1 = Maze(54, 54, num_rows, num_cols, 54, 54)
        for col in m1._cells:
            for cell in col:
                self.assertFalse(cell.visited)
        
if __name__ == "__main__":
    unittest.main()
    