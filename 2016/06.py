# Answer #1: asvcbhvg
# Answer #2: odqnikqv
words = []
with open("input/06", 'r') as f:
	for line in f:
		words.append(line.split())

pw1 = ""
pw2 = ""
for i in range(len(words[0][0])):
    tmp = ""
    for w in words:
        w = w[0]
        tmp += w[i]
    best = 0
    worst = tmp.count(tmp[0])
    for c in tmp:
        cnt = tmp.count(c)
        if(cnt > best):
            best = cnt
            char1 = c
        if(cnt < worst):
            worst = cnt
            char2 = c
    pw1 += char1
    pw2 += char2
print("Answer #1:", pw1)
print("Answer #2:",pw2)
