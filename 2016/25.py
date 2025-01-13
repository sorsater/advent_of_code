# Answer #1: 189

cmds = []
with open("input/25", 'r') as f:
	for line in f:
		cmds.append(line.split())

reg = {}
def set_regs(a, b, c, d):
	reg['a'] = a
	reg['b'] = b
	reg['c'] = c
	reg['d'] = d

def main():
	print("Answer #1: ", reg['a'], end="\r")
	cur_idx = False
	i = 0
	while i < len(cmds):
		cmd = cmds[i]
		if(cmd[0] == 'inc'):
			reg[cmd[1]] += 1

		elif(cmd[0] == 'dec'):
			reg[cmd[1]] -= 1

		elif(cmd[0] == 'jnz'):
			key = cmd[1]
			if key in 'abcd':
				key = reg[key]
			else:
				key = int(key)
			if cmd[2] in 'abcd':
				val = reg[cmd[2]]
			else:
				val = int(cmd[2])
			if(key != 0):
				i += val - 1

		elif(cmd[0] == 'cpy'):
			val = cmd[1]
			key = cmd[2]
			if key in reg:
				if val in 'abcd':
					reg[key] = reg[val]
				else:
					reg[key] = int(val)

		elif (cmd[0] == 'tgl'):
			key = cmd[1]
			if(0 <= i+reg[key] < len(cmds)):
				cmd_mod = cmds[i+reg[key]]
				# one-argument
				if len(cmd_mod) == 2:
					if (cmd_mod[0] == 'inc'):
						cmds[i+reg[key]][0] = 'dec'
					else:
						cmds[i+reg[key]][0] = 'inc'
				# two-argument
				else:
					if (cmd_mod[0] == 'jnz'):
						cmds[i+reg[key]][0] = 'cpy'
					else:
						cmds[i+reg[key]][0] = 'jnz'

		elif (cmd[0] == 'out'):
			key = cmd[1]
			if key in reg:
				res = reg[key]
			else:
				res = key
			if int(cur_idx) != res:
				return False
			cur_idx = not cur_idx

		i += 1

cmds_backup = [x[:] for x in cmds]
a = 0
while True:
	set_regs(a, 0, 0, 0)
	cmds = [x[:] for x in cmds_backup]
	main()
	a += 1
