

class ConsoleUI:

    # Takes a player number, board size, and ship size, and returns a list
    # of XY tuples corresponding to the user selected placement of a ship.
    # This method does not verify that the coordinates make logical sense for
    # a ship, that is left for the Board class. This method does ensure the
    # coordinates fall on to the grid, though.
    def get_ship_placement(self, player, board_size, ship_size):
        pass

    # Takes a grid and its size, and shows the board in its entirety, meant
    # to represent the board from that player's perspective.
    def show_self_board(self, board_grid, board_size):
        pass

    # Takes a grid and its size, and shows the board from the perspective
    # of the other player that has incomplete information -- MISS and SHIP_HIT
    # are shown but no distinction between SHIP_OK and EMPTY.
    def show_other_board(self, board_grid, board_size):
        pass

    # Prompts the player for attack coordinates. Loops until user provides
    # values for row and column that can be converted to integers. Does not verify
    # that the coordinates are valid, that is left to the Board class.
    def get_attack(self, player):
        while True:
            row = input("row: ")
            column = input("column: ")
            try:
                return (int(row), int(column))
            except:
                print('Please try again.\n')

    # Displays a simple message to the console stating that it is now a different
    # player's turn.
    def show_turn_message(self, player):
        print(f"It is now Player {player}'s turn.'")

    # This method implements the main menu for the game. The player can choose
    # to 'play' or 'quit'.
    def get_menu_selection(self):
        pass

    # Displays a simple message to the console stating that the application is
    # exiting.
    def show_exit_message(self):
        pass

    # Displays a simple message to the console stating that an attack missed.
    def display_miss_message(self):
        pass

    # Displays a simple message to the console stating that an attack hit.
    def display_hit_message(self):
        pass

    # Displays a simple message to the console stating that the player has attacked
    # a coordinate that they have previously targetted.
    def display_redundant_attack_message(self):
        pass

    # Displays a simple message to the console stating that a player has won.
    def declare_winner(self, player):
        pass
