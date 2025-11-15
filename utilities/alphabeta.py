import numpy as np


def alpha_beta_search(game, depth=4):
    player = game.current_player

    def max_value(alpha, beta, depth):
        if depth == 0 or game.winning_eval():
            return game.utility(game.board, player)

        v = -np.inf
        for a in game.actions():
            undo_info = game.play_with_undo(a)
            v = max(v, min_value(alpha, beta, depth-1))
            game.undo_move(undo_info)

            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(alpha, beta, depth):
        if depth == 0 or game.winning_eval():
            return game.utility(game.board, player)

        v = np.inf
        for a in game.actions():
            undo_info = game.play_with_undo(a)
            v = min(v, max_value(alpha, beta, depth-1))
            game.undo_move(undo_info)

            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    best_score = -np.inf
    alpha = -np.inf
    beta = np.inf
    best_action = None

    for a in game.actions():
        undo_info = game.play_with_undo(a)
        v = min_value(alpha, beta, depth-1)
        game.undo_move(undo_info)

        if v > best_score:
            best_score = v
            best_action = a
            alpha = v

    return best_action
