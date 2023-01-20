# [기초-리스트] 이상한 출석 번호 부르기2

num = int(input())

num_call = map(int, input().split())

num_call = list(num_call)

for i in range(num - 1, -1, -1) :
    print(num_call[i], end = ' ')