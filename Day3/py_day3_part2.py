# -----------------------
#   Advent of Code 2023
#      GiantWaffle
#   Challenge 3 of 25
#      Part 2 of 2
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
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
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
    '@' : None,
    '#' : None,
    '$' : None,
    '%' : None,
    '&' : None,
    '*' : -1,
    '-' : None,
    '+' : None,
    '=' : None,
    '/' : None,    
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
        
        
def checkNextToSymbols(parts, symbols): # [[cord x, cord y],[list of adj]]
    higest_height_index = symbols[-1][1] #ex is 8
    adj_parts = []
    gear_list = []
    for symbol in symbols:
        for part in parts: 
            # Part    [[Numbers], Line #, [Start Index, End Index]]
            # Symbol  [Symbol, Line #, Position Index]
            #check left right
            if part[1] == symbol[1]:
                if (symbol[2] >= part[2][0]-1) & (symbol[2] <= part[2][1]+1):
                    adj_parts.append(part)
            #check up
            elif (symbol[1] > 0) & (part[1] == symbol[1]-1):
                if (symbol[2] >= part[2][0]-1) & (symbol[2] <= part[2][1]+1):
                    adj_parts.append(part)
            #check down
            elif (symbol[1] <= higest_height_index) & (part[1] == symbol[1]+1):
                if (symbol[2] >= part[2][0]-1) & (symbol[2] <= part[2][1]+1):
                    adj_parts.append(part)
        gear_list.append([[symbol[1], symbol[2]], adj_parts])
        adj_parts = []
    return gear_list

def concInt(part):
    conc_num = []
    for num in part:
        conc_num.append(str(num))
    final_num = int("".join(conc_num))
    return final_num


part_list = generatePartPositions()
symbol_list = generateSymbolPositions()

final_total = 0

for part in part_list:
    part[0] = concInt(part[0])

#print(f'{part_list}')

check_result = checkNextToSymbols(part_list, symbol_list)
#print(f'{check_result}')

ratio_sum = 0

for check in check_result:
    if len(check[1]) == 2:
        #print(f'There are exactly 2 adjecent parts to this gear')
        #print(f'{check[1][0][0]} and {check[1][0][1]}')
        ratio = check[1][0][0] * check[1][1][0]
        ratio_sum += ratio

print(f'Final Sum: {ratio_sum}')