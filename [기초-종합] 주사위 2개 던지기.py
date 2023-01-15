# [기초-종합] 주사위 2개 던지기

num1, num2 = input().split(' ')

num1 = int(num1)
num2 = int(num2)

for i in range(1, num1 + 1) :
    for j in range(1, num2 + 1) :
        print(i, j)