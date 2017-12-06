# Answer #1: 91
# Answer #2: 158

import itertools

weapons = {
    'Dagger':       [8, 4, 0],
    'Shortsword':   [10, 5, 0],
    'Warhammer':    [25, 6, 0],
    'Longsword':    [40, 7, 0],
    'Greataxe':     [74, 8, 0],
}

armors = {
    'Leather':      [13, 0, 1],
    'Chainmail':    [31, 0, 2],
    'Splintmail':   [53, 0, 3],
    'Bandedmail':   [75, 0, 4],
    'Platemail':    [102, 0, 5],
}

rings = {
    'Damage+1':    [25, 1, 0],
    'Damage+2':    [50, 2, 0],
    'Damage+3':    [100, 3, 0],
    'Defense+1':   [20, 0, 1],
    'Defense+2':   [40, 0, 2],
    'Defense+3':   [80, 0, 3],
}

# All items
inventory = dict(list(weapons.items()) + list(armors.items()) + list(rings.items()))

def try_stats(me):
    boss = {
        'hp': 100,
        'damage': 8,
        'armor': 2,
    }
    my_turn = True
    attacker = me
    defender = boss
    while True:
        defender['hp'] -= max(1, attacker['damage'] - defender['armor'])
        if defender['hp'] <= 0:
            return my_turn

        attacker, defender = defender, attacker
        my_turn = not my_turn


# Create all combinations
w = list(weapons.keys())
a = list(armors.keys()) + [[]]
r = [list(ring) for cnt in [0,1,2] for ring in itertools.combinations(list(rings.keys()), cnt)]

kits = [comb for comb in itertools.product(w, a, r)]

winners = []
losers = []

for kit in kits:
    specs = []
    for item in kit:
        if isinstance(item, list):
            for subitem in item:
                specs.append(inventory[subitem])
        else:
            specs.append(inventory[item])

    cost = sum([item[0] for item in specs])
    damage = sum([item[1] for item in specs])
    armor = sum([item[2] for item in specs])

    me = {
        'hp': 100,
        'damage': damage,
        'armor': armor,
    }

    if try_stats(me):
        winners.append(cost)
    else:
        losers.append(cost)

print('Answer #1:', min(winners))
print('Answer #2:', max(losers))