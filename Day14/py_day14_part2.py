#   Advent of Code 2023
#      GiantWaffle
#   Challenge 14 of 25
#      Part 2 of 2
# -----------------------

from tqdm import tqdm


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

def rotate_matrix(matrix):
    rm = list(zip(*matrix[::-1]))
    new_matrix = []
    for line in rm:
        line_str = ''.join(line)
        new_matrix.append(line_str)
    return new_matrix


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


# cycles = 1000000000
cycles = 1000



spin_map = starting_map.copy()

load_history = []
pattern = [90788, 90795, 90785, 90787, 90781, 90790, 90784, 90796, 90794, 90795, 90788, 90792, 90780, 90788, 90783, 90791, 90789, 90801]
pattern_cycle_start = 0

for count in tqdm(range(cycles)):
    for r in range(4):
        spin_map = tilt_north(spin_map)
        spin_map = rotate_matrix(spin_map)
    north_load = calc_north_load(spin_map)
    if len(load_history) > len(pattern)-1 :
        load_history.pop(0)
    load_history.append(north_load)
    if load_history == pattern:
        pattern_cycle_start = count
        break

print(load_history)
print(pattern_cycle_start)
print(f'Part 2 Answer: {load_history[0]}')


#very very very hacky solution
rem = (1000000000-144) % len(pattern)
print(rem)
print(pattern[rem])