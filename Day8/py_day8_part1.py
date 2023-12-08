# -----------------------
#   Advent of Code 2023
#      GiantWaffle
#   Challenge 8 of 25
#      Part 1 of 2
# -----------------------

use_real_data = True

data = []

with open('Day8\data_day8.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    'RL',
    '',
    'AAA = (BBB, CCC)',
    'BBB = (DDD, EEE)',
    'CCC = (ZZZ, GGG)',
    'DDD = (DDD, DDD)',
    'EEE = (EEE, EEE)',
    'GGG = (GGG, GGG)',
    'ZZZ = (ZZZ, ZZZ)'
]

if use_real_data:
    test_input = data
else:
    test_input = example


instructions = test_input[0]
network_map_raw = test_input[2:]

#print(instructions)

network_map = {}

for line in network_map_raw:
    node = line[:3]
    #print(node)
    left_map = line[7:10]
    right_map = line[12:15]
    left_right_map = [left_map, right_map]
    #print(left_right_map)
    network_map[node] = left_right_map

#print(network_map)

#print(network_map['AAA'])

def followInstruction(node, instruction):
    if instruction == 'R':
        return network_map[node][1]
    else:
        return network_map[node][0]

def getInstruction(instruction_num):
    return (instruction_num % len(instructions))

current_node = 'AAA'
steps = 0

while current_node != 'ZZZ':
    current_node = followInstruction(current_node, instructions[getInstruction(steps)])
    steps += 1

print(steps)

