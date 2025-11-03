from MancalaGame import Mancala
from color import color

turns_per_game = []
p1_win = 0
p2_win = 0
draw = 0


for play_game in range(4):
    game = Mancala(pits_per_player=6, stones_per_pit=4)
    # game.display_board()
    i = 0
    
    print(f"{color.BOLD + color.UNDERLINE}START GAME #: {play_game+1}{color.END}")

    while not game.winning_eval():
        print(f"{color.BOLD}Turn number: {i+1}{color.END}")

        # player 
        game.play(game.random_move_generator())
        # game.display_board()

        game.play(game.random_move_generator())
        # game.display_board()

        i += 1

    turns_per_game.append(i)
    p1_win += game.p1_win
    p2_win += game.p2_win
    draw += game.game_draw
    print(turns_per_game)
    print(p1_win)
    print(p2_win)
    print(draw)

print(f"{color.BOLD}{color.GREEN}GAME STATS{color.END}")
print("Player 1 wins", p1_win)
print("Player 1 loses", p2_win)
print("Draws", draw)