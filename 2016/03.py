# Answer #1: 1050
# Answer #2: 1921

nrT = 0
with open("input/03", 'r') as f:
	for line in f:
		tmp = []
		for l in line.split():
			tmp.append(int(l))
		if(max(tmp) / sum(tmp) < 0.5):
			nrT	 += 1

print("Answer #1:", nrT)


# Read the triangles
t = []
with open("input/03", 'r') as f:
	for line in f:
		tmp = []
		for l in line.split():
			tmp.append(int(l))
		t.append(tmp)

# Flip them
t_columns = []
for tr in range(0,len(t),3):
	for i in range(0,3):
		t_columns.append([t[tr][i],t[tr+1][i],t[tr+2][i]])

# Count the number of valid triangles
nrT = 0
for i in t_columns:
	if(max(i) / sum(i) < 0.5):
		nrT	 += 1
print("Answer #2:", nrT)


