def flip(row, collumn, board):
    for i in range(row):
        for j in range(collumn):
            if board[i][j] == 1:
                board[i][j] == 0
            else:
                board[i][j] == 1
    return board

n = int(input())
cows = []
for i in range(n):
    line = input()
    line = line.split()
    line = [int(i) for i in line]
    cows.append(line)

ans = 0
for i in range(n):
    row = cows[-i-1]
    for j in range(n):
        cow = row[-j-1]
        if cow == 1:
            board = flip(n-i, n-j, board)
            ans += 1
print(ans)