
import Board
import time

class Game:

    def __init__(self, ui_manager, board_size=Board.DEFAULT_BOARD_SIZE,
                    ship_size=Board.DEFAULT_SHIP_SIZE):
        self.ui = ui_manager
        self.boards = {
                1 : Board.Board(board_size=board_size, ship_size=ship_size),
                2 : Board.Board(board_size=board_size, ship_size=ship_size)
        }
        self.board_size = board_size
        self.ship_size = ship_size
        self.winner = None

    def get_ship_placement(self, player):
        while True:
            board_size = boards[player].board_size
            ship_size = boards[player].ship_size
            coordinates = self.ui.get_ship_placement(player=player,
                                board_size=board_size, ship_size=ship_size)
            if (boards[player].ship_placement_is_valid(coordinates)):
                return coordinates

    def take_turn(self, player_current, player_other):
        self.ui.display_turn_message(player=player_current)
        self.ui.display_self_board(self.boards[player_current].grid, self.board_size)
        self.ui.display_other_board(self.boards[player_other].grid, self.board_size)

        # get attack command
        while True:
            cell = self.ui.get_attack(player=player_current)
            if self.boards[player_other].coordinates_are_valid(cell[0], cell[1]):
                break

        # execute command
        if self.boards[player_other].get_value_of_cell(cell[0], cell[1]) == self.boards[player_other].cell_states['EMPTY']:
            self.boards[player_other].update_cell(cell[0], cell[1], self.boards[player_other].cell_states['MISS'])
            self.ui.display_miss_message()
        elif self.boards[player_other].get_value_of_cell(cell[0], cell[1]) == self.boards[player_other].cell_states['SHIP_OK']:
            self.boards[player_other].update_cell(cell[0], cell[1], self.boards[player_other].cell_states['SHIP_HIT'])
            self.ui.display_hit_message()
        else:
            self.ui.display_redundant_attack_message()

        # if ship destroyed, flag end game and identify winner
        if self.boards[player_other].ship_destroyed():
            self.game_over = True
            self.winner = player_current


    def start_game(self):

        self.ui.display_start_message()

        self.game_over = False
        self.boards[1].reset_board()
        self.boards[2].reset_board()

        # handle ship placement
        for player in [1, 2]:
            valid_placement = False
            while not valid_placement:
                self.ui.display_self_board(self.boards[player].grid, self.board_size)
                coordinates = self.ui.get_ship_placement(player=player, ship_size=self.ship_size)
                valid_placement = self.boards[player].ship_placement_is_valid(coordinates)
                if not valid_placement:
                    print("Invalid coordinates, please try again.")
                    time.sleep(2)

            self.boards[player].add_ship(coordinates)
            self.ui.display_self_board(self.boards[player].grid, self.board_size)
            self.ui.clear_screen()

        # loop trough turns until a ship is destroyed
        while True:
            self.take_turn(1, 2)
            if self.game_over:
                self.ui.declare_winner(player=self.winner)
                break
            self.take_turn(2, 1)
            if self.game_over:
                self.ui.declare_winner(player=self.winner)
                break

        self.ui.display_exit_message()
