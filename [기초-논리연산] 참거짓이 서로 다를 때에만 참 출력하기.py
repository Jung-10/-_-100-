# [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기

# 참 거짓이 서로 다를 때에만 True 로 계산하는 논리연산을 XOR(exclusive or, 배타적 논리합) 연산

a, b = input().split(' ')

x = bool(int(a))
y = bool(int(b))

print((x and not y) or (not x and y))