#   Advent of Code 2023
#      GiantWaffle
#   Challenge 13 of 25
#      Part 2 of 2
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

def find_smudge(matrix):
    for i in range(len(matrix)):
            lines_to_check = min(i+1,len(matrix)-i-1)
            diff = 0
            for loops in range(lines_to_check):
                top_line = matrix[i-loops]
                bot_line = matrix[i+1+loops]

                for k in range(len(top_line)):
                    if top_line[k] != bot_line[k]:
                        diff += 1
            if diff == 1:
                return i+1
    return



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


smudge_hor_indexs = []
smudge_vert_indexs = []

for matrix in all_matricies:
    hor_index = find_smudge(matrix)
    if hor_index != None:
        smudge_hor_indexs.append(hor_index)

    rotated_matrix = list(zip(*matrix[::-1]))

    vert_index = find_smudge(rotated_matrix)
    if vert_index != None:
        smudge_vert_indexs.append(vert_index)

result = sum(smudge_hor_indexs) * 100 + sum(smudge_vert_indexs)

print(f'Part 2 Answer: {result}')

