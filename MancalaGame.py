import random

from color import color

class Mancala:
    def __init__(self, pits_per_player=6, stones_per_pit=4):
        """
        The constructor for the Mancala class defines several instance variables:

        pits_per_player: This variable stores the number of pits each player has.
        stones_per_pit: It represents the number of stones each pit contains at the start of any game.
        board: This data structure is responsible for managing the Mancala board.
        current_player: This variable takes the value 1 or 2, as it's a two-player game, indicating which player's turn it is.
        moves: This is a list used to store the moves made by each player. It's structured in the format (current_player, chosen_pit).
        p1_pits_index: A list containing two elements representing the start and end indices of player 1's pits in the board data structure.
        p2_pits_index: Similar to p1_pits_index, it contains the start and end indices for player 2's pits on the board.
        p1_mancala_index and p2_mancala_index: These variables hold the indices of the Mancala pits on the board for players 1 and 2, respectively.
        """
        self.pits_per_player = pits_per_player
        self.board = [stones_per_pit] * ((pits_per_player+1) * 2)  # Initialize each pit with stones_per_pit number of stones 
        self.players = 2
        self.current_player = 1
        self.moves = []
        self.p1_pits_index = [0, self.pits_per_player-1]
        self.p1_mancala_index = self.pits_per_player
        self.p2_pits_index = [self.pits_per_player+1, len(self.board)-1-1]
        self.p2_mancala_index = len(self.board)-1
        self.p1_win = 0
        self.p2_win = 0
        self.game_draw = 0
        
        # Zeroing the Mancala for both players
        self.board[self.p1_mancala_index] = 0
        self.board[self.p2_mancala_index] = 0

    def display_board(self):
        """
        Displays the board in a user-friendly format
        """
        player_1_pits = self.board[self.p1_pits_index[0]: self.p1_pits_index[1]+1]
        player_1_mancala = self.board[self.p1_mancala_index]
        player_2_pits = self.board[self.p2_pits_index[0]: self.p2_pits_index[1]+1]
        player_2_mancala = self.board[self.p2_mancala_index]
        print('P1               P2')
        print('     ____{}____     '.format(player_2_mancala))
        for i in range(self.pits_per_player):
            if i == self.pits_per_player - 1:
                print('{} -> |_{}_|_{}_| <- {}'.format(i+1, player_1_pits[i], 
                        player_2_pits[-(i+1)], self.pits_per_player - i))
            else:    
                print('{} -> | {} | {} | <- {}'.format(i+1, player_1_pits[i], 
                        player_2_pits[-(i+1)], self.pits_per_player - i))
        print('         {}         '.format(player_1_mancala))
        
    def valid_move(self, pit):
        """
        Function to check if the pit chosen by the current_player is a valid move.
        """
        if pit < 1 or pit > self.pits_per_player:
            return False
        if self.current_player == 1:
            board_index = pit - 1
            if board_index < self.p1_pits_index[0] or board_index > self.p1_pits_index[1]:
                return False
            if self.board[board_index] == 0:
                return False
        else:
            board_index = self.p2_pits_index[0] + (pit - 1)
            if board_index < self.p2_pits_index[0] or board_index > self.p2_pits_index[1]:
                return False
            if self.board[board_index] == 0:
                return False
        return True
        
    def random_move_generator(self):
        """
        Function to generate random valid moves with non-empty pits for the random player
        """
        valid_pits = []
        if self.current_player == 1:
            for pit in range(1, self.pits_per_player + 1):
                board_index = pit - 1
                if self.board[board_index] > 0:
                    valid_pits.append(pit)
        else:
            for pit in range(1, self.pits_per_player + 1):
                board_index = self.p2_pits_index[0] + (pit - 1)
                if self.board[board_index] > 0:
                    valid_pits.append(pit)
        if valid_pits:
            return random.choice(valid_pits)
        return None
    
    def play(self, pit):
        """
        This function simulates a single move made by a specific player using their selected pit. It primarily performs three tasks:
        1. It checks if the chosen pit is a valid move for the current player. If not, it prints "INVALID MOVE" and takes no action.
        2. It verifies if the game board has already reached a winning state. If so, it prints "GAME OVER" and takes no further action.
        3. After passing the above two checks, it proceeds to distribute the stones according to the specified Mancala rules.

        Finally, the function then switches the current player, allowing the other player to take their turn.
        """
        if self.winning_eval():
            if (self.p1_mancala_index > self.p2_mancala_index):
                print(f"{color.GREEN}GAME OVER{color.END}\nP1 wins!")
                self.p1_win += 1
                print(self.p1_win)
            elif(self.p2_mancala_index > self.p1_mancala_index):
                print(f"{color.RED}GAME OVER{color.END}\nP2 wins!")
                self.p2_win += 1
                print(self.p2_win)
            else:
                print(f"{color.YELLOW}Draw!{color.END}")
                self.game_draw += 1
                print(self.game_draw)
            return self.board
        if not self.valid_move(pit):
            print("INVALID MOVE")
            return self.board
        
        if self.current_player == 1:
            print(f'{color.RED}Player {self.current_player} chose pit: {pit} {color.END}')
        else:
            print(f'{color.CYAN}Player {self.current_player} chose pit: {pit} {color.END}')
        self.moves.append((self.current_player, pit))
        if self.current_player == 1:
            current_pit_index = pit - 1
        else:
            current_pit_index = self.p2_pits_index[0] + (pit - 1)
        stones = self.board[current_pit_index]
        self.board[current_pit_index] = 0
        current_index = current_pit_index
        opponent_mancala = self.p2_mancala_index if self.current_player == 1 else self.p1_mancala_index
        while stones > 0:
            current_index = (current_index + 1) % len(self.board)
            if current_index == opponent_mancala:
                continue
            self.board[current_index] += 1
            stones -= 1
        if self.current_player == 1:
            if (current_index >= self.p1_pits_index[0] and 
                current_index <= self.p1_pits_index[1] and 
                self.board[current_index] == 1):
                opposite_index = self.p2_pits_index[1] - (current_index - self.p1_pits_index[0])
                if self.board[opposite_index] > 0:
                    captured = self.board[opposite_index] + self.board[current_index]
                    self.board[opposite_index] = 0
                    self.board[current_index] = 0
                    self.board[self.p1_mancala_index] += captured
        else:
            if (current_index >= self.p2_pits_index[0] and 
                current_index <= self.p2_pits_index[1] and 
                self.board[current_index] == 1):
                opposite_index = self.p1_pits_index[1] - (current_index - self.p2_pits_index[0])
                if self.board[opposite_index] > 0:
                    captured = self.board[opposite_index] + self.board[current_index]
                    self.board[opposite_index] = 0
                    self.board[current_index] = 0
                    self.board[self.p2_mancala_index] += captured
        self.current_player = 2 if self.current_player == 1 else 1
        return self.board
    
    def winning_eval(self):
        """
        Function to verify if the game board has reached the winning state.
        Hint: If either of the players' pits are all empty, then it is considered a winning state.
        """
        p1_empty = all(self.board[i] == 0 for i in range(self.p1_pits_index[0], self.p1_pits_index[1] + 1))
        p2_empty = all(self.board[i] == 0 for i in range(self.p2_pits_index[0], self.p2_pits_index[1] + 1))
        if p1_empty or p2_empty:
            if not p1_empty:
                for i in range(self.p1_pits_index[0], self.p1_pits_index[1] + 1):
                    self.board[self.p1_mancala_index] += self.board[i]
                    self.board[i] = 0
            if not p2_empty:
                for i in range(self.p2_pits_index[0], self.p2_pits_index[1] + 1):
                    self.board[self.p2_mancala_index] += self.board[i]
                    self.board[i] = 0
            return True
        return False