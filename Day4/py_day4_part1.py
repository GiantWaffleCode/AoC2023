# -----------------------
#   Advent of Code 2023
#      GiantWaffle
#   Challenge 4 of 25
#      Part 1 of 2
# -----------------------


use_real_data = True

data = []

with open('Day4\data_day4.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
    ]

if use_real_data:
    test_input = data
else:
    test_input = example

cards = []

for test in test_input:
    fixed_row = test.replace('  ', ' ')
    card = fixed_row.split(': ', 1)[1].split(' | ')
    final_card = []
    for part in card:
        split = part.split(' ')

        final_card.append(list(map(int, split)))
    cards.append(final_card)
    #print(f'{final_card}')

#print(f'{cards}')

overall_win_total = 0

for card in cards:
    win_amt = 0
    card_win_total = 0
    for winning_num in card[0]:
        for check_num in card[1]:
            if winning_num == check_num:
                win_amt += 1
    if win_amt > 0:
        card_win_total = 2 ** (win_amt - 1)

    overall_win_total += card_win_total

print(f'Total Won is: {overall_win_total}')