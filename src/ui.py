import os

from colorize import TextColor, color_text
from player import GRID_SIZE

GAME_TITLE = """
__ _ ____ _  _ ____ _      ____ ____ _  _ ___  ____ ___
| \| |--|  \/  |--| |___   |___ [__] |\/| |==] |--|  | 
"""

WELCOME_SCREEN = f"""
WELCOME!!!
"""

# GAME OBJECTS
SEA = color_text("  ~  ", TextColor.BRIGHT_BLUE)
SHIP = color_text(" <=> ", TextColor.BRIGHT_GREEN)
WRECKAGE = color_text(" <x> ", TextColor.BRIGHT_RED)


# GAME GRID
def display_grid(game_state: list[list[int]], history: list[tuple]):
    c = 65

    print(color_text("     |", TextColor.GRAY), end="")
    for i in range(GRID_SIZE):
        print(color_text(f"  {i+1}  ", TextColor.GRAY), end="")
    print(color_text("|", TextColor.GRAY))
    print(color_text((GRID_SIZE * 5 + 7) * "-", TextColor.GRAY))

    for i in range(GRID_SIZE):
        print(color_text(f"  {chr(c+i)}  |", TextColor.GRAY), end="")
        for j in range(GRID_SIZE):
            match game_state[i][j]:
                case 0:
                    print(SEA, end="")
                case 1:
                    print(SHIP, end="")
                case 2:
                    print(WRECKAGE, end="")
                case _:
                    print("  .  ", end="")
        print(color_text("|", TextColor.GRAY), end="")

        if len(history) > i:
            last_move_idx = -1 * (i + 1)
            move, is_direct_hit = history[last_move_idx]
            print(
                color_text(
                    f" {move}", TextColor.GREEN if is_direct_hit else TextColor.RED
                ),
                end="",
            )
            if i == 0:
                print(" < last", end="")
        print("")

    print(color_text((GRID_SIZE * 5 + 7) * "-", TextColor.GRAY))


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
