#   Advent of Code 2023
#      GiantWaffle
#   Challenge 12 of 25
#      Part 1 of 2
# -----------------------

use_real_data = False

data = []

with open('Day12\data_day12.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    '???.### 1,1,3',
    '.??..??...?##. 1,1,3',
    '?#?#?#?#?#?#?#? 1,3,1,6',
    '????.#...#... 4,1,1',
    '????.######..#####. 1,6,5',
    '?###???????? 3,2,1'
]

if use_real_data:
    test_input = data
else:
    test_input = example


#parse input
converted_input = []

for line in test_input:
    temp = line.split()
    input_str = temp[0]
    input_tup = tuple(map(int, temp[1].split(',')))

    result = (input_str, input_tup)
    converted_input.append(result)


def slideCheck(string, size, starting_index=0):
    temp_string = string.copy()
    temp_extra = 0
    if len(string)-size-1-starting_index == 0:
        temp_string += '.'
        #print(f'Temp String: {"".join(temp_string)}')
    for j in range(len(temp_string)-size-1-starting_index):
        segment = temp_string[j+starting_index:size+j+2+starting_index]
        if (segment[0] == '.') or (segment[0] == '?'):
            if '.' not in segment[1:size+1]:
                if (segment[-1] == '.') or (segment[-1] == '?'):
                    return j+1+starting_index #returning index of start '#'
    return -1


def modString(string, size ,index):  #'kjmnasdjafs'  '.######.alskjd'
    mod_string = string.copy()
    if index != 0:
        mod_string[index-1] = '.'
    for k in range(size):
        mod_string[index+k] = '#'
    if index + size != len(string):     # ?????    ####  1    .####
        mod_string[index+size] = '.'
    return mod_string


#left load init
left_init_input = []

for line in converted_input: #('???.###', (1, 1, 3))
    start = list(line[0]) #   '???.###'
    order = line[1] #   (1, 1, 3)

    #    1   #.   .#####.    
    current_index = 0
    for i, element in enumerate(order):
        if i == 0: #first item is the only one that can be all the way left
            if ('.' not in start[:element]) & (start[element] != '#'):
                if ('#' not in start[:element]) & ('.' not in start[:element]):
                    mod_string = modString(start, element, 0)
            else:
                index = slideCheck(start, element, current_index)
                current_index = index + element
                mod_string = modString(start, element, index)
        
        else:
            index = slideCheck(start, element, current_index)
            current_index = index + element
            if index == -1:
                break
            mod_string = modString(start, element, index)
     
        start = mod_string.copy()


    #add function to make all remaning '?' into '.'

    final_string = ''.join(mod_string).replace('?','.')
    print(final_string)
    left_init_input.append(final_string)


    



#permutation solving and counting