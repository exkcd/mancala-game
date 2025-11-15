from utilities.MancalaGame import Mancala
import numpy as np
import random
from utilities.formatting import color, stat_title, list_stat
from utilities.minmax import minmax_decision
from utilities.alphabeta import alpha_beta_search
from copy import deepcopy
from tqdm import tqdm

random_player = [1, 2]

total_games = 100

p1_turns = []
p2_turns = []


wins = {
    "p1": 0,
    "p2": 0,
    "draw": 0,
    "wins_first": 0
}

for play in tqdm(range(total_games)):

    game = Mancala(pits_per_player=6, stones_per_pit=4, print_output=False)

    # intialize random player to go first
    game.current_player = random.choice(random_player)
    game.first = game.current_player

    if game.print_output:
        print(
            f'{color.BOLD + color.UNDERLINE + color.GREEN}START GAME #{play+1}{color.END}')
    i = 0

    while not game.winning_eval():
        if game.print_output:
            print(f'{color.BOLD}Turn #{i+1}{color.END}')

        if game.current_player == 1:
            move = minmax_decision(game, depth=5)
            game.play(move)

            if(game.print_output):
                game.display_board()
        else:
            game.play(game.random_move_generator())
            if (game.print_output):
                game.display_board()
            i += 1
    game.check_win()
    p1_turns.append(len([x[0] for x in game.moves if x[0] == 1]))
    p2_turns.append(len([x[0] for x in game.moves if x[0] == 2]))

    wins["p1"] += game.p1_win
    wins["p2"] += game.p2_win
    wins["draw"] += game.draw
    wins["wins_first"] += game.wins_w_first

print("\n")
stat_title("PLAYER 1 STATS", 12)
list_stat("P1 win %:", f"{round((wins["p1"]/total_games)*100)}%", 29)
list_stat("P1 loss %:", f"{round((wins["p2"]/total_games)*100)}%", 28)
list_stat("Avg turns per game:", f"{round(np.average(p1_turns))}", 19)

stat_title("PLAYER 2 STATS", 12)
list_stat("P2 win %:", f"{round((wins["p2"]/total_games)*100)}%", 29)
list_stat("P2 loss %:", f"{round((wins["p1"]/total_games)*100)}%", 28)
list_stat("Avg turns per game:", f"{round(np.average(p2_turns))}", 19)

stat_title("GAME STATS", 14)
list_stat("Draw %:", f"{round((wins["draw"]/total_games)*100)}%", 31)
list_stat("First Turn Advantage %:", f"{round((wins["wins_first"]/total_games)*100)}%", 15)
