
# boards are square, the size determines length
DEFAULT_BOARD_SIZE = 8
DEFAULT_SHIP_SIZE = 3

##
# Board class implements the logic of a battleship board for one player.
# When instantiated, Board object is given a grid of board_size * board_size
# with all cells set to 0 (considered EMPTY).
# Ships can be added with the add_ship method which accepts a list of (row,column)
# tuples, ships will only be added if the placement coordinates are valid.
# Methods exist to check if coordinates are valid, to update cells, get cells,
# reset the board, and check if the ship has been destroyed.
##
class Board:

    # only accept ship size and board size that make sense
    def __init__(self, board_size=DEFAULT_BOARD_SIZE, ship_size=DEFAULT_SHIP_SIZE):
        if board_size > 0 and ship_size > 0 and ship_size <= board_size:
            self.ship_size = ship_size
            self.board_size = board_size
        else:
            self.board_size = DEFAULT_BOARD_SIZE
            self.ship_size = DEFAULT_SHIP_SIZE

        self.cell_states = {'EMPTY'    : 0,
                            'MISS'     : 1,
                            'SHIP_OK'  : 2,
                            'SHIP_HIT' : 3}

        self.grid = [[self.cell_states['EMPTY'] for _ in range(self.board_size)]
                    for _ in range(self.board_size)]

    # Verifies that row/column pair are valid given the board size
    def coordinates_are_valid(self, row, column):
        if row >= 0 and row < self.board_size:
            if column >= 0 and column < self.board_size:
                return True
        return False

    # Updates a cell but only if coordinates and value are valid
    def update_cell(self, row, column, new_value):
        if self.coordinates_are_valid(row, column):
                if new_value in self.cell_states.values():
                    self.grid[row][column] = new_value

    # Return a cell but only if coordinates are valid
    def get_value_of_cell(self, row, column):
        if self.coordinates_are_valid(row, column):
            return self.grid[row][column]

    # Set all cells on the board to 0 (EMPTY)
    def reset_board(self):
        self.grid = [[self.cell_states['EMPTY'] for _ in range(self.board_size)]
                    for _ in range(self.board_size)]

    # Add a ship to the board, but only if proposed placement is valid (calls
    # self.ship_placement_is_valid to check)
    def add_ship(self, coordinates):
        if self.ship_placement_is_valid(coordinates):
            for pair in coordinates:
                if self.coordinates_are_valid(pair[0], pair[1]):
                    self.update_cell(pair[0], pair[1], self.cell_states['SHIP_OK'])

    # checks if a list of ship coordinates is valid, given the board size.
    def ship_placement_is_valid(self, coordinates):
        # first, verify that the number of coordinates is correct and that the type is tuple
        # and then verify that all of the cells are individually valid
        if len(coordinates) == self.ship_size and type(coordinates[0] == 'tuple'):
            for pair in coordinates:
                if not self.coordinates_are_valid(pair[0], pair[1]):
                    return False
        else:
            return False

        # define a helper function to determine if a list of integers can form a sequence
        def list_is_sequential(test_list):
            return sorted(test_list) == list(range(min(test_list), max(test_list)+1))

        # collect row values and column values on their own
        row_values = [pair[0] for pair in coordinates]
        col_values = [pair[1] for pair in coordinates]

        # coordinates are valid iff all the row values form a sequence and all
        # the column values are the same, or vice versa
        if list_is_sequential(row_values) and len(set(col_values)) == 1:
            return True
        elif list_is_sequential(col_values) and len(set(row_values)) == 1:
            return True
        else:
            return False

    # return true if the ship is destroyed, false otherwise
    def ship_destroyed(self):
        number_of_hits = 0
        for row in self.grid:
            number_of_hits += row.count(self.cell_states['SHIP_HIT'])
        return True if number_of_hits >= self.ship_size else False
