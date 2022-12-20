
data = open("03.input").read().splitlines()

def part1_one(line):
    ll = len(line)
    part1, part2 = line[:ll//2], line[ll//2:]
    intersect = set(part1) & set(part2)
    char = list(intersect)[0]
    return ord(char) - 38 if char.isupper() else ord(char) - 96

res = list(map(part1_one, data))
print(sum(res))

def part2(three_lines):
    intersect = set(three_lines[0]) & set(three_lines[1]) & set(three_lines[2])
    char = list(intersect)[0]
    return ord(char) - 38 if char.isupper() else ord(char) - 96

start = 0
res_part2 = []
while True:
    res_part2.append(part2(data[start:start + 3]))
    start += 3
    if start + 3 > len(data):
        break
print(sum(res_part2))
