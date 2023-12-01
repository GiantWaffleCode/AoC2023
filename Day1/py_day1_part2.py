# -----------------------
#   Advent of Code 2023
#      GiantWaffle
#   Challenge 1 of 25
#      Part 2 of 2
# -----------------------

data = []

with open('Day1\data_day1.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
    'fourbsqr7bktkbqbdlpfour'
    ]

num_dict = {
    'one'   : '1',
    'two'   : '2',
    'three' : '3',
    'four'  : '4',
    'five'  : '5',
    'six'   : '6',
    'seven' : '7',
    'eight' : '8',
    'nine'  : '9',
    '1'       : '1',
    '2'       : '2',
    '3'       : '3',
    '4'       : '4',
    '5'       : '5',
    '6'       : '6',
    '7'       : '7',
    '8'       : '8',
    '9'       : '9'
}

total= 0

for ex in data:
    found = []
    for key, value in num_dict.items():
        check = ex.find(key)
        rcheck = ex.rfind(key)
        if check >= 0:
            found.append((check, value))
        if rcheck >= 0:
            found.append((rcheck, value))
    num_smol = [999, None]
    num_beeg = [-1, None]
    for item in found: #(index, value)
        index = item[0]
        if index < num_smol[0]:
            num_smol = [index, item[1]]
        if index > num_beeg[0]:
            num_beeg = [index, item[1]]
    result = num_smol[1] + num_beeg [1]
    # print(f'{result}')
    total += int(result)

print(f'Answer: {total}')
    
