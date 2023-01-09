# [기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기

# 비트단위(bitwise) 연산자
# ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
# <<(bitwise left shift), >>(bitwise right shift)

# ~n = -n - 1 , -n = ~n + 1 

num = int(input())

print(~num)