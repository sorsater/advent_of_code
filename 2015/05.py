# Answer #1: 238
# Answer #2: 69

with open('input/05') as f:
    strings = [line.split()[0] for line in f]

def classify_string_1(string):
    vow_cnt = 0
    for vowel in 'aeiou':
        vow_cnt += string.count(vowel)

    if vow_cnt < 3:
        return False

    for part in ['ab', 'cd', 'pq', 'xy']:
        if part in string:
            return False

    for i in range(1, len(string)):
        if string[i-1] == string[i]:
            break
    else:
        return False

    return True

def classify_string_2(string):
    for i in range(2, len(string)):
        if string[i-2] == string[i]:
            break
    else:
        return False

    for i in range(1, len(string)):
        pair = string[i-1] + string[i]
        if pair in string[:i-1]:
            break
    else:
        return False

    return True

result_1 = []
result_2 = []
for string in strings:
    result_1.append(classify_string_1(string))
    result_2.append(classify_string_2(string))

print('Answer #1:', sum(result_1))
print('Answer #1:', sum(result_2))

