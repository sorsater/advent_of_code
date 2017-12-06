# Answer #1: 1606483
# Answer #2: 3842356

import re

re0 = r'(\d+)x(\d+)x(\d+)'

with open('input/02') as f:
    boxes = [[int(a) for a in re.match(re0, line).groups()] for line in f]

def main():
    total_surface, total_ribbon = 0, 0
    for l, w, h in boxes:
        # Paper
        a = l * w
        b = l * h
        c = w * h
        total_surface += 2 * (a + b + c) + min(a, b, c)

        # Ribbon
        total_ribbon += 2 * (l + w + h - max(l, w, h)) + l * w * h

    return total_surface, total_ribbon

paper, ribbon = main()
print('Answer #1:', paper)
print('Answer #2:', ribbon)
