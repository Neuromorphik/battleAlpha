
import unittest
import Board

class BoardTest(unittest.TestCase):

    def test_default_board_init(self):

        board = Board.Board()

        # verify that grid has 8 rows
        self.assertEqual(len(board.grid), 8)

        # verify that each row has 8 cells
        [self.assertEqual(len(board.grid[0]), 8)
        for i in range(len(board.grid))]

        # verify that all cells are set to 0
        [self.assertEqual(set(board.grid[i]), {0})
        for i in range(len(board.grid))]

        # verify that board_size is 8 and ship_size is 3 (Defaults)
        self.assertEqual(board.board_size, 8)
        self.assertEqual(board.ship_size, 3)

    def test_modified_board_init(self):

        board = Board.Board(board_size = 10, ship_size = 2)

        # verify that grid has 10 rows
        self.assertEqual(len(board.grid), 10)

        # verify that each row has 10 cells
        [self.assertEqual(len(board.grid[0]), 10)
        for i in range(len(board.grid))]

        # verify that all cells are set to 0
        [self.assertEqual(set(board.grid[i]), {0})
        for i in range(len(board.grid))]

        # verify that board_size is 10 and ship_size is 2
        self.assertEqual(board.board_size, 10)
        self.assertEqual(board.ship_size, 2)

    def test_invalid_board_init(self):

        # If we try to init with board_size <= 0, should use default sizes
        board = Board.Board(board_size = 0)
        self.assertEqual(board.board_size, 8)
        self.assertEqual(board.ship_size, 3)

        board = Board.Board(board_size = -1)
        self.assertEqual(board.board_size, 8)
        self.assertEqual(board.ship_size, 3)

        # if we try to init with ship_size <= 0, should use default sizes
        board = Board.Board(ship_size = 0)
        self.assertEqual(board.board_size, 8)
        self.assertEqual(board.ship_size, 3)

        board = Board.Board(ship_size = -1)
        self.assertEqual(board.board_size, 8)
        self.assertEqual(board.ship_size, 3)

        # if we try to init with ship_size >= board_size, should use default sizes
        board = Board.Board(board_size = 5, ship_size = 10)
        self.assertEqual(board.board_size, 8)
        self.assertEqual(board.ship_size, 3)

    def test_coordinates_are_valid(self):

        board = Board.Board() # default (8x8 board, 3x1 ship)

        # test valid coordinates
        self.assertEqual(board.coordinates_are_valid(0, 0), True) # edge case
        self.assertEqual(board.coordinates_are_valid(7, 7), True) # edge case
        self.assertEqual(board.coordinates_are_valid(4, 4), True)

        # test invalid coordinates
        self.assertEqual(board.coordinates_are_valid(-1, 0), False) # neg row
        self.assertEqual(board.coordinates_are_valid(0, -1), False) # neg col
        self.assertEqual(board.coordinates_are_valid(-1, -1), False) # neg row & col
        self.assertEqual(board.coordinates_are_valid(10, 0), False) # too big row
        self.assertEqual(board.coordinates_are_valid(0, 10), False) # too big col
        self.assertEqual(board.coordinates_are_valid(10, 10), False) # too big row & col

    def test_update_cell_AND_get_value_of_cell(self):

        board = Board.Board() # default (8x8 board, 3x1 ship)

        # test valid updates
        self.assertEqual(board.get_value_of_cell(0, 0), 0) # cell should start as 0
        board.update_cell(0, 0, board.cell_states['EMPTY']) # update that cell to 0
        self.assertEqual(board.get_value_of_cell(0, 0), 0) # should still be 0

        board.update_cell(0, 0, board.cell_states['MISS']) # update that cell to 1
        self.assertEqual(board.get_value_of_cell(0, 0), 1) # should be 1

        board.update_cell(0, 0, board.cell_states['SHIP_OK']) # update that cell to 2
        self.assertEqual(board.get_value_of_cell(0, 0), 2) # should be 2

        board.update_cell(0, 0, board.cell_states['SHIP_HIT']) # update that cell to 3
        self.assertEqual(board.get_value_of_cell(0, 0), 3) # should be 3

        # test invalid updates
        board.update_cell(0, 0, -1) # try neg value
        self.assertEqual(board.get_value_of_cell(0, 0), 3) # should fail and still be 3

        board.update_cell(0, 0, 4) # try too big value
        self.assertEqual(board.get_value_of_cell(0, 0), 3) # should fail and still be 3
