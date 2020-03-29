
import Board

class Game:

    def __init__(self, ui_manager, input_manager, board_size=Board.DEFAULT_BOARD_SIZE,
                    ship_ship=Board.DEFAULT_SHIP_SIZE):
        self.ui = ui_manager
        self.input = input_manager
        self.board_player_1 = Board.Board(board_size)
        self.board_player_2 = Board.Board(board_size)

    def start_game(self):
        self.turn = 1
        self.board_player_1.reset_board()
        self.board_player_2.reset_board()

        while True:
            # clear console

            if (self.turn == 1):
                # show p1 their interface
                self.ui.show_self_board(self.board_player_1)
                self.ui.show_other_board(self.board_player_2)

                # get p1 attack command
                while True:
                    coordinate = self.input.get_attack()
                    if self.board_player_2.coordinates_are_valid(coordinate[0], coordinate[1]):
                        break

                # execute command
                self.board_player_2.update_cell(coordinate[0], coordinate[1])

                # show p1 the result
                self.ui.show_other_board(self.board_player_2)

                # end game if p2 ship destroyed
                if self.board_player_2.ship_destroyed():
                    return

                # set turn to p2
                self.turn = 2

            else:
                # show p2 their interface
                self.ui.show_self_board(self.board_player_2)
                self.ui.show_other_board(self.board_player_1)

                # get p2 attack command
                while True:
                    coordinate = self.input.get_attack()
                    if self.board_player_2.coordinates_are_valid(coordinate[0], coordinate[1]):
                        break

                # execute command
                self.board_player_1.update_cell(coordinate[0], coordinate[1])

                # show p2 the result
                self.ui.show_other_board(self.board_player_1)

                # end game if p1 ship destroyed
                if self.board_player_1.ship_destroyed():
                    return

                # set turn to p1
                self.turn = 1
