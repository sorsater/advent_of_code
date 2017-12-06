# Answer #1: 36629
# Answer #2: 99C3D

com = []
with open("input/02") as f:
	for line in f:
		com.append(line.split()[0])

def part1():
	x,y = 1,1

	res = ""
	for c in com:
		for l in c:
			if(l == 'U'):
				if(y > 0):
					y -= 1
			elif(l == 'D'):
				if(y < 2):
					y += 1
			elif(l == 'L'):
				if(x > 0):
					x -= 1
			elif(l == 'R'):
				if(x < 2):
					x += 1

		res += str(y*3 + x +1)
	return res

def part2():
	x,y = 1,3

	pos = [
	[0,0,0,0,0,0,0],
	[0,0,0,1,0,0,0],
	[0,0,2,3,4,0,0],
	[0,5,6,7,8,9,0],
	[0,0,'A','B','C',0,0],
	[0,0,0,'D',0,0,0],
	[0,0,0,0,0,0,0]
	]

	res = ""
	for c in com:
		for l in c:
			if(l == 'U'):
				if(pos[y-1][x] != 0):
					y -= 1
			elif(l == 'D'):
				if(pos[y+1][x] != 0):
					y += 1
			elif(l == 'L'):
				if(pos[y][x-1] != 0):
					x -= 1
			elif(l == 'R'):
				if(pos[y][x+1] != 0):
					x += 1
		res += str(pos[y][x])
	return res
print("Answer #1:", part1())
print("Answer #2:", part2())
