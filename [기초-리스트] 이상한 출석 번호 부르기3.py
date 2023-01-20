# [기초-리스트] 이상한 출석 번호 부르기3

num = int(input())

num_call = map(int, input().split())

num_call = list(num_call)

result = num_call[0]

for i in range(0, num) :

    if num_call[i] < result :
        result = num_call[i]

print(result)