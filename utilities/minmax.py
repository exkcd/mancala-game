import numpy as np


def minmax_decision(game, depth=4):

    player = game.current_player

    def max_value(depth):
        if depth == 0 or game.winning_eval():
            return game.utility(game.board, player)

        v = -np.inf
        for a in game.actions():
            undo_info = game.play_with_undo(a)
            v = max(v, min_value(depth - 1))
            game.undo_move(undo_info)
        return v

    def min_value(depth):
        if depth == 0 or game.winning_eval():
            return game.utility(game.board, player)

        v = np.inf
        for a in game.actions():
            undo_info = game.play_with_undo(a)
            v = min(v, max_value(depth - 1))
            game.undo_move(undo_info)
        return v

    best_score = -np.inf
    best_action = None

    for a in game.actions():
        undo_info = game.play_with_undo(a)
        value = min_value(depth - 1)
        game.undo_move(undo_info)

        if value > best_score:
            best_score = value
            best_action = a

    return best_action
