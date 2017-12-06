# Answer #1: 317993
# Answer #2: 9227647
import time

cmds = []
with open("input/12", 'r') as f:
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
			if(key != 0):
				i += int(cmd[2]) - 1

		elif(cmd[0] == 'cpy'):
			val = cmd[1]
			key = cmd[2]
			if val in 'abcd':
				reg[key] = reg[val]
			else:
				reg[key] = int(val)

		i += 1
		if(c%1000 == 0):
			print("Time: {0:.1f}".format(time.time()-start), end="\r")
		c += 1

# Part 1
set_regs(0,0,0,0)
main()
print("Answer #1:", reg['a'])

# Part 2
set_regs(0,0,1,0)
main()
print("Answer #2:", reg['a'])
