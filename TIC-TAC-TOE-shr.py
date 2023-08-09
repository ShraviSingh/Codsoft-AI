class TicTacToeGame:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]

    def display_board(self):
        print('-------------')
        for i in range(0, 9, 3):
            print(f"| {self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]} |")
            print('-------------')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, position, player):
        self.board[position] = player

    def check_winner(self, player):
        for combo in self.winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def is_board_full(self):
        return all(spot != ' ' for spot in self.board)

    def minimax(self, depth, maximizing_player):
        if self.check_winner('X'):
            return -10 + depth
        if self.check_winner('O'):
            return 10 - depth
        if self.is_board_full():
            return 0

        if maximizing_player:
            max_eval = float('-inf')
            for move in self.available_moves():
                self.make_move(move, 'O')
                eval_score = self.minimax(depth + 1, False)
                self.make_move(move, ' ')
                max_eval = max(max_eval, eval_score)
            return max_eval

        else:
            min_eval = float('inf')
            for move in self.available_moves():
                self.make_move(move, 'X')
                eval_score = self.minimax(depth + 1, True)
                self.make_move(move, ' ')
                min_eval = min(min_eval, eval_score)
            return min_eval

    def find_best_move(self):
        best_score = float('-inf')
        best_move = None
        for move in self.available_moves():
            self.make_move(move, 'O')
            move_score = self.minimax(0, False)
            self.make_move(move, ' ')

            if move_score > best_score:
                best_score = move_score
                best_move = move

        return best_move

def get_player_symbol():
    while True:
        symbol = input("Choose your symbol ('X' or 'O'): ").upper()
        if symbol in ('X', 'O'):
            return symbol
        else:
            print("Invalid choice. Please select 'X' or 'O'.")

def get_player_move(board):
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move not in range(9):
                raise ValueError
            if board[move] != ' ':
                print("Spot already taken. Try again.")
                continue
            return move
        except ValueError:
            print("Invalid input. Enter a number between 0 and 8.")

def play_game():
    game = TicTacToeGame()
    print("Welcome to Tic-Tac-Toe!")
    game.display_board()

    player_symbol = get_player_symbol()
    ai_symbol = 'X' if player_symbol == 'O' else 'O'
    print(f"You are '{player_symbol}' and AI is '{ai_symbol}'. Let's begin!")

    while not game.is_board_full():
        player_move = get_player_move(game.board)
        game.make_move(player_move, player_symbol)
        game.display_board()

        if game.check_winner(player_symbol):
            print(f"Congratulations! You ('{player_symbol}') win!")
            return

        if game.is_board_full():
            print("It's a draw!")
            return

        ai_move = game.find_best_move()
        game.make_move(ai_move, ai_symbol)
        print("AI's move:")
        game.display_board()

        if game.check_winner(ai_symbol):
            print("AI wins! Better luck next time.")
            return

if __name__ == "__main__":
    play_game()
