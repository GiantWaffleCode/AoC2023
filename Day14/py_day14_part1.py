#   Advent of Code 2023
#      GiantWaffle
#   Challenge 14 of 25
#      Part 1 of 2
# -----------------------

use_real_data = False

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
    shifted_map = map.copy()
    for i in range(len(shifted_map)-1):
        for cell_index, cell in enumerate(shifted_map[i+1]):
            if cell == 'O' and shifted_map[i][cell_index] == '.':
                shifted_map[i] = shifted_map[i][:cell_index] + '.' + shifted_map[i][cell_index+1:]
                cell = '.'
    return shifted_map

new_map = shift_up_once(starting_map)

for line in new_map:
    print(line)


# def tilt_north(map):
#     pre_tilted_map = map.copy()
#     for i in range(len(pre_tilted_map)-1):

#     return tilted_map


def calc_north_load(source_map):
    load = 0
    return load

source_map = []

# new_map = tilt_north(starting_map)
# north_load = calc_north_load(new_map)

# print(f'Part 1 Answer: {north_load}')

