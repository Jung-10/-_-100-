# [기초-논리연산] 정수 입력받아 참 거짓 평가하기

# bool( ) 을 이용하면 입력된 식이나 값을 평가해 불 형의 값(True 또는 False)을 출력
# 정수값 0은 False(거짓)로 평가되고, 그 외의 값들은 모두 True(참)

num = int(input())

if num == 0 :
    print(bool(num))
else :
    print(bool(num))