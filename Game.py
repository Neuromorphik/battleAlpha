
import Board

class Game:

    def __init__(self, ui_manager, board_size=Board.DEFAULT_BOARD_SIZE,
                    ship_ship=Board.DEFAULT_SHIP_SIZE):
        self.ui = ui_manager
        self.boards = {
                1 : Board.Board(board_size=board_size, ship_size=ship_size),
                2 : Board.Board(board_size=board_size, ship_size=ship_size)
        }
        self.winner = None

    def show_menu(self):
        choice = self.ui.get_menu_selection()
        if choice == 'quit':
            self.ui.show_exit_message()
        elif choice == 'play':
            self.start_game()
        else:
            pass

    def get_ship_placement(self, player):
        while True:
            board_size = boards[player].board_size
            ship_size = boards[player].ship_size
            coordinates = self.ui.get_ship_placement(player=player,
                                board_size=board_size, ship_size=ship_size)
            if (ship_placement_is_valid(coordinates)):
                return coordinates

    def take_turn(self, player_current, player_other):
        self.ui.show_turn_message(turn=player_current)
        self.ui.show_self_board(self.boards[player_current])
        self.ui.show_other_board(self.boards[player_other])

        # get attack command
        while True:
            coordinate = self.input.get_attack(player=player_current)
            if boards[player_other].coordinates_are_valid(coordinate[0], coordinate[1]):
                break

        # execute command
        if self.boards[player_other].get_value_of_cell(coordinate) == self.boards[player_other].cell_states['EMPTY']:
            self.boards[player_other].update_cell(coordinate[0], coordinate[1], self.boards[player_other].cell_states['MISS'])
            self.ui.display_miss_message()
        elif self.boards[player_other].get_value_of_cell(coordinate) == self.boards[player_other].cell_states['SHIP_OK']:
            self.boards[player_other].update_cell(coordinate[0], coordinate[1], self.boards[player_other].cell_states['SHIP_HIT'])
            self.ui.display_hit_message()
        else:
            self.ui.display_already_hit_message()

        # show the result
        self.ui.show_other_board(self.boards[player_other])

        # flag end game and identify winner if ship destroyed
        if self.boards[player_other].ship_destroyed():
            self.game_over = True
            self.winner = player_current


    def start_game(self):
        self.game_over = False
        self.boards[1].reset_board()
        self.boards[2].reset_board()

        self.boards[1].add_ship(get_ship_placement(player=1))
        self.boards[2].add_ship(get_ship_placement(player=2))

        self.ui.show_start_message()

        while True:
            self.take_turn(1, 2)
            if self.game_over:
                self.ui.declare_winner(player=self.winner)
                break
            self.take_turn(2, 1)
            if self.game_over:
                self.ui.declare_winner(player=self.winner)
                break

        self.show_menu()
