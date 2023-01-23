# [기초-리스트] 바둑알 십자 뒤집기

board = []

for i in range(19) :
    board.append([])

    for j in range(19) :
        board[i].append(0)

for a in range(19) :
    board[a] = list(map(int, input().split()))

num = int(input())

for b in range(1, num + 1) :
    x, y = map(int ,input().split())

    for c in range(0, 19): # 행 숫자 변경
        if board[x-1][c] == 0 :
            board[x-1][c] = 1
        else :
            board[x-1][c] = 0

    for d in range(0, 19) : # 열 숫자 변경
        if board[d][y-1] == 0 :
            board[d][y-1] = 1
        else :
            board[d][y-1] = 0

for e in range(0, 19) :
    for f in range(0, 19) :
        print(board[e][f], end=" ")
    print()