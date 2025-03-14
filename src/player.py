import random

import colorize
import errors

GRID_SIZE = 9  # FUTURE: give user option to choose between [5, 9]
N_SHIPS = 6 if GRID_SIZE >= 7 else 4
MAX_MISSILES = N_SHIPS * 2


class Player:
    def __init__(self, name):
        self.name = name
        self.fleet = [[0 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
        self.n_ships_operational = 0
        self.n_ships_wreaked = 0
        self.moves = []
        self.remaining_shots = MAX_MISSILES

    def place_ship(self, row: int, col: int):
        # check if ship exists
        if self.fleet[row][col]:
            raise errors.PlaceNotEmptyError()

        self.fleet[row][col] = 1

    def take_hit(self, row: int, col: int) -> bool:
        if self.fleet[row][col] == 1:
            self.fleet[row][col] = 2
            return True
        return False

    def reset_fleet(self):
        self.fleet = [[0 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]


class AiPlayer(Player):
    def __init__(self):
        super().__init__("computer")
        self.place_ships()

    def random_coordinates(self):
        return random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)

    def place_ships(self):
        count = 0
        while count < N_SHIPS:
            row, col = self.random_coordinates()
            # print(f"AI Placing ship at {row}, {col} : {count}, {N_SHIPS}")
            try:
                self.place_ship(row, col)
                count += 1
            except errors.PlaceNotEmptyError:
                # print(f"Not Empty {row}, {col}")
                continue
            except Exception as e:
                print(
                    colorize.color_text(
                        f"(While AI was Placing ship at ({row}, {col}))\nERROR : {e}",
                        colorize.TextColor.RED,
                    )
                )
