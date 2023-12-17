#   Advent of Code 2023
#      GiantWaffle
#   Challenge 17 of 25
#      Part 1 of 2
# -----------------------

from dataclasses import dataclass

use_real_data = False
data = []

with open('Day17\data_day17.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    '2413432311323',
    '3215453535623',
    '3255245654254',
    '3446585845452',
    '4546657867536',
    '1438598798454',
    '4457876987766',
    '3637877979653',
    '4654967986887',
    '4564679986453',
    '1224686865563',
    '2546548887735',
    '4322674655533'
]


if use_real_data:
    test_input = data
else:
    test_input = example


#create weight grid
grid = []

for line in test_input:
    sep = list(map(int, [x for x in line]))
    grid.append(sep)

for line in grid:
    print(line)