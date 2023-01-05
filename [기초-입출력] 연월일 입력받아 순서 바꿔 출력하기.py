# [기초-입출력] 연월일 입력받아 순서 바꿔 출력하기

year, month, date = input().split(".")

print("{}-{}-{}".format(date, month, year))