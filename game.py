import random
import checker


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def play_game(player_figure, computer_figure):
    display_board()

    while True:
        player_move(player_figure)

        checker.check()
        if checker.check() == 1:
            print(f"{player_figure} wins.")
            break
        else:
            checker.check()
            if checker.tie() == 0:
                print("Tie.")
                break

        computer_move(computer_figure)

        checker.check()
        if checker.check() == 1:
            print(f"{computer_figure} wins.")
            break


def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


def player_move(player_figure):
    i = 0
    while i == 0:
        try:
            player_position = int(input("Podaj pole: "))
            if board[player_position - 1] == "-":
                board[player_position - 1] = player_figure
                i = 1
                display_board()
                return player_position
            else:
                i = 0
                print("pole zajęte")
                display_board()
        except ValueError:
            i = 0


def computer_move(computer_figure):
    i = 0
    while i == 0:
        computer_position = random.randint(1, 9)
        if board[computer_position - 1] == "-":
            board[computer_position - 1] = computer_figure
            i = 1
            display_board()
        else:
            i = 0



