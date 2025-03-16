import time

import player
import ui
from colorize import TextColor, color_text


def main():
    is_game_over = False

    ui.clear_screen()

    # START
    print(ui.GAME_TITLE)
    print(ui.WELCOME_SCREEN)
    user_name = input("Enter Your Name > ")

    player1 = player.Player(user_name)
    player2 = player.AiPlayer()

    # PLACE SHIPS
    count = 0
    error = ""
    while count <= player.N_SHIPS:
        ui.clear_screen()

        print(ui.GAME_TITLE)
        print(f"{player1.name}'s fleet")
        ui.display_grid(player1.fleet)
        print("Available Ships: ", ui.SHIP * (player.N_SHIPS - count))

        # Confirm deployment
        if count == player.N_SHIPS:
            print("Are you satisfied with your battle plan?")
            print("Yes, Let's go!! -> (y) \nNo, reset positions. -> (n)")
            is_valid = False
            while not is_valid:
                confirmation = input(">>> ")
                if confirmation.lower() == "y":
                    is_valid = True
                    break
                elif confirmation.lower() == "n":
                    is_valid = True
                    count = 0
                    player1.reset_fleet()
                else:
                    print(color_text("Please enter 'y' or 'n'", TextColor.RED))
            if is_valid:
                count += 1
                continue

        if error:
            print(color_text(error, TextColor.RED))
            error = ""
        print("Enter coordinate to deploy ship at (ex. A1)")
        print("[reset (r) | exit (e)]")
        coordinate = input(">>> ")

        # Reset fleet
        if coordinate.lower() == "r":
            if count == 0:
                continue
            count = 0
            player1.reset_fleet()
            continue

        # TODO: Add undo (u) option

        # Exit game
        if coordinate.lower() == "e":
            ui.clear_screen()
            return

        # coordinate validation
        if (
            len(coordinate) != 2
            or not coordinate[0].isalpha()
            or not coordinate[1].isnumeric()
        ):
            error = "Please enter valid coordinates"
            continue

        # extract coordinates
        row, col = ord(coordinate[0].upper()) - ord("A"), int(coordinate[1]) - 1

        # validate is within range
        if not (0 <= row < player.GRID_SIZE and 0 <= col < player.GRID_SIZE):
            error = "Please enter valid coordinates"
            continue

        # Try placing ship
        try:
            player1.place_ship(row, col)
            count += 1
        except:
            error = f"A ship is already deployed at {coordinate.upper()}"

    # START GAME
    feedback = ""
    turn = 0
    while not is_game_over:
        ui.clear_screen()

        print(ui.GAME_TITLE)
        print(f"{player1.name} vs. {player2.name}\n")
        print(f"{player1.name}'s fleet")

        ui.display_grid(player1.fleet)

        print(f"\n{player2.name}'s fleet")
        ui.display_grid(player2.fleet)

        print(feedback)
        feedback = ""

        if turn % 2 == 0:
            print(f"{player1.remaining_shots} missiles left.")
            print("Enter target coordinates (ex. A1)")
            print("[exit (e)]")
            coordinate = input(">>> ")

            # Exit game
            if coordinate.lower() == "e":
                print(color_text("Exiting...", TextColor.GRAY))
                is_game_over = True
                return

            # coordinate validation
            if (
                len(coordinate) != 2
                or not coordinate[0].isalpha()
                or not coordinate[1].isnumeric()
            ):
                feedback = color_text("Please enter valid coordinates", TextColor.RED)
                continue

            # extract coordinates
            row, col = ord(coordinate[0].upper()) - ord("A"), int(coordinate[1]) - 1

            # validate is within range
            if not (0 <= row < player.GRID_SIZE and 0 <= col < player.GRID_SIZE):
                feedback = color_text("Please enter valid coordinates", TextColor.RED)
                continue

            was_successful = player1.shoot(player2, row, col)
            turn += 1
            time.sleep(1)
            if was_successful:
                print(color_text("Direct Hit!!!", TextColor.GREEN))
            else:
                print(color_text("Missed!", TextColor.RED))
            time.sleep(2)

        # Player 2 Attempt hit
        else:
            print(f"{player2.name}'s chance.")
            target_row, target_col = player2.random_coordinates()
            time.sleep(1)
            was_successful = player2.shoot(player1, target_row, target_col)
            turn += 1
            if was_successful:
                print(color_text(f"Direct Hit!!!", TextColor.RED))
            else:
                print(color_text(f"Missed!", TextColor.GREEN))
            time.sleep(2)
        if (
            player2.remaining_shots == 0
            or player1.n_ships_operational == 0
            or player2.n_ships_operational == 0
        ):
            is_game_over = True

    if is_game_over:
        ui.clear_screen()

        print(ui.GAME_TITLE)
        print(f"{player1.name} vs. {player2.name}\n")

        print(color_text("Game Over!\n", TextColor.GRAY))

        winner = ""

        if player1.n_ships_operational > player2.n_ships_operational:
            winner = player1.name
        elif player1.n_ships_operational < player2.n_ships_operational:
            winner = player2.name

        print(
            f"{player1.name}'s fleet"
            + (
                color_text(" WINNER!!!", TextColor.GREEN)
                if winner == player1.name
                else color_text(" LOST !", TextColor.RED)
            )
        )

        ui.display_grid(player1.fleet)

        print(
            f"\n{player2.name}'s fleet"
            + (
                color_text(" WINNER!!!", TextColor.GREEN)
                if winner == player2.name
                else color_text(" LOST !", TextColor.RED)
            )
        )
        ui.display_grid(player2.fleet)

        if winner:
            print(color_text(f"\n{winner} won !!!", TextColor.BRIGHT_CYAN))
        else:
            print("It was a draw!")

        print("")
        print(color_text("Exiting...", TextColor.GRAY))


if __name__ == "__main__":
    main()
