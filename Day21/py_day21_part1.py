#   Advent of Code 2023
#      GiantWaffle
#   Challenge 21 of 25
#      Part 1 of 2
# -----------------------
from collections import deque
from tqdm import tqdm

use_real_data = True
data = []

with open('Day21\data_day21.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
'...........',
'.....###.#.',
'.###.##..#.',
'..#.#...#..',
'....#.#....',
'.##..S####.',
'.##..#...#.',
'.......##..',
'.##.#.####.',
'.##..##.##.',
'...........',
]

starting_point = (int, int)

if use_real_data:
    test_input = data
else:
    test_input = example



#Hashmap of grid
grid = {}

for row, line in enumerate(test_input):
    str_list = [*line]
    for col, item in enumerate(str_list):
        if item == 'S':
            starting_point = (row, col)

        grid[(row, col)] = item


def find_neighbors(cell):
    row, col = cell
    neighbors = []

    down = grid.get((row+1, col))
    if down == '.' or down == 'S':
        neighbors.append((row+1, col))

    up = grid.get((row-1, col))
    if up  == '.' or up == 'S':
        neighbors.append((row-1, col))

    right = grid.get((row, col+1))
    if right  == '.' or right == 'S':
        neighbors.append((row, col+1))

    left = grid.get((row, col-1))
    if left  == '.' or left == 'S':
        neighbors.append((row, col-1))

    return neighbors
    
q = deque()

#add starting point to queue
q.append(starting_point)

CYCLES = 64

for cycle in tqdm(range(CYCLES)):
    all_neighbors = []
    #print(q)
    #step through queue
    #grab location
    #go to each neighbor and add to next queue
    #remove location from queue
    #repeat till empty queue
    #somehow get rid of duplicate cells in next queue
    #repeat for x cycles
    while q:
        point = q.popleft()
        neighbors = find_neighbors(point)
        for n in neighbors:
            all_neighbors.append(n)
    
    all_neighbors = list(set(all_neighbors))

    for item in all_neighbors:
        q.append(item)

print(f'Part 1 Answer: {len(q)}')


