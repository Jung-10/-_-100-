# [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기

a, b = input().split(' ')

x = bool(int(a))
y = bool(int(b))

print((x and y) or (not x and not y))