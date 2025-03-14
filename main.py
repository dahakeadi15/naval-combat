import player
import ui


def main():
    user_input = "start"
    is_game_over = False
    feedback_to = ""

    ui.clear_screen()

    print(ui.GAME_TITLE)
    print(ui.WELCOME_SCREEN)
    user_name = input("Enter Your Name >")

    player1 = player.Player(user_name)
    player2 = player.AiPlayer()

    ui.display_grid(player2.fleet, len(player2.fleet))

    while not is_game_over:
        ui.clear_screen()

        print(ui.GAME_TITLE)
        print(f"{player1.name} vs. {player2.name}\n")
        print(f"{player1.name}'s fleet")

        ui.display_grid(player1.fleet, player.GRID_SIZE)

        print(f"\n{player2.name}'s fleet")
        ui.display_grid(player2.fleet, player.GRID_SIZE)

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
