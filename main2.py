class ChessGame:
    def __init__(self):
        self.board = self.create_board()
        self.current_player = "white"
        
    def create_board(self):
        board = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(None)
            board.append(row)
        board[0][0] = "r"
        board[0][1] = "n"
        board[0][2] = "b"
        board[0][3] = "q"
        board[0][4] = "k"
        board[0][5] = "b"
        board[0][6] = "n"
        board[0][7] = "r"
        for i in range(8):
            board[1][i] = "p"
        board[7][0] = "R"
        board[7][1] = "N"
        board[7][2] = "B"
        board[7][3] = "Q"
        board[7][4] = "K"
        board[7][5] = "B"
        board[7][6] = "N"
        board[7][7] = "R"
        for i in range(8):
            board[6][i] = "P"
        return board
    
    def print_board(self):
        for row in self.board:
            row_str = ""
            for square in row:
                if square is None:
                    row_str += "."
                else:
                    row_str += square
            print(row_str)
                
    def is_valid_move(self, from_square, to_square):
        return True  # Placeholder for now
    
    def make_move(self, from_square, to_square):
        if not self.is_valid_move(from_square, to_square):
            print("Invalid move.")
            return
        i, j = self.square_to_index(from_square)
        x, y = self.square_to_index(to_square)
        self.board[x][y] = self.board[i][j]
        self.board[i][j] = None
        self.current_player = "black" if self.current_player == "white" else "white"
        
    def square_to_index(self, square):
        file, rank = square[0], int(square[1])
        return rank-1, ord(file)-ord('a')

        
    def play(self):
        while True:
            self.print_board()
            print(f"It's {self.current_player}'s turn.")
            from_square = input("Enter the square you want to move from (e.g. 'e2'): ")
            to_square = input("Enter the square you want to move to: ")
            self.make_move(from_square, to_square)


game = ChessGame()
game.play()
