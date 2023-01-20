# [기초-리스트] 이상한 출석 번호 부르기1

# d = [] : 어떤 데이터 목록(list) 을 순서대로 저장하기 위해 아무것도 없는 리스트 변수 만들기
# d.append(값) : d 리스트의 마지막에 원하는 값을 추가(append)해 넣음 
# d[a[i]] += 1 : 2중 리스트 참조 -> 만약 a[i]의 값이 1이었다면? d[1] += 1 이 실행되는 것이다. 1번 카운트 1개 증가

# 'map' object is not subscriptable : map을 사용하면 [0]같은 연산자로는 접근 할 수가 없다
# 따라서, num_call = list(num_call)처럼 []이 사용 가능한 list같은 자료형으로 캐스팅

# 다른 방법으로는
# a = input().split()   => 공백을 기준으로 잘라 a에 순서대로 저장
# for i in range(n) :   => 0부터 n-1까지...
#  a[i] = int(a[i])     => a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장


num = int(input())

num_call = map(int, input().split())

num_call = list(num_call)

d = []

for x in range(24) :
    d.append(0)

for y in range(num) :
    d[num_call[y]] += 1

for z in range(1, 24) :
    print(d[z], end=' ')
