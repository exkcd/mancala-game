def alpha_beta_search(game, depth=4):
    player= game.current_player

    def max_value(state, alpha, beta, depth):
        if depth==0 or state.winning_eval():
            return state.utility(state.board, player)
        v = -np.inf
        for a in state.actions():
            new_state = deepcopy(state)
            new_state.play(a)
            v=max(v, min_value(new_state, alpha, beta, depth-1))
            if (v >= beta):
                return v
            alpha = max(alpha, v)
        return v
    def min_value(state, alpha, beta, depth):
        if depth==0 or state.winning_eval():
            return state.utility(state.board, player)
        v=np.inf
        for a in state.actions():
            new_state = deepcopy(state)
            new_state.play(a)
            v=min(v, max_value(new_state, alpha, beta, depth -1))
            if v<= alpha:
                return v
            beta=min(beta, v)
        return v
    
    best_score = -np.inf
    beta=np.inf
    best_action= None
    for a in game.actions():
        new_state = deepcopy(game)
        new_state.play(a)
        v = min_value(new_state, best_score, beta, depth -1)
        if (v > best_score):
            best_score = v
            best_action = a
    return best_action