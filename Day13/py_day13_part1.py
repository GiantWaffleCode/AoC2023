#   Advent of Code 2023
#      GiantWaffle
#   Challenge 13 of 25
#      Part 1 of 2
# -----------------------

use_real_data = True

data = []

with open('Day13\data_day13.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
'#.##..##.',
'..#.##.#.',
'##......#',
'##......#',
'..#.##.#.',
'..##..##.',
'#.#.##.#.',
'',
'#...##..#',
'#....#..#',
'..##..###',
'#####.##.',
'#####.##.',
'..##..###',
'#....#..#'
]

if use_real_data:
    test_input = data
else:
    test_input = example

# [[[1,2,3,4],[1,2,3,4]],[[3,4,5,6],[3,4,5,6]]]

all_matricies = []
matrix = []

for line in test_input:
    if line == '':
        all_matricies.append(matrix.copy())
        matrix.clear()
    else:
        matrix.append(line)
all_matricies.append(matrix.copy())
    

# for line in all_matricies[0]:
#     print(line)
# print('')

def find_hor_mirror(matrix):
    for i in range(len(matrix)):
        lines_to_check = min(i+1,len(matrix)-i-1)
        mirrored = None
        for loops in range(lines_to_check):
            if matrix[i-loops] != matrix[i+1+loops]:
                mirrored = False
                break
            mirrored = True
        if mirrored:
            return (i+1)
    return

hor_mirror_index = []
vert_mirror_index = []

for matrix in all_matricies:
    hor_index = find_hor_mirror(matrix)
    if hor_index != None:
        hor_mirror_index.append(hor_index)

    rotated_matrix = list(zip(*matrix[::-1]))

    vert_index = find_hor_mirror(rotated_matrix)
    if vert_index != None:
        vert_mirror_index.append(vert_index)

result = sum(hor_mirror_index) * 100 + sum(vert_mirror_index)

print(f'Part 1 Answer: {result}')

