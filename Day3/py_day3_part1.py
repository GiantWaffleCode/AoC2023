# -----------------------
#   Advent of Code 2023
#      GiantWaffle
#   Challenge 3 of 25
#      Part 1 of 2
# -----------------------

use_real_data = True

data = []

with open('Day3\data_day3.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    '467..114..',
    '...*......',
    '..35...633',
    '......#...',
    '617*......',
    '.....+..58',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..'
]

if use_real_data:
    test_input = data
else:
    test_input = example

lookup = {
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '0' : 0,
    '@' : -1,
    '#' : -1,
    '$' : -1,
    '%' : -1,
    '&' : -1,
    '*' : -1,
    '-' : -1,
    '+' : -1,
    '=' : -1,
    '/' : -1,    
    '.' : None
}

# [[Numbers], Line #, [Start Index, End Index]]
def generatePartPositions():
    parts = []
    for height, line in enumerate(test_input):
        found_number = []
        location = [None, None]
        for width, point in enumerate(line):
            #print(point)
            test = lookup[point]
            if (test is None) | (test == -1):
                if found_number:
                    #print(f'{found_number}')
                    location[1] = width - 1
                    part = [found_number, height, location]
                    #print(f'{part}')
                    parts.append(part)
                    found_number = []
                    location = [None, None]
            elif test >= 0:
                if not found_number:
                    location[0] = width
                if width != len(line) - 1:
                    found_number.append(test)
                else:
                    #print(f'Found Number at end of line')
                    found_number.append(test)
                    location[1] = width - 1
                    part = [found_number, height, location]
                    #print(f'{part}')
                    parts.append(part)
                    found_number = []
                    location = [None, None]
    return parts


# [Symbol, Line #, Position Index]
def generateSymbolPositions():
    symbols = []
    for height, line in enumerate(test_input):
        found_symbol = ''
        location = None
        for width, point in enumerate(line):
            test = lookup[point]
            if test == -1:
                found_symbol = point
                location = width
                symbol = [found_symbol, height, location]
                #print(f'{symbol}')
                symbols.append(symbol)
                found_symbol = ''
                location = None
    return symbols
        

#given a range of cordinates check is a symbol is next to it
def checkIfNextToSymbols(cord, symbols): #cord = [line#, [index start, index end]]
    higest_height_index = symbols[-1][1] #ex is 8
    for symbol in symbols:
        #check left and right
        if symbol[1] == cord[0]: 
            if (symbol[2] == cord[1][0]-1) | (symbol[2] == cord[1][1]+1):
                #print(f'Symbol: {symbol[0]} is left or right of the number')
                return symbol
        #check above
        if (cord[0] > 0) & (symbol[1] == cord[0]-1):
            if (symbol[2] >= cord[1][0] - 1) & (symbol[2] <= cord[1][1] + 1):
                #print(f'Symbol: {symbol[0]} is above the number')
                return symbol
        #check below    
        if (cord[0] < higest_height_index) & (symbol[1] == cord[0]+1):
            if (symbol[2] >= cord[1][0] - 1) & (symbol[2] <= cord[1][1] + 1):
                #print(f'Symbol: {symbol[0]} is below the number')
                return symbol
    return -1

part_list = generatePartPositions()
symbol_list = generateSymbolPositions()

final_total = 0

for part in part_list:
    #print(f'{part}')
    #print(f'Checking: {part[0]} Cords: {part[1:3]}')
    check_result = checkIfNextToSymbols(part[1:3], symbol_list)
    #print(f'{check_result}')
    if check_result != -1:
        conc_num = []
        for num in part[0]:
            conc_num.append(str(num))
        final_num = int("".join(conc_num))
        final_total += final_num
        #print(f'{final_num}')
        #print(f'Part [{final_num}] is next to symbol: {check_result[0]}')
        continue

print(f'Final Sum: {final_total}')