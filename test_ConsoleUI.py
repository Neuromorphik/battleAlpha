import unittest
import mock

import ConsoleUI

class ConsoleUITest(unittest.TestCase):

    def test_get_attack(self):

        ui = ConsoleUI.ConsoleUI()

        # mock input values as "0"
        with mock.patch('builtins.input', return_value="0"):
            # should return (0,0) tuple
            self.assertEqual(ui.get_attack(player=1), (0, 0))
