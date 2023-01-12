# [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기1

num = int(input())

while num != 0 :
    
    if num == 0 :
        break
    else :
        print(num)
        num = num -1