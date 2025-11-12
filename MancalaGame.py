import random
from utilities.formatting import color

class Mancala:
    def __init__(self, pits_per_player=6, stones_per_pit=4, print_output=True):
        self.pits_per_player = pits_per_player
        # Initialize each pit with stones_per_pit number of stones
        self.board = [stones_per_pit] * ((pits_per_player + 1) * 2)
        self.players = 2
        self.current_player = 1
        self.moves = []
        self.p1_pits_index = [0, self.pits_per_player - 1]
        self.p1_mancala_index = self.pits_per_player
        self.p2_pits_index = [
            self.pits_per_player + 1, len(self.board) - 1 - 1]
        self.p2_mancala_index = len(self.board) - 1

        self.p1_win = 0
        self.p2_win = 0
        self.draw = 0
        self.print_output = print_output

        # winning advantage
        self.first= 0
        self.wins_w_first= 0

        # Zeroing the Mancala for both players
        self.board[self.p1_mancala_index] = 0
        self.board[self.p2_mancala_index] = 0

    def display_board(self):
        """
        Displays the board in a user-friendly format
        """
        player_1_pits = self.board[self.p1_pits_index[0]: self.p1_pits_index[1] + 1]
        player_1_mancala = self.board[self.p1_mancala_index]
        player_2_pits = self.board[self.p2_pits_index[0]: self.p2_pits_index[1] + 1]
        player_2_mancala = self.board[self.p2_mancala_index]

        print('P1               P2')
        print('     ____{}____     '.format(player_2_mancala))
        for i in range(self.pits_per_player):
            if i == self.pits_per_player - 1:
                print('{} -> |_{}_|_{}_| <- {}'.format(i + 1, player_1_pits[i],
                                                       player_2_pits[-(i + 1)], self.pits_per_player - i))
            else:
                print('{} -> | {} | {} | <- {}'.format(i + 1, player_1_pits[i],
                                                       player_2_pits[-(i + 1)], self.pits_per_player - i))

        print('         {}         '.format(player_1_mancala))

    def valid_move(self, pit): # actions
        return True if pit in range(1, self.pits_per_player+1) else False
    
    def actions(self):
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
        return valid_pits

    def random_move_generator(self):
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

    def play(self, pit): # result
        if pit is None:
            return self.board
        
        if not self.winning_eval():
            if self.print_output:
                self.print_moves(pit)
            current_index = self.get_pit_index(pit)

            if not self.valid_move(pit):
                if self.print_output:
                    print("INVALID MOVE")
                return self.board

            stones = self.board[current_index]  # get amount of stones
            self.board[current_index] = 0  # remove stones
            opponent_mancala = self.p2_mancala_index if self.current_player == 1 else self.p1_mancala_index

            while stones > 0:
                current_index = (current_index + 1) % len(self.board)

                if current_index == opponent_mancala:
                    continue
                self.board[current_index] += 1
                stones -= 1

            self.capture_stones(current_index)
            self.moves.append((self.current_player, pit))
            self.switch_player()
        return self.board

    def capture_stones(self, current_index):
        if self.current_player == 1:
            if (current_index >= self.p1_pits_index[0] and
                current_index <= self.p1_pits_index[1] and
                    self.board[current_index] == 1):
                opposite_index = self.p2_pits_index[1] - \
                    (current_index - self.p1_pits_index[0])
                if self.board[opposite_index] > 0:
                    captured = self.board[opposite_index] + \
                        self.board[current_index]
                    self.board[opposite_index] = 0
                    self.board[current_index] = 0
                    self.board[self.p1_mancala_index] += captured
        else:
            if (current_index >= self.p2_pits_index[0] and
                current_index <= self.p2_pits_index[1] and
                    self.board[current_index] == 1):
                opposite_index = self.p1_pits_index[1] - \
                    (current_index - self.p2_pits_index[0])
                if self.board[opposite_index] > 0:
                    captured = self.board[opposite_index] + \
                        self.board[current_index]
                    self.board[opposite_index] = 0
                    self.board[current_index] = 0
                    self.board[self.p2_mancala_index] += captured

    def print_moves(self, pit):
        if self.current_player == 1:
            print(
                f'{color.BLUE}Player {self.current_player} chose pit: {pit}{color.END}')
        else:
            print(
                f'{color.RED}Player {self.current_player} chose pit: {pit}{color.END}')

    def get_pit_index(self, pit):
        if self.current_player == 1:
            return pit - 1
        else:
            return self.p1_mancala_index + pit

    def switch_player(self):
        self.current_player = 2 if self.current_player == 1 else 1

    def check_win(self):
        if self.winning_eval():
            p1_total = self.board[self.p1_mancala_index]
            p2_total = self.board[self.p2_mancala_index]
            if p1_total > p2_total:
                self.p1_win = 1
                if(self.first == 1):
                    self.wins_w_first += 1
                # if self.print_output:
                print(f'{color.BOLD + color.BLUE}GAME OVER: P1 wins!{color.END}')
            elif p2_total > p1_total:
                if(self.first == 2):
                    self.wins_w_first += 1
                    self.p2_win = 1
                # if self.print_output:
                print(f'{color.BOLD + color.RED}GAME OVER: P2 wins!{color.END}')
            else:
                self.draw = 1
                # if self.print_output:
                print(f'{color.BOLD + color.YELLOW}GAME OVER: It\'s a draw!{color.END}')

    def winning_eval(self):
        p1_empty = all(self.board[i] == 0 for i in range(
            self.p1_pits_index[0], self.p1_pits_index[1] + 1))
        p2_empty = all(self.board[i] == 0 for i in range(
            self.p2_pits_index[0], self.p2_pits_index[1] + 1))
        if p1_empty or p2_empty:
            if not p1_empty:
                for i in range(self.p1_pits_index[0], self.p1_pits_index[1] + 1):
                    self.board[self.p1_mancala_index] += self.board[i]
                    self.board[i] = 0
            if not p2_empty:
                for i in range(self.p2_pits_index[0], self.p2_pits_index[1] + 1):
                    self.board[self.p2_mancala_index] += self.board[i]
                    self.board[i] = 0

        return True if p1_empty or p2_empty else False
    
    def utility(self, state, player):
        if self.current_player == 1:
            return self.board[self.p1_mancala_index]- self.board[self.p2_mancala_index]
        else:
            return self.board[self.p2_mancala_index] - self.board[self.p1_mancala_index]