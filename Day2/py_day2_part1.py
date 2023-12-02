# -----------------------
#   Advent of Code 2023
#      GiantWaffle
#   Challenge 2 of 25
#      Part 1 of 2
# -----------------------




data = []

with open('Day2\data_day2.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
]

game_data = []

    #switch example to data for proper input
for item in data:
    #[Pull ID, R, G, B]
    game = item.split(': ', 1)[1].split('; ')
    result = []
    for pull in game:
        currentpull = pull.split(', ')
        currentresult = []
        for ind in currentpull:
            currentresult.append(ind.split(' '))
        result.append(currentresult)
    game_data.append(result)
    #print(f'{game_data}')
    

master_data = []
for i, game in enumerate(game_data):
    game_pulls = []
    for pull in game:
        pull_data = [0, 0, 0] #[R, G, B]
        for dice in pull:
            #print(f'{dice}')
            match dice[1]:
                case 'red':
                    pull_data[0] = int(dice[0])
                case 'green':
                    pull_data[1] = int(dice[0])
                case 'blue':
                    pull_data[2] = int(dice[0])
                case _:
                    continue
        game_pulls.append(pull_data)
    game_data = [i + 1, game_pulls]
    master_data.append(game_data)
#print(f'{master_data}')

total_dice = [12, 13, 14] # [R, G, B]
total_good_ids = 0

for game in master_data:
    is_possible = True
    #print(f'{game}')
    for indround in game[1]:
        if indround[0] > total_dice[0]:
            is_possible = False
        if indround[1] > total_dice[1]:
            is_possible = False
        if indround[2] > total_dice[2]:
            is_possible = False
    if is_possible:
        total_good_ids += game[0]

print(f'Total: {total_good_ids}')
        

