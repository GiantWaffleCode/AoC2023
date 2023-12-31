#   Advent of Code 2023
#      GiantWaffle
#   Challenge 14 of 25
#      Part 1 of 2
# -----------------------

use_real_data = True

data = []

with open('Day14\data_day14.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    'O....#....',
    'O.OO#....#',
    '.....##...',
    'OO.#O....O',
    '.O.....O#.',
    'O.#..O.#.#',
    '..O..#O..O',
    '.......O..',
    '#....###..',
    '#OO..#....'
    ]


if use_real_data:
    test_input = data
else:
    test_input = example


starting_map = [] #starting map of rocks

for line in test_input:
    starting_map.append(line)


def shift_up_once(map):
    s = map.copy()
    for i in range(len(s)-1):
        for index, cell in enumerate(s[i+1]):
            if cell == 'O' and s[i][index] == '.':
                s[i] = s[i][:index] + 'O' + s[i][index+1:]
                s[i+1] = s[i+1][:index] + '.' + s[i+1][index+1:]
    return s


def tilt_north(map):
    p = map.copy()
    for i in range(len(p)-1):
        p = shift_up_once(p)
    return p


def calc_north_load(map):
    total_lines = len(map)
    load = 0
    for i, line in enumerate(map):
        line_load = line.count('O') * (total_lines - i)
        load += line_load
    return load


tilted_map = tilt_north(starting_map)
north_load = calc_north_load(tilted_map)

print(f'Part 1 Answer: {north_load}')

