import random
import game


def smart_move(player_position, player_figure):
    i = 0
    a = random.randint(1, 9)
    for field in game.board:
        if field == player_figure:
            i += 1
    if i == 1:
        a = first_move(player_position)

    return a

    #tactical_checker(player_position, player_figure)


def first_move(player_position, player_figure):
    if player_position == 5:
        a = random.randint(1, 9)
    else:
        a = 5
    return a


# sprawdzenie pól przeciwnika
def tactical_checker(player_position, player_figure):
    for field in game.board:
        if field == player_figure:
            return

# tworzenie rozwiązań

# wybór rozwiązania

