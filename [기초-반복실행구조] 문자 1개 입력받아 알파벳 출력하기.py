# [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기

# 알파벳 문자 a의 정수값은 ord('a')로 알아낼 수 있음
# chr(정수값)을 이용하면 유니코드 문자로 출력

# print(..., end=' ') 와 같이 작성하면 값 출력 후 공백문자 ' '를 출력
# end='\n'로 작성하거나 생략하면, 값을 출력한 후 마지막(end)에 줄바꿈(newline)

ord_num = ord(input())

ord_a = ord('a')

while ord_a <= ord_num :
    print(chr(ord_a), end=' ')
    ord_a += 1