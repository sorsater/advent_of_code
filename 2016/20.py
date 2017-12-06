# Answer #1: 14975795
# Answer #2: 101

with open("input/20", "r") as f:
	ips = [[int(x) for x in line.split()[0].split('-')] for line in f]

# Python is kind and sorts on first element
ips.sort()

valids = []
curr_best = 0
for ip in ips:
	if curr_best < ip[0]:
		valids.append(curr_best)

	if(ip[1] > curr_best):
		curr_best = ip[1] + 1

print("Answer #1:", valids[0])
print("Answer #2:", len(valids))
