class Piece:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        return str(self.valeur) + " "+ str(self.couleur)

class Board:
    def __init__(self, board):
        self.board = board

    def __repr__(self):
        return str(self.board)
    
    def position(self, board):
        self.board[0] = "R"

        
b = Board([0, 1, 2, 3])



p = [Piece("", ""),Piece("", ""),Piece("", ""),Piece("", ""),Piece("", ""),Piece("", ""),Piece("", ""),Piece("", ""),
    Piece('P','w'),Piece('P','w'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),
    Piece('TOUR','blanc'),Piece('CAVALIER','blanc'),Piece('FOU','blanc'),Piece('DAME','blanc'),Piece('ROI','blanc'),Piece('FOU','blanc'),Piece('CAVALIER','blanc'),Piece('TOUR','blanc')
]

print(p)

prin('ok')

##class Board:
##    def __init__(self, board, case):
##        self.board = board
##        self.case = case
##    
##
##board = [[0, 1, 2, 3, 4, 5, 6, 7],
##        [8, 9, 10, 11, 12, 13, 14, 15],
##        [16, 17, 18, 19, 20, 21, 22, 23],
##        [24, 25, 26, 27, 28, 29, 30, 31],
##        [32, 33, 34, 35, 36, 37, 38, 39],
##        [40, 41, 42, 43, 44, 45, 46, 47],
##        [48, 49, 50, 51, 52, 53, 54, 55],
##        [56, 57, 58, 59, 60, 61, 62,63]
##]
##
##
##case = [
##    Piece('R','B'),Piece('N','B'),Piece('B','B'),Piece('Q','B'),Piece('K','B'),Piece('B','B'),Piece('N','B'),Piece('R','B'),
##    Piece('P','B'),Piece('P','B'),Piece('P','B'),Piece('P','B'),Piece('P','B'),Piece('P','B'),Piece('PION','noir'),Piece('PION','noir'),
##    Piece("", ""),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
##    Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
##    Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
##    Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
##    Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),
##    Piece('TOUR','blanc'),Piece('CAVALIER','blanc'),Piece('FOU','blanc'),Piece('DAME','blanc'),Piece('ROI','blanc'),Piece('FOU','blanc'),Piece('CAVALIER','blanc'),Piece('TOUR','blanc')
##
##
##]
##
##print(case)