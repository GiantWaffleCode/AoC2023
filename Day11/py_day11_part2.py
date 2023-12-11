#   Advent of Code 2023
#      GiantWaffle
#   Challenge 11 of 25
#      Part 2 of 2
# -----------------------

import tqdm

use_real_data = True

data = []

with open('Day11\data_day11.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    '...#......',
    '.......#..',
    '#.........',
    '..........',
    '......#...',
    '.#........',
    '.........#',
    '..........',
    '.......#..',
    '#...#.....'
]

expanded_map = []

if use_real_data:
    test_input = data
else:
    test_input = example

expansion_value = 1000000

for line in test_input:
    expanded_map.append(line)
    if not '#' in line:
        for k in range(expansion_value-1):
            expanded_map.append(line)


no_galaxy = []

for i in range(len(test_input[0])):
    no_galaxy.append(True)

for y, line in enumerate(test_input):
    for x, cell in enumerate(line):
        if cell == '#':
            no_galaxy[x] = False

final_map = []

for line in tqdm.tqdm(expanded_map):
    expansions = 0
    new_line = []
    for point in range(len(no_galaxy)):
        new_line.append(line[point])
        if no_galaxy[point]:
            for k in range(expansion_value-1):
                new_line.append('.')
                expansions += 1
    mod = ''.join(new_line)
    final_map.append(mod)

# for line in expanded_map:
#     print(line)

def calcCartDist(cord1,cord2):
    return abs(cord2[0]-cord1[0]) + abs(cord2[1]-cord1[1])


galaxies = []

for y, line in enumerate(final_map):
    for x, cell in enumerate(line):
        if cell == '#':
            galaxies.append((x,y))

dist_sum = 0
#print(galaxies)
for i in range(len(galaxies)):
    for gal_num, galaxy in enumerate(galaxies):
        if i != gal_num:
            dist = calcCartDist(galaxies[i], galaxy)
            dist_sum += dist

print(f'Part 1 Answer: {dist_sum/2}')