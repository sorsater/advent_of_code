import re
from collections import defaultdict

data = open("02.input").read()

raw_crates, raw_instructions = data.split("\n\n")

crates = defaultdict(list)
crate_pattern = r"\[\w\]"
for line in raw_crates.splitlines()[::-1][1:]:
    for match in re.finditer(crate_pattern, line):
        crates[match.regs[0][0] // 4 + 1].append(match.group().replace("[", "").replace("]", ""))

instr_re = r".*(\d+).*(\d+).*(\d+)"

instructions = []
for instr in raw_instructions.splitlines():
    match = re.match(instr_re, instr)
    num, from_, to = list(map(int, match.groups()))
    instructions.append([num, from_, to])

for instr in instructions:
    num, from_, to = instr
    pickup = crates[from_][-num:][::-1]
    x = 1
    crates[from_] = crates[from_][:-num]
    crates[to].extend(pickup)
    d = 1

print(crates)

for key in sorted(crates.keys()):
    # print(key)
    try:
        print(crates[key][-1])
    except:
        print()


