class ChessGame:
    def __init__(self):
        self.board = self.create_board()
        self.current_turn = 'white'

    def create_board(self):
        # Create the initial chess board with all pieces in their starting positions
        return [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

    def display_board(self):
        # Display the current board state
        for row in range(8):
            print(f"{8-row} | {'  '.join(self.board[row])} ")
        print("   -----------------------")
        print("    a  b  c  d  e  f  g  h")

    def is_valid_move(self, start, end):
        # Basic validation of the move (this can be expanded for more rules)
        sx, sy = self.parse_position(start)
        ex, ey = self.parse_position(end)

        piece = self.board[sx][sy]

        # Check if a piece exists at the start position and if it's the correct player's turn
        if piece == '.' or (self.current_turn == 'white' and piece.islower()) or (self.current_turn == 'black' and piece.isupper()):
            print("Invalid move: no piece or not your turn.")
            return False

        # Add more complex validation (checking legal moves for specific pieces)
        return True

    def parse_position(self, pos):
        # Convert chess notation (e.g., "e2") to board indices
        file = pos[0]
        rank = pos[1]
        return 8 - int(rank), ord(file) - ord('a')

    def make_move(self, start, end):
        # Make the move on the board
        if self.is_valid_move(start, end):
            sx, sy = self.parse_position(start)
            ex, ey = self.parse_position(end)

            # Move the piece
            self.board[ex][ey] = self.board[sx][sy]
            self.board[sx][sy] = '.'

            # Switch turn
            self.current_turn = 'black' if self.current_turn == 'white' else 'white'
        else:
            print("Move is not valid. Try again.")

    def is_game_over(self):
        # Check if the game is over (this can be expanded for checkmate, stalemate)
        kings = sum([row.count('k') for row in self.board]) + sum([row.count('K') for row in self.board])
        return kings != 2

    def play(self):
        # Main game loop
        while not self.is_game_over():
            self.display_board()
            print(f"{self.current_turn.capitalize()}'s turn.")
            
            start = input("Enter the start position (e.g., 'e2'): ")
            end = input("Enter the end position (e.g., 'e4'): ")

            self.make_move(start, end)

        print("Game over!")


# Run the chess game
if __name__ == "__main__":
    game = ChessGame()
    game.play()
