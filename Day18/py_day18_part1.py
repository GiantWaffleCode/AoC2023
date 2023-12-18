#   Advent of Code 2023
#      GiantWaffle
#   Challenge 17 of 25
#      Part 1 of 2
# -----------------------

import copy

use_real_data = False
data = []

with open('Day18\data_day18.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    'R 6 (#70c710)',
    'D 5 (#0dc571)',
    'L 2 (#5713f0)',
    'D 2 (#d2c081)',
    'R 2 (#59c680)',
    'D 2 (#411b91)',
    'L 5 (#8ceee2)',
    'U 2 (#caa173)',
    'L 1 (#1b58a2)',
    'U 2 (#caa171)',
    'R 2 (#7807d2)',
    'U 3 (#a77fa3)',
    'L 2 (#015232)',
    'U 2 (#7a21e3)'
]

passed_test = [
    '#######',
    '#######',
    '#######',
    '..#####',
    '..#####',
    '#######',
    '#####..',
    '#######',
    '.######',
    '.######'
]


if use_real_data:
    test_input = data
else:
    test_input = example

instructions = []

for line in test_input:
    split_line = line.split()
    instruction = [
        split_line[0],
        int(split_line[1]),
        split_line[2][2:-1]
            ]
    instructions.append(instruction)

# for line in instructions:
#     print(line)

right_count = 0
max_right = 0
min_right = 0
down_count = 0
max_down = 0
min_down = 0

for ins in instructions:
    match ins[0]:
        case 'R':
            right_count += ins[1]
            max_right = max(max_right, right_count)
            min_right = min(min_right, right_count)
        case 'L':
            right_count -= ins[1]
            max_right = max(max_right, right_count)
            min_right = min(min_right, right_count)
        case 'U':
            down_count -= ins[1]
            max_down = max(max_down, down_count)
            min_down = min(min_down, down_count)
        case 'D':
            down_count += ins[1]
            max_down = max(max_down, down_count)
            min_down = min(min_down, down_count)

grid_size = [max_right-min_right, max_down-min_down]

print(f'Right - Min: {min_right} | Max: {max_right} | Total: {grid_size[0]}')
print(f'Down - Min: {min_down} | Max: {max_down} | Total: {grid_size[1]}')

starting_pos = (abs(min_right), abs(min_down))

print(f'Starting Pos: {starting_pos}')


def gen_grid(x,y):
    grid = []
    for col in range(y+1):
        line = ['.']*(x+1)
        grid.append(line)
    return grid

grid = gen_grid(grid_size[0], grid_size[1]) #make grid from determined size

grid[starting_pos[1]][starting_pos[0]] = '#'

def draw_grid(grid):
    for line in grid:
        new_line = ''.join(line)
        print(new_line)

def follow_instruction(grid, instruction: (str, int), pos: (int, int)):
    ins_dir, ins_len = instruction
    pos_x, pos_y = pos

    match ins_dir:
        case 'R':
            line = grid[pos_y]
            for i in range(ins_len):
                line[pos_x+i+1] = '#'
            pos_x += ins_len
        case 'L':
            line = grid[pos_y]
            for i in range(ins_len):
                line[pos_x-i-1] = '#'
            pos_x -= ins_len
        case 'U':
            for i in range(ins_len):
                grid[pos_y-i-1][pos_x] = '#'
            pos_y -= ins_len
        case 'D':
            for i in range(ins_len):
                grid[pos_y+i+1][pos_x] = '#'
            pos_y += ins_len

    return grid, (pos_x, pos_y)

# draw_grid(grid)
# ins = instructions[0]
# #print(f'{(ins[0], ins[1])}')
# new_grid = follow_instruction(grid, ('D', 4), (0,0))
# print('')
# draw_grid(new_grid[0])
# print(f'New Pos: {new_grid[1]}')

new_grid = copy.deepcopy(grid)
pos = starting_pos

for ins in instructions:
    new_grid, pos = follow_instruction(new_grid, (ins[0], ins[1]), pos)
    #draw_grid(new_grid)


draw_grid(new_grid)