import random
random.seed(109)

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

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
        self.board = [stones_per_pit] * ((pits_per_player + 1) * 2)  # Initialize each pit with stones_per_pit number of stones
        self.players = 2
        self.current_player = 1
        self.moves = []
        self.p1_pits_index = [0, self.pits_per_player - 1]
        self.p1_mancala_index = self.pits_per_player
        self.p2_pits_index = [self.pits_per_player + 1, len(self.board) - 1 - 1]
        self.p2_mancala_index = len(self.board) - 1

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
        turn = color.RED + 'Turn: P1' + color.END if self.current_player == 1 else color.CYAN + 'Turn: P2' + color.END
        print(turn)

    def valid_move(self, pit):
        """
        Function to check if the pit chosen by the current_player is a valid move.
        """

        # write your code here
        return True if pit in range(0, len(self.board)) and self.board[pit] != 0 else False

    def random_move_generator(self):
        """
        Function to generate random valid moves with non-empty pits for the random player
        """

        # write your code here
        if self.current_player == 1:
            pits = range(self.p1_pits_index[0], self.p1_pits_index[1]+1)
        else:
            pits = range(self.p2_pits_index[0], self.p2_pits_index[1]+1)

        available_pits = [x for x in pits if self.board[x] > 0]

        if not available_pits:
            print('No available pits')

        chosen_pit = random.choice(available_pits)

        if self.current_player == 1:
            pit_num = chosen_pit + 1
        else:
            pit_num = chosen_pit - self.p1_mancala_index

        self.play(pit_num)


    def play(self, pit):
        """
        This function simulates a single move made by a specific player using their selected pit. It primarily performs three tasks:
        1. It checks if the chosen pit is a valid move for the current player. If not, it prints "INVALID MOVE" and takes no action.
        2. It verifies if the game board has already reached a winning state. If so, it prints "GAME OVER" and takes no further action.
        3. After passing the above two checks, it proceeds to distribute the stones according to the specified Mancala rules.

        Finally, the function then switches the current player, allowing the other player to take their turn.
        """

        # write your code here

        pit_index = self.get_pit_index(pit)

        if self.current_player == 1:
            print(f'{color.RED}Player {self.current_player} chose pit: {pit} {color.END}')
        else:
            print(f'{color.CYAN}Player {self.current_player} chose pit: {pit} {color.END}')

        if not self.valid_move(pit_index):
            print("INVALID MOVE")
            self.switch_player()
            return
        self.moves.append((self.current_player, pit))

        stones = self.board[pit_index]  # stones in pit
        self.board[pit_index] = 0  # empty current pit

        index = pit_index
        while stones > 0:
            index = (index + 1) % len(self.board)

            # skip over opponent's mancala
            if self.current_player == 1 and index == self.p2_mancala_index:
                continue
            if self.current_player == 2 and index == self.p1_mancala_index:
                continue

            self.board[index] += 1
            stones -= 1

        last_pit = index

        if self.current_player == 1 and self.p1_pits_index[0] <= last_pit <= self.p1_pits_index[1] :
            if self.board[last_pit] == 1: # if pit was empty before, and now it has one
                opp_pit = len(self.board) - 2 - last_pit

                if self.board[last_pit] > 0:
                    captured_stones = self.board[last_pit] + self.board[opp_pit]
                    self.board[last_pit] = 0
                    self.board[opp_pit] = 0
                    self.board[self.p1_mancala_index] = captured_stones

        if self.current_player == 2 and self.p2_pits_index[0] <= last_pit <= self.p2_pits_index[1] :
            if self.board[last_pit] == 1: # if pit was empty before, and now it has one
                opp_pit = len(self.board) - 2 - last_pit
                if self.board[last_pit] > 0:
                    captured_stones = self.board[last_pit] + self.board[opp_pit]
                    self.board[last_pit] = 0
                    self.board[opp_pit] = 0
                    self.board[self.p2_mancala_index] = captured_stones
        if self.winning_eval():
            print("GAME OVER")
            if (self.p1_mancala_index > self.p2_mancala_index):
                print("P1 win")
            elif(self.p2_mancala_index > self.p1_mancala_index):
                print("P2 win")
            else:
                print("Draw")
            return
        self.switch_player()

    # helper function to get the pit index
    def get_pit_index(self, pit_num):
        if self.current_player == 1:
            return pit_num - 1
        else:
            return self.p1_mancala_index + pit_num

    # helper function to switch the players more easily
    def switch_player(self):
        self.current_player = 2 if self.current_player == 1 else 1


    def winning_eval(self):
        """
        Function to verify if the game board has reached the winning state.
        Hint: If either of the players' pits are all empty, then it is considered a winning state.
        """

        # write your code here
        p1_empty = all(self.board[i] == 0 for i in range(self.p1_pits_index[0], self.p1_pits_index[1]+1))
        p2_empty = all(self.board[i] == 0 for i in range(self.p2_pits_index[0], self.p2_pits_index[1]+1))

        return p1_empty or p2_empty
