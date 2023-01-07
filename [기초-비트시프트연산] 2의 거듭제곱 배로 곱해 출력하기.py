# [기초-비트시프트연산] 2의 거듭제곱 배로 곱해 출력하기

num1, num2 = input().split(' ')

num1 = int(num1)
num2 = int(num2)

num = num1 << num2

print(num)