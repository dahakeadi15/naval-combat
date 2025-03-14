import unittest

import errors
import player


class TestPlayer(unittest.TestCase):
    def test_player_init(self):
        player1 = player.Player("John")
        self.assertEqual(player1.name, "John")

    def test_ship_placement(self):
        player1 = player.Player("John")
        player1.place_ship(0, 0)
        player1.place_ship(player.GRID_SIZE - 1, player.GRID_SIZE - 1)

        self.assertEqual(player1.fleet[0][0], 1)
        self.assertEqual(player1.fleet[player.GRID_SIZE - 1][player.GRID_SIZE - 1], 1)
        self.assertRaises(errors.PlaceNotEmptyError, lambda: player1.place_ship(0, 0))

    def test_ship_hit(self):
        player1 = player.Player("John")
        was_successful_hit = player1.take_hit(0, 0)

        self.assertEqual(was_successful_hit, False)

        player1.place_ship(0, 0)
        was_successful_hit = player1.take_hit(0, 0)

        self.assertEqual(player1.fleet[0][0], 2)
        self.assertEqual(was_successful_hit, True)

    def test_ai_player_init(self):
        ai = player.AiPlayer()

        self.assertEqual(ai.name, "computer")

        total_ships = sum([sum(row) for row in ai.fleet])
        self.assertEqual(total_ships, player.N_SHIPS)


if __name__ == "__main__":
    unittest.main()
