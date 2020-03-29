
SELF_BOARD_MAP = {
    0 : '[ ]', # EMPTY
    1 : '[m]', # MISS
    2 : '[@]', # SHIP_OK
    3 : '[*]' # SHIP_HIT
}

OTHER_BOARD_MAP = {
    0 : '[?]', # EMPTY
    1 : '[m]', # MISS
    2 : '[?]', # SHIP_OK
    3 : '[*]' # SHIP_HIT
}

class ConsoleUI:

    # Takes a player number, board size, and ship size, and returns a list
    # of XY tuples corresponding to the user selected placement of a ship.
    # This method does not verify that the coordinates make logical sense for
    # a ship, that is left for the Board class.
    def get_ship_placement(self, player, ship_size):
        coordinates = []
        while len(coordinates) < ship_size:
            print(f"Player {player}, provide next cell coordinate for ship.")
            row = input("row (int): ")
            column = input("column (letter): ")
            column = ord(column.upper())-65 # letter to numeric
            try:
                coordinates.append((int(row)-1, int(column)))
            except:
                print('There was a problem with that, please try again.\n')
        return coordinates

    # Takes a board grid and its size, and shows the board in its entirety, meant
    # to represent the board from that player's perspective.
    # Only board size 8 is currently implemented.
    def show_self_board(self, board_grid, board_size):
        if board_size == 8:
            print("\nYour board")
            # show the top letters
            print('   A   B   C   D   E   F   G   H ')

            # show the grid with numerical index
            for row_index, row in enumerate(board_grid):
                currentRow = str(row_index+1) + ' '
                for cell in row:
                    currentRow += SELF_BOARD_MAP[cell] + ' '
                print(currentRow)
        else:
            print('\nError: No implementation for show_self_board for this board size.')

    # Takes a grid and its size, and shows the board from the perspective
    # of the other player that has incomplete information -- MISS and SHIP_HIT
    # are shown but no distinction between SHIP_OK and EMPTY.
    # Only board size 8 is currently implemented.
    def show_other_board(self, board_grid, board_size):
        if board_size == 8:
            print("\nOther Player's board")
            # show the top letters
            print('   A   B   C   D   E   F   G   H ')

            # show the grid with numerical index
            for row_index, row in enumerate(board_grid):
                currentRow = str(row_index+1) + ' '
                for cell in row:
                    currentRow += OTHER_BOARD_MAP[cell] + ' '
                print(currentRow)
        else:
            print('\nError: No implementation for show_self_board for this board size.')

    # Prompts the player for attack coordinates. Loops until user provides
    # values for row and column that can be converted to integers. Does not verify
    # that the coordinates are valid, that is left to the Board class.
    def get_attack(self, player):
        print(f"Choose your attack coordinates, player {player}.")
        while True:
            row = input("row (int): ")
            column = input("column (letter): ")
            column = ord(column.upper())-65 # letter to numeric
            try:
                return (int(row)-1, int(column))
            except:
                print('Please try again.\n')

    # Displays a simple message to the console stating that it is now a different
    # player's turn.
    def show_turn_message(self, player):
        print(f"It is now Player {player}'s turn.")

    # This method implements the main menu for the game. The player can choose
    # to 'play' or 'quit'.
    def get_menu_selection(self):
        pass

    # Displays a simple message to the console stating that the application is
    # exiting.
    def show_exit_message(self):
        print('Exiting game.')

    # Displays a simple message to the console stating that an attack missed.
    def display_miss_message(self):
        print('Miss.')

    # Displays a simple message to the console stating that an attack hit.
    def display_hit_message(self):
        print('Hit.')

    # Displays a simple message to the console stating that the player has attacked
    # a coordinate that they have previously targetted.
    def display_redundant_attack_message(self):
        print('Miss (again).')

    # Displays a simple message to the console stating that a player has won.
    def declare_winner(self, player):
        print(f"You sunk my battleship, Player {player}.")
