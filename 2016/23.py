# Answer #1: 11640
# Answer #2: 479008200

tal = 479008200
import time

cmds = []
with open("input/23", 'r') as f:
	for line in f:
		cmds.append(line.split())

reg = {}

def set_regs(a, b, c, d):
	reg['a'] = a
	reg['b'] = b
	reg['c'] = c
	reg['d'] = d

def main():
	i = 0
	c = 0
	start = time.time()
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

		i += 1
		# Keep track of time
		if(c%1000 == 0):
			print("Reg: {0:.4f} Time: {1:.1f}".format(100*reg['a']/tal, time.time()-start), end="\r")
		c += 1

cmds_backup = [x[:] for x in cmds]
# Part 1
set_regs(7,0,0,0)
main()
print()
print()
print("Answer #1:", reg['a'])

cmds = [x[:] for x in cmds_backup]

# Part 2
set_regs(12,0,0,0)
main()
print()
print()
print("Answer #2:", reg['a'])