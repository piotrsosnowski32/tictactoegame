from game import play_game

computer_figure = ""
player_figure = ""

while computer_figure == "":

    player_figure = input("Wybierz x lub o: ")
    computer_figure = ""
    if player_figure == "x":
        computer_figure = "o"
    elif player_figure == "o":
        computer_figure = "x"


play_game(player_figure, computer_figure)