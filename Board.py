
DEFAULT_BOARD_SIZE = 8
DEFAULT_SHIP_SIZE = 3

class Board:

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

        self.ship_coordinates = None

    def coordinates_are_valid(self, row, column):
        if row >= 0 and row < self.board_size:
            if column >= 0 and column < self.board_size:
                return True
        return False

    def update_cell(self, row, column, new_value):
        if self.coordinates_are_valid(row, column):
                if new_value in self.cell_states.values():
                    self.grid[row][column] = new_value

    def get_value_of_cell(self, row, column):
        if self.coordinates_are_valid(row, column):
            return self.grid[row][column]

    def reset_board(self):
        self.grid = [[self.cell_states['EMPTY'] for _ in range(self.board_size)]
                    for _ in range(self.board_size)]

    def add_ship(self, coordinates):
        if len(coordinates) == self.ship_size and type(coordinates[0] == 'tuple'):
            for pair in coordinates:
                if self.coordinates_are_valid(pair[0], pair[1]):
                    self.update_cell(pair[0], pair[1], self.cell_states['SHIP_OK'])

    def ship_destroyed(self):
        number_of_hits = 0
        for row in self.grid:
            number_of_hits += row.count(self.cell_states['SHIP_HIT'])
        return True if number_of_hits >= self.ship_size else False
