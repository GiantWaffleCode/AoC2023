#   Advent of Code 2023
#      GiantWaffle
#   Challenge 18 of 25
#      Part 2 of 2
# -----------------------

import copy
import sys

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
    
new_instructions = []

for ins in instructions:
    size = ins[2][:-1]
    new_size = int(size, 16)
    direction = int(ins[2][5:])
    new_dir = ''
    match direction:
        case 0:
            new_dir = 'R'
        case 1:
            new_dir = 'D'
        case 2:
            new_dir = 'L'
        case 3:
            new_dir = 'U'
    new_ins = [new_dir, new_size]
    #print(new_ins)
    new_instructions.append(new_ins)

# print(instructions)
# print('')
# print(new_instructions)

instructions=new_instructions

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


new_grid = copy.deepcopy(grid)
pos = starting_pos

for ins in instructions:
    new_grid, pos = follow_instruction(new_grid, (ins[0], ins[1]), pos)
    #draw_grid(new_grid)


#TODO: Rewrite this

def is_one(grid, row, col):
    '''
    Helper method for checking whether the pixel belongs to an island or not
    '''
    if (row < 0 or row > len(grid) - 1):
        return False

    if (col < 0 or col > len(grid[0]) - 1):
        return False

    if grid[row][col] == '.':
        return True
    else:
        return False

def iterative_flood_fill(grid, row, col):
    '''
    Iterative version of flood fill algorithm. Works better for larger maps.
    '''
    if (row < 0 or row > len(grid) - 1):
        return 'Return 1'

    if (col < 0 or col > len(grid[0]) - 1):
        return 'Return 2'

    if (grid[row][col] != '.'):
        return 'Return 3'

    q = []  # init empty queue (FIFO)
    grid[row][col] = '#'  # mark as visited
    q.append([row, col])  # add to queue

    while len(q) > 0:
        [cur_row, cur_col] = q[0]
        del q[0]

        if (is_one(grid, cur_row - 1, cur_col) == True):
            grid[cur_row - 1][cur_col] = '#'
            q.append([cur_row - 1, cur_col])

        if (is_one(grid, cur_row + 1, cur_col) == True):
            grid[cur_row + 1][cur_col] = '#'
            q.append([cur_row + 1, cur_col])

        if (is_one(grid, cur_row, cur_col - 1) == True):
            grid[cur_row][cur_col - 1] = '#'
            q.append([cur_row, cur_col - 1])

        if (is_one(grid, cur_row, cur_col + 1) == True):
            grid[cur_row][cur_col + 1] = '#'
            q.append([cur_row, cur_col + 1])

    return grid


start_x = 200
start_y = 100

#draw_grid(new_grid)
filled_grid = iterative_flood_fill(new_grid, start_y, start_x)
print('')
#print(filled_grid)
#draw_grid(filled_grid)


total_filled = 0

for line in filled_grid:
    total_filled += line.count('#')

print(f'Total Filled: {total_filled}')