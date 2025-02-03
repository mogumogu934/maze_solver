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
                
    def test_maze_create_cells_check_walls(self):
        m1 = Maze(54, 54, 4, 4, 54, 54)
        for col in m1._cells:
            for cell in col:
                self.assertTrue(cell.has_left_wall)
                self.assertTrue(cell.has_right_wall)
                self.assertTrue(cell.has_top_wall)
                self.assertTrue(cell.has_bottom_wall)
        
    def test_maze_create_cells_check_visited_status(self):
        m1 = Maze(54, 54, 4, 4, 54, 54)
        for col in m1._cells:
            for cell in col:
                self.assertFalse(cell.visited)
    
    def test_maze_break_entrance_and_exit(self):
        m1 = Maze(54, 54, 4, 4, 54, 54)
        m1._break_entrance_and_exit()
        self.assertTrue(m1._cells[0][0].has_left_wall)
        self.assertTrue(m1._cells[0][0].has_right_wall)
        self.assertTrue(m1._cells[0][0].has_bottom_wall)
        self.assertFalse(m1._cells[0][0].has_top_wall)
        
        self.assertTrue(m1._cells[-1][-1].has_left_wall)
        self.assertTrue(m1._cells[-1][-1].has_right_wall)
        self.assertTrue(m1._cells[-1][-1].has_top_wall)
        self.assertFalse(m1._cells[-1][-1].has_bottom_wall)
        
if __name__ == "__main__":
    unittest.main()
    