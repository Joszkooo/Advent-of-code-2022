answer = 0
with open('data.txt', 'r') as file:
    line = file.readline()

    while line:
        # slicing first and second half of text
        fist_part = slice(0, len(line) // 2)
        second_part = slice(len(line) // 2, len(line))

        # taking half of text and attributing to variable
        first = line[fist_part]
        second = line[second_part]

        for word in first:
            if word in second:
                if word.islower():
                    answer += ord(word) - 96
                if word.isupper():
                    answer += ord(word) - 38
                break
        line = file.readline()
print(f'ilosc punktow: {answer}')

# 8185
