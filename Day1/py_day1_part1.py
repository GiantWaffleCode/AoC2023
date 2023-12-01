# -----------------------
#   Advent of Code 2023
#      GiantWaffle
#   Challenge 1 of 25
#      Part 1 of 2
# -----------------------

data = []

with open('Day1\data_day1.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet'
    ]

total = 0

for line in data:
   # go through fwd
    for char_fwd in line:
        if char_fwd.isdigit():
            firstdigit = char_fwd
            break

    for char_bwd in reversed(line):
        if char_bwd.isdigit():
            lastdigit = char_bwd
            break

    total += int(firstdigit + lastdigit)

print(f'{total}')
