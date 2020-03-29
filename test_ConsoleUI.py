import unittest
import mock

import ConsoleUI

class ConsoleUITest(unittest.TestCase):

    def test_get_attack(self):

        ui = ConsoleUI.ConsoleUI()

        # mock input values as "1"
        with mock.patch('builtins.input', return_value="1"):
            # should return (0,-16) tuple
            self.assertEqual(ui.get_attack(player=1), (0, -16))


    def test_get_ship_placement(self):

        ui = ConsoleUI.ConsoleUI()

        # mock input values as "1"
        with mock.patch('builtins.input', return_value="1"):
            self.assertEqual(ui.get_ship_placement(1, 3), [(0, -16), (0, -16), (0, -16)])
