# [기초-리스트] 성실한 개미

# 오른쪽이나 아래쪽으로 움직임
# 0 : 갈 수 있는 곳, 1 : 벽 또는 장애물, 2 : 먹이
# 맨 아래의 가장 오른쪽 도착, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우
# => 더이상 이동하지 않고 그 곳에 머무름
# 테두리는 모두 벽으로 되어있음
# 개미집인 (2, 2)에서 출발

# 개미가 이동한 경로 : 9로 표시

maze = []

for i in range(10) :
    maze.append([])
    for j in range(10) :
        maze[i].append(0)

for a in range(10) :
    maze[a] = list(map(int, input().split()))

x = 1
y = 1

while True :

    if maze[x][y] == 0 :
        maze[x][y] = 9

    elif maze[x][y] == 2 :
        maze[x][y] = 9
        break

    if (maze[x][y+1] == 1) and (maze[x+1][y] == 1) :
        break

    if maze[x][y+1] != 1 :
        y += 1

    elif maze[x+1][y] != 1 :
        x += 1


for b in range(10) :
    for c in range(10) :
        print(maze[b][c], end = " ")
    print()