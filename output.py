from MancalaGame import Mancala
from color import color

turns_per_game = []
p1_win = 0
p2_win = 0
draw = 0

for play in range(100):
    game = Mancala(6, 4)
    print(f'{color.BOLD + color.UNDERLINE + color.GREEN}START GAME #{play+1}{color.END}')
    i = 0

    while not game.winning_eval():
        print(f'{color.BOLD}Turn #{i+1}{color.END}')

        game.play(game.random_move_generator())
        # game.display_board()

        game.play(game.random_move_generator())
        # game.display_board()

        i += 1
    game.check_win()

    turns_per_game.append(i)
    p1_win += game.p1_win
    p2_win += game.p2_win
    draw += game.draw

print(f"{color.BOLD}{color.GREEN}===========GAME STATS==========={color.END}")
print("Player 1 wins", p1_win)
print("Player 1 loses", p2_win)
print("Draws", draw)