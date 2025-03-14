import player
import ui
from colorize import TextColor, color_text


def main():
    user_input = "start"
    is_game_over = False
    feedback_to = ""

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

    while not is_game_over:
        ui.clear_screen()

        print(ui.GAME_TITLE)
        print(f"{player1.name} vs. {player2.name}\n")
        print(f"{player1.name}'s fleet")

        ui.display_grid(player1.fleet)

        print(f"\n{player2.name}'s fleet")
        ui.display_grid(player2.fleet)

        print(feedback_to)
        feedback_to = ""

        print(ui.GAME_OPTIONS)

        user_input = input(">>> ")
        match user_input.lower():
            case "n":
                feedback_to = ui.OF_NEW_GAME
            case "e":
                is_game_over = True
            case _:
                feedback_to = ui.OF_INVALID_OPTION


if __name__ == "__main__":
    main()
