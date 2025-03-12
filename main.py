import ui


def main():
    user_input = "start"
    is_game_over = False
    while not is_game_over:
        ui.clear_screen()
        print(ui.GAME_TITLE)
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
        user_input = input("End game? (y/n)\n>>> ")
        if user_input == "y":
            is_game_over = True


if __name__ == "__main__":
    main()
