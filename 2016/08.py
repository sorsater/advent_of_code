# Answer #1: 115
# Answer #2: EFEYKFRFIJ
width = 50
height = 6

# Create grid
grid = []
for i in range(height):
	tmp = []
	for j in range(width):
		tmp.append(' ')
	grid.append(tmp)

# Save the commands
cmd = []
with open("input/08", 'r') as f:
	for line in f:
		cmd.append(line.split())

for c in cmd:
	if(c[0] == "rect"):
		idx = c[1].index('x')
		x = int(c[1][:idx])
		y = int(c[1][idx+1:])
		for i in range(y):
			for j in range(x):
				grid[i][j] = '#'
	elif(c[0] == "rotate"):
		rc = int(c[2][2:])
		val = int(c[4])
		if(c[1] == "column"):
			for v in range(val):
				tmp = grid[height-1][rc]
				for i in range(height-1,0,-1):
					grid[i][rc] = grid[i-1][rc]
				grid[0][rc] = tmp
		elif(c[1] == "row"):
			for i in range(val):
				grid[rc] = [grid[rc][-1]] + grid[rc][0:-1]

# Count the number of ones
c = 0
for i in range(height):
	for j in range(width):
		if(grid[i][j] == '#'):
			c += 1
print("Answer #1: Count:",c)


# Part two
print("Answer #2")
letters = int(width / 5)
msg = []
for i in range(height):
	msg.append('')

for i in range(letters):
	for j in range(height):
		tmp = ""
		#print()
		tmp += str(grid[j][i*5])
		tmp += str(grid[j][i*5+1])
		tmp += str(grid[j][i*5+2])
		tmp += str(grid[j][i*5+3])
		tmp += str(grid[j][i*5+4])
		msg[j] = str(msg[j]) + tmp

for char in msg:
	print(char)


