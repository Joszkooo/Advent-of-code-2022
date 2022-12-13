answer = 0

with open('data.txt', 'r') as f:

    first_line = f.readline()
    second_line = f.readline()
    third_line = f.readline()
    while first_line:
        for word in first_line:
            if word in second_line and word in third_line:
                if word.islower():
                    answer += ord(word) - 96
                if word.isupper():
                    answer += ord(word) - 38
                break
        first_line = f.readline()
        second_line = f.readline()
        third_line = f.readline()

print(answer)
# 2817
