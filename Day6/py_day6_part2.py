# -----------------------
#   Advent of Code 2023
#      GiantWaffle
#   Challenge 6 of 25
#      Part 2 of 2
# -----------------------

use_real_data = True

data = []

with open('Day6\data_day6.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    'Time:      7  15   30',
    'Distance:  9  40  200'
]

if use_real_data:
    test_input = data
else:
    test_input = example

race_data = [
    [int(''.join(test_input[0].removeprefix('Time:').split()))],
    [int(''.join(test_input[1].removeprefix('Distance:').split()))]
    ]

#print(f'{race_data=}')

def calcDistance(time_held_down, time):
    return (time_held_down * (time - time_held_down))

total_wins = []

for num, race in enumerate(race_data[0]):
    distance_record = race_data[1][num]
    winning_times = []
    for i in range(race):
        total_distance = calcDistance(i, race)
        if total_distance > distance_record:
            winning_times.append(i)
    total_wins.append(len(winning_times))

total_tol = 1

for win in total_wins:
    total_tol *= win

print(f'Total Tolerance: {total_tol}')