import math

def alpha_beta_pruning(state, depth, alpha, beta, is_maximizing_player):
    if depth == 0 or game_over(state):
        return evaluate(state)
    
    if is_maximizing_player:
        max_eval = -math.inf
        for move in possible_moves(state):
            eval = alpha_beta_pruning(move, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in possible_moves(state):
            eval = alpha_beta_pruning(move, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def game_over(state):
    # Implement your own logic to check if the game is over
    pass

def evaluate(state):
    # Implement your own evaluation function to evaluate the given state
    pass

def possible_moves(state):
    # Generate and return a list of possible next states from the current state
    pass
