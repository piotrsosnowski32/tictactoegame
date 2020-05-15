import game


def check():

    line()
    if line() == game.board[0] or line == game.board[3] or line == game.board[6]:
        return 1

    column()
    if column() == game.board[0] or column() == game.board[1] or column() == game.board[2]:
        return 1

    diagonal()
    if diagonal() == game.board[0] or diagonal() == game.board[2]:
        return 1

    tie()



def line():

    line_1 = game.board[0] == game.board[1] == game.board[2] != "-"
    line_2 = game.board[3] == game.board[4] == game.board[5] != "-"
    line_3 = game.board[6] == game.board[7] == game.board[8] != "-"

    if line_1:
        return game.board[0]

    if line_2:
        return game.board[3]

    if line_3:
        return game.board[6]

    return 0


def column():

    column_1 = game.board[0] == game.board[3] == game.board[6] != "-"
    column_2 = game.board[1] == game.board[4] == game.board[7] != "-"
    column_3 = game.board[2] == game.board[5] == game.board[8] != "-"

    if column_1:
        return game.board[0]

    if column_2:
        return game.board[1]

    if column_3:
        return game.board[2]

    return 0


def diagonal():

    diagonal_1 = game.board[0] == game.board[4] == game.board[8] != "-"
    diagonal_2 = game.board[2] == game.board[4] == game.board[6] != "-"

    if diagonal_1:
        return game.board[0]

    if diagonal_2:
        return game.board[2]

    return 0


def tie():
    counter = 0
    for field in game.board:
        if game.board[game.board.index(field)] != "-":
            counter += 1

        if counter == 8:
            return 0


