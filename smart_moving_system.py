import random
import game


def smart_move(player_figure):
    counter = 0
    for field in game.board:
        if field != "-":
            counter += 1

    if counter == 1:
        move = first_move(player_figure)
    else:
        move = other_moves(player_figure)

    return move


def first_move(player_figure):
    if game.board[4] == player_figure:
        move = random.randint(1, 9)
    else:
        move = 5

    return move


def other_moves(player_figure):
    status = column(player_figure)
    if status == None:
        status = line(player_figure)
        if status == None:
            status = diagonal_1(player_figure)
            if status == None:
                status = diagonal_2(player_figure)
                if status == None:
                    status = random.randint(1, 9)

    return status


def column(player_figure):
    i = 0
    counter = 0
    move = None
    for line_cell in range(3):
        for column_cell in range(3):

            if game.board[i] == player_figure:
                counter += 1

            if game.board[i] == "-":
                move = i + 1

            if i < 6:
                i += 3

            if counter == 2:
                return move

        counter = 0
        i -= 5


def line(player_figure):
    counter = 0
    i = 0
    move = None
    for column_cell in range(3):
        for line_cell in range(3):
            if game.board[i] == player_figure:
                counter += 1

            if game.board[i] == "-":
                move = i + 1

            if counter == 2:
                return move

            i += 1

        counter = 0


def diagonal_1(player_figure):
    counter = 0
    i = 0
    move = None
    for cell in range(3):

        if game.board[i] == player_figure:
            counter += 1

        if game.board[i] == "-":
            move = i + 1

        if i < 7:
            i += 4

    if counter == 2:
        return move


def diagonal_2(player_figure):
    counter = 0
    i = 2
    move = None
    for cell in range(3):

        if game.board[i] == player_figure:
            counter += 1

        if game.board[i] == "-":
            move = i + 1

        if i < 7:
            i += 2

    if counter == 2:
        return move

# wypierdala sie przy checku dla komputera i przy wyborze pola za pomocą SMS



