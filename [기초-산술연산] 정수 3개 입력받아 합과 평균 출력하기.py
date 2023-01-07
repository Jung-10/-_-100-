# [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기

# 평균은 소숫점 이하 셋째 자리에서 반올림하여 둘째 자리까지 출력

num1, num2, num3 = input().split(' ')

sum = int(num1) + int(num2) + int(num3)

average = sum / 3

print(sum, format(average, '.2f'))