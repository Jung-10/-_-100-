# [기초-종합] 언제까지 더해야 할까?

num = int(input())
sum = 0

for i in range(1, 1001) :
    sum += i

    if num <= sum :
        break

print(i)