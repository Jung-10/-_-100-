# [기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기

num1, num2 = input().split(' ')

num1 = float(num1)
num2 = float(num2)

num = num1 / num2

print(format(num, ".3f")) #소숫점 넷째자리에서 반올림