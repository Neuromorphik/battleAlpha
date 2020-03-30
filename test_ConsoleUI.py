import unittest
import mock

import ConsoleUI

##
# ConsoleUITest inherits from unittest's TestCase class.
# ConsoleUI tests the methods in the ConsoleUI class.
# Many of these methods are display methods; to test these methods, the
# parameter 'testing' is set to True which causes these display methods to
# return the display message instead of printing it to console and pausing.
# The first two test cases are tested with mocking, the methods use Python's
# input() method so the mocking works by just passing in "1" wherever input()
# is called.
#
##
class ConsoleUITest(unittest.TestCase):

    def test_get_attack(self):

        ui = ConsoleUI.ConsoleUI()

        # mock input values as "1"
        with mock.patch('builtins.input', return_value="1"):
            # should return (0,-16) tuple
            # (0, -16) is of course an invalid coordinate but can only pass in one
            # value for both input() calls while mocking, and the second call expects
            # a letter. In short, (0,-16) shows its working as expected.
            self.assertEqual(ui.get_attack(player=1, testing=True), (0, -16))

    def test_get_ship_placement(self):

        ui = ConsoleUI.ConsoleUI()

        # mock input values as "1"
        # (0, -16) is of course an invalid coordinate but can only pass in one
        # value for both input() calls while mocking, and the second call in each
        # loop expects a letter. In short, (0,-16) shows its working as expected.
        with mock.patch('builtins.input', return_value="1"):
            self.assertEqual(ui.get_ship_placement(1, 3, testing=True), [(0, -16), (0, -16), (0, -16)])

    def test_messages(self):

        ui = ConsoleUI.ConsoleUI()

        # display_turn_message - test for player=1 and player=2
        self.assertEqual(ui.display_turn_message(player=1, testing=True), "It is now Player 1's turn.")
        self.assertEqual(ui.display_turn_message(player=2, testing=True), "It is now Player 2's turn.")

        # display_start_message
        self.assertEqual(ui.display_start_message(testing=True), 'Starting Game. Players need to place ships.')

        # display_exit_message
        self.assertEqual(ui.display_exit_message(testing=True), 'Exiting game.')

        # display_miss_message
        self.assertEqual(ui.display_miss_message(testing=True), '\nMiss.')

        # display_hit_message
        self.assertEqual(ui.display_hit_message(testing=True), '\nHit.')

        # display_redundant_attack_message
        self.assertEqual(ui.display_redundant_attack_message(testing=True), '\nMiss.')

        # declare_winner - test for player=1 and player=2
        self.assertEqual(ui.declare_winner(player=1, testing=True), "You sunk my battleship, Player 1.")
        self.assertEqual(ui.declare_winner(player=2, testing=True), "You sunk my battleship, Player 2.")
