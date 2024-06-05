def islegal(xi, yi, xf, yf):
    if board[yf][xf][0] != null and board[yi][xi][0] == board[yf][xf][0]:
        return False
    else:
        return True

board = [['brook', 'bknight', 'bbishop', 'bking', 'bqueen', 'bbishop', 'bknight', 'brook'], 
    ['bpawn' for i in range(8)],
    [None for i in range(8)],
    [None for i in range(8)],
    [None for i in range(8)],
    [None for i in range(8)],
    ['wpawn' for i in range(8)],
    ['wrook', 'wknight', 'wbishop', 'wking', 'wqueen', 'wbishop', 'wknight', 'wrook']]

