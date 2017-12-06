# Answer #1: 2655
# Answer #2: 1059

import re

seconds = 2503
pattern = r'(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds.'

reindeers = {}
with open('input/14') as f:
  for line in f:
      match = re.match(pattern, line)
      if match:
          name, speed, fly_time, rest_time = match.groups()
          reindeers[name] = {
            'speed': int(speed),
            'fly_time': int(fly_time),
            'rest_time': int(rest_time),
            'distance': 0,
            'points': 0,
            'fly': True,
            'cur_time': 0,
          }

# For each reindeer, update timers and switch mode if needed
for s in range(seconds):
    scores = []
    for key, value in reindeers.items():
        # Toggle state if time is up
        if value['cur_time'] == value['fly_time' if value['fly'] else 'rest_time']:
            value['cur_time'] = 0
            value['fly'] = not value['fly']

        # Update distance
        if value['fly']:
            value['distance'] += value['speed']

        value['cur_time'] += 1
        scores.append(value['distance'])

    # Part 2, give points to leading reindeer
    for value in reindeers.values():
        if value['distance'] == max(scores):
            value['points'] += 1

distances = [value['distance'] for value in reindeers.values()]
points = [value['points'] for value in reindeers.values()]

print('Answer #1:', max(distances))
print('Answer #2:', max(points))
