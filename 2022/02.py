data = open("02.input").read().splitlines()

score_map = {
    "A X": 3 + 1,
    "A Y": 6 + 2,
    "A Z": 0 + 3, 
    "B X": 0 + 1, 
    "B Y": 3 + 2, 
    "B Z": 6 + 3, 
    "C X": 6 + 1, 
    "C Y": 0 + 2,
    "C Z": 3 + 3,
}

pick_move_map = {
    "Y": { # draw
        "A": "X",
        "B": "Y",
        "C": "Z",
    },
    "Z": { # win
        "A": "Y",
        "B": "Z",
        "C": "X",
    },
    "X": { # lose
        "A": "Z",
        "B": "X",
        "C": "Y",
    }
}

part1 = sum(list(map(lambda x: score_map[x], data)))
print(part1)

def part2_one(line):
    my_move = pick_move_map[line[2]][line[0]]
    return score_map[f"{line[0]} {my_move}"]

part2 = sum(list(map(lambda x: part2_one(x), data)))
print(part2)
