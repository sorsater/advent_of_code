# Answer #1: 21367368
# Answer #2: 1766400

import re
from itertools import product
from functools import reduce

pattern = r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)'
parameters = ['capacity', 'durability', 'flavor', 'texture', 'calories']

ingredients = {}
with open('input/15') as f:
    for idx, line in enumerate(f):
        match = re.match(pattern, line)
        if match:
            name, capacity, durability, flavor, texture, calories = match.groups()
            ingredients[idx] = {
                'capacity': int(capacity),
                'durability': int(durability),
                'flavor': int(flavor),
                'texture': int(texture),
                'calories': int(calories),
            }

valid_combinations = []
prev = -1
for comb in product([i for i in range(0, 101)], repeat=len(ingredients)):
    if sum(comb) == 100:
        valid_combinations.append(comb)
        if comb[0] != prev:
            print('Progess: {} %'.format(comb[0]), end='\r')
            prev = comb[0]

scores_part1 = []
scores_part2 = []
for comb in valid_combinations:
    tmp_score_list = []
    for i, parameter in enumerate(parameters):
        p_score = 0
        for key, val in ingredients.items():
            p_score += val[parameter] * comb[key]
        # Will multiply to zero, no need to continue
        if p_score <= 0:
            break
        tmp_score_list.append(p_score)
    else:
        # Multiply all values together
        tmp_score = reduce(lambda x, y: x * y, tmp_score_list[:-1])
        scores_part1.append(tmp_score)

        # Check for calories
        if tmp_score_list[-1] == 500:
            scores_part2.append(tmp_score)

print('Answer #1:', max(scores_part1))
print('Answer #2:', max(scores_part2))