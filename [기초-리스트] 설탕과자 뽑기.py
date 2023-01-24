# [기초-리스트] 설탕과자 뽑기

# x, y : 가장 왼쪽, 위쪽

# 입력 1 : 세로(h) * 가로(w) 격자판의 크기
# 입력 2 : 막대의 개수(n)
# 입력 3 : 막대의 길이(l), 방향(d : 가로 - 0, 세로 - 1), 좌료(x, y)

h, w = list(map(int, input().split()))

board = []

for i in range(h) :
    board.append([])
    for j in range(w) :
        board[i].append(0)

n = int(input())

for a in range(n) :
    l, d, x, y = list(map(int, input().split()))

    if d == 0 :
        for b in range(l) :
            board[x-1][(y-1)+b] = 1

    elif d == 1 :
        for c in range(l) :
            board[(x-1)+c][y-1] = 1

for d in range(h) :
    for e in range(w) :
        print(board[d][e], end = " ")
    print()