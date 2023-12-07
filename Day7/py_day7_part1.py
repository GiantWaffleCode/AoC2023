# -----------------------
#   Advent of Code 2023
#      GiantWaffle
#   Challenge 7 of 25
#      Part 1 of 2
# -----------------------

use_real_data = True

data = []

with open('Day7\data_day7.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    '32T3K 765',
    'T55J5 684',
    'KK677 28',
    'KTJJT 220',
    'QQQJA 483'
]

if use_real_data:
    test_input = data
else:
    test_input = example


games = []

#Get rounds into lists
# [['3', '2', 'T', '3', 'K'], 765, -1]
# [[Cards in Order], Bet, Rank (-1 if none)]
for case in test_input:
    curr_round = case.split()
    curr_round = [list(curr_round[0]), int(curr_round[1]), -1]
    games.append(curr_round)


def secondaryScore(hand): #  ['K','K','6','7','7']
    total_score = 0
    for i, card in enumerate(hand):
        card_value = '23456789TJQKA'.find(card)+2
        multi = 15 ** (4-i)
        total_score += card_value * multi
    return total_score


five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = [] 
two_pair = []
one_pair = []
high_card = []


for game in games:
    game[2] = secondaryScore(game[0])

    hits = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for card in game[0]:
        hits['23456789TJQKA'.find(card)+1] += 1
    
    if 5 in hits: #five of a kind
        five_of_a_kind.append(game)

    elif 4 in hits: #four of a kind
        four_of_a_kind.append(game)

    elif 3 in hits: #full house and three of a kind
        if 2 in hits:
            full_house.append(game)
        else:
            three_of_a_kind.append(game)
    
    elif 2 in hits: #two pair and one pair
        if hits.count(2) == 2:
            two_pair.append(game)
        else:
            one_pair.append(game)
    
    else: #high card
        high_card.append(game)


all_ranks = [
    five_of_a_kind,
    four_of_a_kind,
    full_house,
    three_of_a_kind,
    two_pair,
    one_pair,
    high_card
]


def sortByScore(rank):
    rank.sort(key=lambda x: x[2], reverse=True)

all_games = []

for rank in all_ranks: #sort all ranks by secondary score
    sortByScore(rank)
    for game in rank:
        all_games.append(game)
    
all_games.reverse()

print(f'{all_games[0]}')

total_score = 0

for i, game in enumerate(all_games):
    hand_score = game[1] * (i+1)
    print(hand_score)
    total_score += hand_score

print(f'Final Score: {total_score}')