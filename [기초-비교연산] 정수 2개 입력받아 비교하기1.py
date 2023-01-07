# [기초-비교연산] 정수 2개 입력받아 비교하기1

# 비교/관계연산자 : <, >, <=, >=, ==(같다), !=(다르다)
# 결과를 True(참), 또는 False(거짓)로 계산해 주는 연산자

a, b = input().split(' ')

if int(a) < int(b) :
    print('True')
else :
    print('False')