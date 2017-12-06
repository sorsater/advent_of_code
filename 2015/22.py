# Answer #1: 1269
# Answer #2: 1309

from copy import deepcopy
import time
import math

start = time.time()

best_iteration = math.inf

BOSS_HP = 58
BOSS_DAMAGE = 9
MY_HP = 50
MY_MANA = 500

# Duration -1 means immediately
spells = {
    'magic_missile': {'cost': 53, 'damage': 4, 'armor': 0, 'hp': 0, 'mana': 0, 'duration': 0},
    'drain': {'cost': 73, 'damage': 2, 'armor': 0, 'hp': 2, 'mana': 0, 'duration': 0},
    'shield': {'cost': 113, 'damage': 0, 'armor': 7, 'hp': 0, 'mana': 0, 'duration': 6},
    'poison': {'cost': 173, 'damage': 3, 'armor': 0, 'hp': 0, 'mana': 0, 'duration': 6},
    'recharge': {'cost':229, 'damage': 0, 'armor': 0, 'hp': 0, 'mana': 101, 'duration': 5},
}

def take_turn(mana_spent, part2, player_turn, my_mana, my_hp, boss_hp, boss_damage, active_spells):
    my_armor = 0

    global best_iteration

    if mana_spent >= best_iteration:
        return

    print("Best:", best_iteration, end='\r')
    # Cast all spells
    new_active_spells = []
    for i, (spell, counter) in enumerate(active_spells):
        if counter >= 0:
            my_mana += spells[spell]['mana']
            my_armor += spells[spell]['armor']
            my_hp += spells[spell]['hp']
            boss_hp -= spells[spell]['damage']

        if counter > 1:
            new_active_spells.append([spell, counter - 1])

    if boss_hp <= 0:
        best_iteration = mana_spent
        return

    if player_turn:
        if part2:
            my_hp -= 1
            if my_hp <= 0:
                return
        # Cast spells!
        for name, spell in spells.items():
            # Ignore active spells
            for active_spell, iteration in new_active_spells:
                if name == active_spell:
                    break
            else:
                if spell['cost'] < my_mana:
                    tmp_active_spells = deepcopy(new_active_spells)
                    tmp_active_spells.append([name, spell['duration']])

                    take_turn(mana_spent + spell['cost'], part2, not player_turn, my_mana - spell['cost'], my_hp, boss_hp, boss_damage, tmp_active_spells)

    else:
        my_hp -= 1 if boss_damage - my_armor < 1 else boss_damage - my_armor

        if my_hp > 0:
            take_turn(mana_spent, part2, not player_turn, my_mana, my_hp, boss_hp, boss_damage, new_active_spells)

take_turn(0, False, True, MY_MANA, MY_HP, BOSS_HP, BOSS_DAMAGE, [])

answer1 = best_iteration
best_iteration = math.inf
print('Answer #1:', answer1)

take_turn(0, True, True, MY_MANA, MY_HP, BOSS_HP, BOSS_DAMAGE, [])

answer2 = best_iteration
print('Answer #2:', answer2)

print('Time: {0:.2f}'.format(time.time()-start))