#t를 찾아라

input = input()

sum = 0

for input_split in range(0, len(input)):
    if input[input_split] == "t":
        sum += 1


print(sum)