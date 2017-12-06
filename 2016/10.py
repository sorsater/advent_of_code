# Answer #1: 93
# Answer #2: 47101
import re

re0 = r'value (\d+) goes to bot (\d+)'
re1 = r'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)'

# Key is bots, value is microchip
bots_val = {}
# Key is value, value is bot
values = {}
# Instructions for the bots
bots_instr = {}

# Helpmethod for adding values
def add_arg_dict(arg):
	add_key_val_dict('bot-' + arg[1], int(arg[0]))

# Add value to bot
# Add bots to values
def add_key_val_dict(bot, val):
	if not bot in bots_val:
		bots_val[bot] = [val]
	else:
		bots_val[bot].append(val)
	if not val in values:
		values[val] = [bot]
	else:
		values[val].append(bot)

# Add instructions for the different bots
def add_instr_dict(arg):
	bot = 'bot-' + arg[0]
	low = arg[1] + '-' + arg[2]
	high = arg[3] + '-' + arg[4]

	if not bot in bots_instr:
		bots_instr[bot] = [low, high]
	else:
		bots_instr[bot].append([low, high])

regFunc = {
	re0: add_arg_dict,
	re1: add_instr_dict
}

# Add the values and instructions to the dictionaries
with open("input/10", 'r') as f:
	for line in f:
		for regex, func in regFunc.items():
			match = re.match(regex, line)
			if(match):
				func(match.groups())

# Execute the instruction for the first bot with two values
def exec_next_instr():
	for bot in bots_val:
		if(len(bots_val[bot]) == 2):

			low_bot = bots_instr[bot][0]
			high_bot = bots_instr[bot][1]

			values = bots_val[bot]
			low_val = min(values)
			high_val = max(values)

			add_key_val_dict(low_bot, low_val)
			add_key_val_dict(high_bot, high_val)

			del bots_val[bot]
			return True

	return False

# Execute the instructions
while exec_next_instr():
	pass

# Part 1
res = ""
for i in values[61]:
	for j in values[17]:
		if(i == j):
			# Ignore "bot-" part
			res += i[4:]

print("Answer #1:", res)


# Part 2
out_0 = bots_val['output-0'][0]
out_1 = bots_val['output-1'][0]
out_2 = bots_val['output-2'][0]

print("Answer #2:", out_0*out_1*out_2)
