from MancalaGame import Mancala


# Mancala part 2
game = Mancala(pits_per_player=6, stones_per_pit=4)
game.display_board()

# turn 1
game.play(3)
game.display_board()

game.random_move_generator()
game.display_board()

# turn 2
game.play(6)
game.display_board()

game.random_move_generator()
game.display_board()

# turn 3
game.play(5)
game.display_board()

game.random_move_generator()
game.display_board()

# turn 4
game.play(2)
game.display_board()

game.random_move_generator()
game.display_board()

# turn 5
game.play(1)
game.display_board()

game.random_move_generator()
game.display_board()