class Piece:
    def __init__(self, id):
        self.id = id



def islegal(xi, yi, xf, yf):
    if board[yf][xf][0] != null and board[yi][xi][0] == board[yf][xf][0]:
        return False
    else:
        return True

board = [
    ['wrook', 'wknight', 'wbishop', 'wqueen', 'wking', 'wbishop', 'wknight', 'wrook'], 
    ['wpawn' for i in range(8)],
    [None for i in range(8)],
    [None for i in range(8)],
    [None for i in range(8)],
    [None for i in range(8)],
    ['bpawn' for i in range(8)],
    ['brook', 'bknight', 'bbishop', 'bqueen', 'bking', 'bbishop', 'bknight', 'brook']
]

for row in board:
    print(row)