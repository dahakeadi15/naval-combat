import os

GAME_TITLE = """
 __ _ ____ _  _ ____ _      ____ ____ _  _ ___  ____ ___
 | \| |--|  \/  |--| |___   |___ [__] |\/| |==] |--|  | 

"""


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
            if game_state[i][j] == 0:
                # SEA
                object = "  ~  "
            elif game_state[i][j] == 1:
                # SHIP
                object = " <=> "
            elif game_state[i][j] == 2:
                # WRECKAGE / HIT
                object = " <*> "
            else:
                # MISS
                object = "  x  "
            print(f"{object}", end="")
        print("|")

    print((grid_size * 5 + 7) * "-")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
