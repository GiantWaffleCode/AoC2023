#   Advent of Code 2023
#      GiantWaffle
#   Challenge 20 of 25
#      Part 1 of 2
# -----------------------

use_real_data = False
data = []

with open('Day20\data_day20.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    'broadcaster -> a, b, c',
    '%a -> b',
    '%b -> c',
    '%c -> inv',
    '&inv -> a'
]

if use_real_data:
    test_input = data
else:
    test_input = example

instructions = []

for line in test_input:
    split = line.split(' -> ')
    if split[0] == 'broadcaster':
        ins = [[split[0]],split[1].split(', ')]
    else:
        ins = [[split[0][:1], split[0][1:]], split[1].split(', ')]
    instructions.append(ins)


ff_dict = {}  #key = idenity      value = state


# ! Broadcaster
    
def broad_mod(signal):
    return signal
    
# ! Flip Flop %
def flip_flop_mod(signal, loc, dest, dict):
    status = dict.get(loc, False)
    if not signal:
        status = not status
        output = int(status)
        dict[loc] = status
        return output, dest

# ! Conj &
    

for ins in instructions:
    match ins[0][0]:
        case 'broadcaster':
            pass
        case '%':
            pass
        case '&':
            pass

print(ff_dict)
signal1 = flip_flop_mod(0, 'a', ['b'], ff_dict)
print(ff_dict)
print(signal1)

#signal2 = flip_flop_mod(signal1, 'b', ['c','d'], ff_dict)
signal3 = flip_flop_mod(0, 'a', ['b'], ff_dict)
print(ff_dict)
print(signal3)

#TODO: REST OF PROBLEM