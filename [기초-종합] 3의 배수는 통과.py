# [기초-종합] 3의 배수는 통과

num = int(input())
result = 1

for i in range(1, num + 1):
    if result % 3 != 0 :
        print(result, end = ' ')
        result += 1  
    else :
        result += 1