# [기초-종합] 짝수 합 구하기

num = int(input())
sum = 0

for i in range(1, num + 1) :
    if i % 2 == 0 :
        sum += i
    
print(sum)