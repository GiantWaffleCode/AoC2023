#   Advent of Code 2023
#      GiantWaffle
#   Challenge 11 of 25
#      Part 2 of 2
# -----------------------

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

if use_real_data:
    test_input = data
else:
    test_input = example

multi = 1000000
expansion_value = multi-1

no_galaxy = [[],[]]

for x in range(len(test_input[0])): #init list for x
    no_galaxy[0].append(True)

for y in range(len(test_input)):
    no_galaxy[1].append(True)

for y, line in enumerate(test_input):
    for x, cell in enumerate(line):
        if cell == '#':
            no_galaxy[0][x] = False

for y, line in enumerate(test_input):
    if '#' in line:
        no_galaxy[1][y] = False

def calcCartDist(cord1,cord2):
    return abs(cord2[0]-cord1[0]) + abs(cord2[1]-cord1[1])

galaxies = []

for y, line in enumerate(test_input):
    for x, cell in enumerate(line):
        if cell == '#':
            galaxies.append([x,y])

# print(galaxies)

expanded_galaxies = []

x_expansions = 0
for x, x_check in enumerate(no_galaxy[0]):
    if x_check:
        for cord in galaxies:
            if cord[0] > x+(x_expansions*expansion_value):
                cord[0] += expansion_value
        x_expansions += 1

y_expansions = 0
for y, y_check in enumerate(no_galaxy[1]):
    if y_check:
        for cord in galaxies:
            if cord[1] > y+(y_expansions*expansion_value):
                cord[1] += expansion_value
        y_expansions += 1

dist_sum = 0

for i in range(len(galaxies)):
    for gal_num, galaxy in enumerate(galaxies):
        if i != gal_num:
            dist = calcCartDist(galaxies[i], galaxy)
            dist_sum += dist

print(f'Part 2 Answer: {dist_sum/2}')