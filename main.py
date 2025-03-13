import ui


def main():
    user_input = "start"
    is_game_over = False
    feedback_to = ""

    ui.clear_screen()

    print(ui.GAME_TITLE)
    print(ui.WELCOME_SCREEN)
    user_name = input("Enter Your Name > ")

    while not is_game_over:
        ui.clear_screen()
        print(ui.GAME_TITLE)
        print(f"{user_name} vs. [opponent]\n")
        print(f"{user_name}'s fleet")
        game_state = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 3, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        ui.display_grid(game_state, len(game_state))
        # TODO: Set up game states instead of this and change game_state to player_state
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
