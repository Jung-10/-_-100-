# [기초-조건/선택실행구조] 월 입력받아 계절 출력하기

num = int(input())

if num // 3 == 1 :
    print('spring')

elif num // 3 == 2 :
    print('summer')

elif num // 3 == 3 :
    print('fall')

else :
    print('winter')