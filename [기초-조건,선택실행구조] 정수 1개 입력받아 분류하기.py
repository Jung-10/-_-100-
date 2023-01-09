# [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기

num = int(input())

num = int(num)

if (num < 0) and (num % 2 == 0) :
    print('A')

elif (num < 0) and (num % 2 == 1) :
    print('B')

elif (num > 0) and (num % 2 == 0) :
    print('C')

elif (num > 0) and (num % 2 == 1) :
    print('D')