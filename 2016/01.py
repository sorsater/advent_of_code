# Answer #1: 300
# Answer #2: 159
commands = []
with open("input/01", 'r') as f:
	for line in f:
		commands.append(line.replace(" ","").split(","))

d = 0
# 0 = north
# 1 = east
# 2 = south
# 3 = west
x = 0
y = 0

visited = [[x,y]]

positionVisited = 0
bestValue = 0

def checkPos(x,y,dx,dy,l):
	global positionVisited
	global bestValue
	if(positionVisited == 0):
		for i in range(1,l+1):
			if([x+i*dx,y+i*dy] in visited):
				positionVisited = 1
				bestValue = abs(x+i*dx) + abs(y+i*dy)
			visited.append([x+i*dx,y+i*dy])

for c in commands[0]:
	if(c[0] == "R"):
		d += 1
	else:
		d -= 1
	d = d%4

	l = int(c[1:])
	if(d == 0):
		checkPos(x,y,0,-1,l)
		y -= l
	if(d == 1):
		checkPos(x,y,1,0,l)
		x += l
	if(d == 2):
		checkPos(x,y,0,1,l)
		y += l
	if(d == 3):
		checkPos(x,y,-1,0,l)
		x -= l

print("Answer #1:", abs(x)+abs(y))
print("Answer #2:", bestValue)





