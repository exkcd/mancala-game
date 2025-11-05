from MancalaGame import Mancala
from color import color
import numpy as np
import random
from formatting import stat_title, list_stat

random_player = [1, 2]

total_games = 100

p1_turns = []
p2_turns = []

p1_win = 0
p2_win = 0
draw = 0

for play in range(total_games):
    game = Mancala(pits_per_player=6, stones_per_pit=4, print_output=False)

    # intialize random player to go first
    game.current_player = random.choice(random_player)

    if game.print_output:
        print(
            f'{color.BOLD + color.UNDERLINE + color.GREEN}START GAME #{play+1}{color.END}')
    i = 0

    while not game.winning_eval():
        if game.print_output:
            print(f'{color.BOLD}Turn #{i+1}{color.END}')

        game.play(game.random_move_generator())
        # game.display_board()

        game.play(game.random_move_generator())
        # game.display_board()
        i += 1
    game.check_win()

    p1_turns.append(len([x[0] for x in game.moves if x[0] == 1]))
    p2_turns.append(len([x[0] for x in game.moves if x[0] == 2]))

    p1_win += game.p1_win
    p2_win += game.p2_win
    draw += game.draw

stat_title("PLAYER 1 STATS", 12)
list_stat("P1 win %:", f"{round((p1_win/total_games)*100)}%", 29)
list_stat("P1 loss %:", f"{round((p2_win/total_games)*100)}%", 28)
list_stat("Avg turns per game:", f"{round(np.average(p1_turns))}", 19)

stat_title("PLAYER 2 STATS", 12)
list_stat("P2 win %:", f"{round((p2_win/total_games)*100)}%", 29)
list_stat("P2 loss %:", f"{round((p1_win/total_games)*100)}%", 28)
list_stat("Avg turns per game:", f"{round(np.average(p2_turns))}", 19)

stat_title("GAME STATS", 14)
list_stat("Draw %:", f"{round((draw/total_games)*100)}%", 31)
list_stat("First Turn Advantage:", f"TBD", 18)
