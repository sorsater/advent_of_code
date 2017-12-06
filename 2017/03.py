# Answer #1: 371
# Answer #2: 369601

goal = 368078   

import math
def part1():
    
    i = math.ceil(math.sqrt(goal))
    if i % 2 == 0:
        i += 1

    # Distance to center
    cen_dist = (i-1) // 2 

    cur_sq = i**2
    prv_sq = (i-2)**2

    # Distance between corners
    diff = (cur_sq - prv_sq) // 4

    # Find the 4 corners
    corners = [cur_sq - diff*i for i in range(5)]

    # Find the elements with a straight line to the center
    mid_corners = [(corners[i] + corners[i+1]) // 2 for i in range(4)]

    # Distance to closest middle element
    mid_dist = min([abs(goal - b) for b in mid_corners])

    return cen_dist + mid_dist

def part2():
    grid = {}
    # Right, Up, Left, Down
    directions = [[1,0], [0,-1], [-1,0], [0,1]]
    grid_directions = directions + [[1,1], [-1,-1], [1,-1], [-1,1]]

    x, y, cnt = 0, 0, 0
    grid['0:0'] = 1
    while True:
        # Walk the spiral
        for i, (_x, _y) in enumerate(directions):
            # Increase length after two turns
            if i % 2 == 0:
                cnt += 1
            # Walk cnt steps
            for j in range(cnt):
                x += _x
                y += _y
               
                # Calculate sum of adjacent numbers
                res = sum([grid.get(str(x + g_x) + ':' + str(y + g_y), 0) for g_x, g_y in grid_directions])
                
                grid[str(x) + ':' + str(y)] = res
                
                if res >= goal:
                    return res

print('Answer #1: {}'.format(part1()))
print('Answer #2: {}'.format(part2()))
