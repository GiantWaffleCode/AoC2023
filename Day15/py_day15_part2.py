#   Advent of Code 2023
#      GiantWaffle
#   Challenge 15 of 25
#      Part 2 of 2
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

# for line in data_list:
#     print(line)


def hash_line(string):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value

# 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

#seperate string and operators
directions = []

for line in data_list:
    if '=' in line:
        split = line.split('=')
        split[1] = int(split[1])
    else:
        split = [line[:-1]]
    directions.append(split)

# print(directions)

#initialize box list

boxes = []

for i in range(256):
    boxes.append([])

print(len(boxes))

#hash string for box number

for direction in directions:
    hash_value= hash_line(direction[0])
    lens_list = boxes[hash_value]
    if len(direction) == 2: # = command
        # [['pc', 4],['ot', 9],['ab', 5]]
        for lens in lens_list:
            if lens[0] == direction[0]:
                lens[1] = direction[1]
                break
        else:
            lens_list.append(direction)

    else: # - command
        for lens in lens_list:
            if lens[0] == direction[0]:
                lens_list.remove(lens)
                break

print(boxes[0])

def calc_box_light(lens_list):
    # [['pc', 4],['ot', 9],['ab', 5]]
    total = 0
    for num, lens in enumerate(lens_list):
        total += (lens[1] * (num+1))
    return total
            
light_values = []

for box_num, box in enumerate(boxes):
    light_val = calc_box_light(box)
    total = (box_num + 1) * light_val
    light_values.append(total)

#go to box and perform operation
# = go to back and look for lens.
# replace if found, add if not
#- go to box and remove lens in present

#calc light (multi all)
# box num + 1
# slot number of lens starting at 1
# focal len

#sum all boxes for total focal power
    
print(f'Part 2 Answer: {sum(light_values)}')