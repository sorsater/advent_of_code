# Answer #1: 8997277

goal_row = 3010
goal_col = 3019

def find():
    code = 20151125
    row = 1
    while True:
        row += 1
        for col in range(1, row + 1):
            code = (code * 252533) % 33554393
            if (row - col + 1) == goal_row and (col == goal_col):
                return code

print('Answer #1:', find())