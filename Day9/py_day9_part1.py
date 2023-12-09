# -----------------------
#   Advent of Code 2023
#      GiantWaffle
#   Challenge 9 of 25
#      Part 1 of 2
# -----------------------

use_real_data = True

data = []

with open('Day9\data_day9.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    '0 3 6 9 12 15',
    '1 3 6 10 15 21',
    '10 13 16 21 30 45'
]

if use_real_data:
    test_input = data
else:
    test_input = example

patterns = []

for line in test_input:
    pattern = list(map(int, line.split()))
    patterns.append(pattern)

#print(patterns)

    # [0, 3, 6, 9, 12, 15]
    # [3, 3, 3, 3, 3, 3]
    # [0, 0, 0, 0, 0]

def differenceList(list):
    diffs = []
    for i in range(len(list)-1):
        diff = list[i+1] - list[i]
        diffs.append(diff)
    return diffs


def findNextNumInPattern(pattern):
    current_pattern = pattern
    pattern_diffs = [pattern]
    while any(current_pattern):
        next_diff = differenceList(current_pattern)
        pattern_diffs.append(next_diff)
        current_pattern = next_diff
    
    pattern_diffs[-1].append(0)
    for i in range(len(pattern_diffs)-1):
        pattern_diffs[-i-2].append(pattern_diffs[-i-2][-1]+pattern_diffs[-i-1][-1])

    return pattern_diffs[0][-1]

results = []

for pattern in patterns:
    pattern_result = findNextNumInPattern(pattern)
    results.append(pattern_result)

print(f'Sum of Pattern Results: {sum(results)}')