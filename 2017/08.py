# Answer #1: 4647
# Answer #2: 5590

with open('input/08') as f:
    regs = [line.strip().split() for line in f]

# Loop over all unique reg names and create dict
reg_values = {name: 0 for name in list(set([reg[0] for reg in regs]))}

tmp_vals = set()
for reg, i_d, val, _if, new_reg, op, op_val in regs:
    # If expression is true, either increase or decrease
    if eval('reg_values[new_reg] {} int(op_val)'.format(op)):
        reg_values[reg] += int(val) * (1 if i_d == 'inc' else -1)
    tmp_vals.add(reg_values[reg])

print('Answer #1: {}'.format(max([val for val in reg_values.values()])))
print('Answer #2: {}'.format(max(tmp_vals)))
