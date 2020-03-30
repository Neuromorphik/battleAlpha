
import time

# symbols that the player will see, looking at their own board
SELF_BOARD_SYMBOLS = {
    0 : '[ ]', # EMPTY
    1 : '[X]', # MISS
    2 : '[@]', # SHIP_OK
    3 : '[O]' # SHIP_HIT
}

# symbols that the player will see, looking at their view of opponent's board
OTHER_BOARD_SYMBOLS = {
    0 : '[?]', # EMPTY
    1 : '[X]', # MISS
    2 : '[?]', # SHIP_OK
    3 : '[O]' # SHIP_HIT
}

###
# ConsoleUI implements the methods expected of a UI manager for the Game.py class.
# ConsolueUI implements these methods with simple console I/O.
# Many of the display methods behave differently if testing param is set to True
# in order to simplify testing.
###
class ConsoleUI:

    # Takes a player number, board size, and ship size, and returns a list
    # of XY tuples corresponding to the user selected placement of a ship.
    # This method does not verify that the coordinates make logical sense for
    # a ship, that is left for the Board class.
    def get_ship_placement(self, player, ship_size, testing=False):
        coordinates = []
        while len(coordinates) < ship_size:
            if not testing: print(f"\nPlayer {player}, provide next cell coordinate for ship placement.")
            row = input("row (int): ")
            column = input("column (letter): ")
            try:
                column = ord(column.upper())-65 # letter to numeric
            except:
                print('There was a problem with that, please try again.\n')
                continue
            try:
                coordinates.append((int(row)-1, int(column)))
            except:
                print('There was a problem with that, please try again.\n')
        return coordinates

    # Takes a board grid and its size, and displays the board in its entirety, meant
    # to represent the board from that player's perspective.
    # Only board size 8 is currently implemented.
    def display_self_board(self, board_grid, board_size):
        if board_size == 8:
            print("\nYour board")
            # display the top letters
            print('   A   B   C   D   E   F   G   H ')
            # display the grid with numerical index
            for row_index, row in enumerate(board_grid):
                currentRow = str(row_index+1) + ' '
                for cell in row:
                    currentRow += SELF_BOARD_SYMBOLS[cell] + ' '
                print(currentRow)
        else:
            print('\nError: No implementation for display_self_board for board size {board_size}.')
        time.sleep(1)

    # Takes a grid and its size, and displays the board from the perspective
    # of the other player that has incomplete information -- MISS and SHIP_HIT
    # are displayn but no distinction between SHIP_OK and EMPTY.
    # Only board size 8 is currently implemented.
    def display_other_board(self, board_grid, board_size):
        if board_size == 8:
            print("\nOther Player's board")
            # display the top letters
            print('   A   B   C   D   E   F   G   H ')
            # display the grid with numerical index
            for row_index, row in enumerate(board_grid):
                currentRow = str(row_index+1) + ' '
                for cell in row:
                    currentRow += OTHER_BOARD_SYMBOLS[cell] + ' '
                print(currentRow)
        else:
            print('\nError: No implementation for display_self_board for this board size.')
        time.sleep(1)

    # Prompts the player for attack coordinates. Loops until user provides
    # values for row and column that can be converted to integers. Does not verify
    # that the coordinates are valid, that is left to the Board class.
    def get_attack(self, player, testing=False):
        if not testing: print(f"\nChoose your attack coordinates, player {player}.")
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
    def display_turn_message(self, player, testing=False):
        message = f"It is now Player {player}'s turn."
        if not testing:
            self.clear_screen()
            print(message)
            time.sleep(2)
        if testing: return message

    def display_start_message(self, testing=False):
        message = 'Starting Game. Players need to place ships.'
        if not testing:
            self.clear_screen()
            print(message)
            time.sleep(2)
        if testing: return message

    # Displays a simple message to the console stating that the application is
    # exiting.
    def display_exit_message(self, testing=False):
        message = 'Exiting game.'
        if not testing:
            print(message)
            time.sleep(2)
        if testing: return message

    # Displays a simple message to the console stating that an attack missed.
    def display_miss_message(self, testing=False):
        message = '\nMiss.'
        if not testing:
            print(message)
            time.sleep(2)
        if testing: return message

    # Displays a simple message to the console stating that an attack hit.
    def display_hit_message(self, testing=False):
        message = '\nHit.'
        if not testing:
            print(message)
            time.sleep(2)
        if testing: return message

    # Displays a simple message to the console stating that the player has attacked
    # a coordinate that they have previously targetted.
    def display_redundant_attack_message(self, testing=False):
        message = '\nMiss.'
        if not testing:
            print(message)
            time.sleep(2)
        if testing: return message

    # Displays a simple message to the console stating that a player has won.
    def declare_winner(self, player, testing=False):
        message = f"You sunk my battleship, Player {player}."
        if not testing:
            print(message)
            time.sleep(2)
        if testing: return message

    # outputs 50 blank lines to "clear" the view on the console.
    def clear_screen(self):
        print('\n' * 50)
