
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
