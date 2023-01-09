# [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기

# 예) (a if a>b else b) if ((a if a>b else b)>c) else c와 같은 계산식은 a, b, c 의 값 중 가장 큰 값으로 계산

num1, num2, num3 = input().split(' ')

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

cal = (num1 if num1 < num2 else num2) if ((num1 if num1 < num2 else num2) < num3) else num3

print(cal)