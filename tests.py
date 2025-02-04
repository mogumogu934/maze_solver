import unittest
from cell import Cell
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells_1(self):
        m1 = Maze(54, 54, 6, 6, 54, 54)
        self.assertEqual(len(m1._cells), 6)
        self.assertEqual(len(m1._cells[0]), 6)
        
    def test_maze_create_cells_invalid_1(self):
        with self.assertRaises(ValueError):
            m1 = Maze(54, 54, 0, 0, 54, 54)

    def test_maze_create_cells_invalid_2(self):
        with self.assertRaises(ValueError):
            m1 = Maze(54, 54, -2, -2, 54, 54)
            
    def test_maze_create_cells_class_object(self):
        m1 = Maze(54, 54, 4, 4, 54, 54)
        for col in m1._cells:
            for cell in col:
                self.assertTrue(isinstance(cell, Cell))
        
    def test_maze_create_cells_check_visited_status(self):
        m1 = Maze(54, 54, 4, 4, 54, 54)
        for col in m1._cells:
            for cell in col:
                self.assertTrue(cell.visited)
        
if __name__ == "__main__":
    unittest.main()
    