#   Advent of Code 2023
#      GiantWaffle
#   Challenge 15 of 25
#      Part 1 of 2
# -----------------------

use_real_data = True
data = []

with open('Day15\data_day15.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = ['rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7']


if use_real_data:
    test_input = data
else:
    test_input = example

data_list = test_input[0].split(',')

for line in data_list:
    print(line)


current_value = 0
current_values = []

for line in data_list:
    current_value = 0
    for char in line:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    current_values.append(current_value)

print(current_values)
print(f'Part 1 Answer: {sum(current_values)}')
