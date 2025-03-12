import os

from colorize import TextColor, color_text

GAME_TITLE = """
 __ _ ____ _  _ ____ _      ____ ____ _  _ ___  ____ ___
 | \| |--|  \/  |--| |___   |___ [__] |\/| |==] |--|  | 

"""

# GAME OBJECTS
SEA = color_text("  ~  ", TextColor.BRIGHT_BLUE)
SHIP = color_text(" <=> ", TextColor.BRIGHT_GREEN)
WRECKAGE = color_text(" <x> ", TextColor.BRIGHT_RED)


# GAME GRID
def display_grid(game_state: list[list[int]], grid_size):
    c = 65

    # TODO: Fix grid for double digit grid size

    print(color_text("     |", TextColor.GRAY), end="")
    for i in range(grid_size):
        print(color_text(f"  {i+1}  ", TextColor.GRAY), end="")
    print(color_text("|", TextColor.GRAY))
    print(color_text((grid_size * 5 + 7) * "-", TextColor.GRAY))

    for i in range(grid_size):
        print(color_text(f"  {chr(c+i)}  |", TextColor.GRAY), end="")
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
        print(color_text("|", TextColor.GRAY))

    print(color_text((grid_size * 5 + 7) * "-", TextColor.GRAY))


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
