# [기초-리스트] 바둑판에 흰 돌 놓기

num = int(input())

board = []

for i in range(20) :
    board.append([])
    for j in range(20) :
        board[i].append(0)

for i in range(0, num) :
    x, y = map(int, input().split())
    board[x][y] = 1

for x in range(1, 20) :
    for y in range(1, 20) :
        print(board[x][y], end = " ")
    print()
