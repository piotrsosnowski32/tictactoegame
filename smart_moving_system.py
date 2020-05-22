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
    if status == 0:
        status = line(player_figure)
        if status == 0:
            status = diagonal_1(player_figure)
            if status == 0:
                status = diagonal_2(player_figure)
                if status == 0:
                    status = random.randint(1, 9)

    return status


def column(player_figure):
    counter = 0
    i = 0
    move = 0
    for line_cell in range(2):
        for column_cell in range(2):
            if game.board[i] == player_figure:
                counter += 1
            else:
                move = i + 1
            i += 3
            if counter == 2:
                return move
        counter = 0
        i -= 5


def line(player_figure):
    counter = 0
    i = 0
    move = 0
    for column_cell in range(2):
        for line_cell in range(2):
            if game.board[i] == player_figure:
                counter += 1
            else:
                move = i + 1
            i += 1
            if counter == 2:
                return move
        counter = 0
        i += 1


def diagonal_1(player_figure):
    counter = 0
    i = 0
    move = 0
    for cell in range(2):
        if game.board[i] == player_figure:
            counter += 1
        else:
            move = i + 1
        i += 4

        if counter == 2:
            return move


def diagonal_2(player_figure):
    counter = 0
    i = 2
    move = 0
    for cell in range(2):
        if game.board[i] == player_figure:
            counter += 1
        else:
            move = i + 1
        i += 2

        if counter == 2:
            return move





