import os

GAME_TITLE = """
 __ _ ____ _  _ ____ _      ____ ____ _  _ ___  ____ ___
 | \| |--|  \/  |--| |___   |___ [__] |\/| |==] |--|  | 

"""

# GAME OBJECTS
SEA = "  ~  "
SHIP = " <=> "
WRECKAGE = " <x> "


def display_grid(game_state: list[list[int]], grid_size):
    c = 65

    # TODO: Fix grid for double digit grid size

    print("     |", end="")
    for i in range(grid_size):
        print(f"  {i+1}  ", end="")
    print("|")
    print((grid_size * 5 + 7) * "-")

    for i in range(grid_size):
        print(f"  {chr(c+i)}  |", end="")
        for j in range(grid_size):
            match game_state[i][j]:
                case 0:
                    print(SEA, end="")
                case 1:
                    print(SHIP, end="")
                case 2:
                    print(WRECKAGE, end="")
                case _:
                    print("  .  ", end="")
        print("|")

    print((grid_size * 5 + 7) * "-")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
