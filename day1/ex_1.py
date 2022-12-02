with open('input.txt', 'r') as file:

# FIRST HALF

    line = file.readline()
    dic = {}
    i = 0
    tab = []
    while line:
        if line == '\n':
            line = file.readline()
            dic[f'Elf {i}'] = sum(tab)

            tab = []
            i += 1
        line = line.strip()
        tab.append(int(line))
        line = file.readline()

    answer1 = max(dic.values())

# SECOND HALF

    answer2 = 0
    for _ in range(3):
        value = {i for i in dic if dic[i] == max(dic.values())}
        temp = ''.join(value)
        temp = dic.pop(temp)
        answer2 += temp

print(f'Answer1: {answer1}')
print(f'Answer2: {answer2}')
