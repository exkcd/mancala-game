import numpy as np
from copy import deepcopy

def minmax_decision(game, depth=4):

    player = game.current_player

    def max_value(state, depth):
        if depth == 0 or state.winning_eval():
            return state.utility(state.board, player)
        v = -np.inf
        for a in state.actions():
            new_state = deepcopy(state)
            new_state.play(a)
            v = max(v, min_value(new_state, depth - 1))
        return v
    
    def min_value(state, depth):
        if depth == 0 or state.winning_eval():
            return state.utility(state.board, player)
        v = np.inf

        for a in state.actions():
            new_state = deepcopy(state)
            new_state.play(a)
            v = min(v, max_value(new_state, depth - 1))

        return v
    
    best_score = -np.inf
    best_action = 0

    for a in game.actions():
        new_state = deepcopy(game)
        new_state.play(a)

        value = min_value(new_state, depth - 1)
        if value > best_score:
            best_score = value
            best_action = a

    return best_action