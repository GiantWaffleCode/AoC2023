# -----------------------
#   Advent of Code 2023
#      GiantWaffle
#   Challenge 5 of 25
#      Part 1 of 2
# -----------------------

use_real_data = True

data = []
example = []

with open('Day5\data_day5.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

with open('Day5\example_day5.txt') as f:
   lines = f.readlines()
   for line in lines:
      example.append(line.strip())

if use_real_data:
    test_input = data
else:
    test_input = example

#Get Seeds List
seeds = test_input[0].split('seeds: ',1)[1].split(' ')
seeds = list(map(int, seeds))

seed_to_soil_index = test_input.index('seed-to-soil map:')
soil_to_fert_index = test_input.index('soil-to-fertilizer map:')
fert_to_water_index = test_input.index('fertilizer-to-water map:')
water_to_light_index = test_input.index('water-to-light map:')
light_to_temp_index = test_input.index('light-to-temperature map:')
temp_to_humidity_index = test_input.index('temperature-to-humidity map:')
humidity_to_location_index = test_input.index('humidity-to-location map:')

index_map = [
    seed_to_soil_index,
    soil_to_fert_index,
    fert_to_water_index,
    water_to_light_index,
    light_to_temp_index,
    temp_to_humidity_index,
    humidity_to_location_index
]

#print(f'{index_map}')

#[[Destination, Source, Len],...]
seed_to_soil_values = []
soil_to_fert_values = []
fert_to_water_values = []
water_to_light_values = []
light_to_temp_values = []
temp_to_humidity_values = []
humidity_to_location_values = []


for index, line in enumerate(test_input):

    if (index >= seed_to_soil_index + 1) and (index <= soil_to_fert_index - 2):
        result = list(map(int, line.split(' ')))
        seed_to_soil_values.append(result)

    elif (index >= soil_to_fert_index + 1) and (index <= fert_to_water_index - 2):
        result = list(map(int, line.split(' ')))
        soil_to_fert_values.append(result)

    elif (index >= fert_to_water_index + 1) and (index <= water_to_light_index - 2):
        result = list(map(int, line.split(' ')))
        fert_to_water_values.append(result)

    elif (index >= water_to_light_index + 1) and (index <= light_to_temp_index - 2):
        result = list(map(int, line.split(' ')))
        water_to_light_values.append(result)
    
    elif (index >= light_to_temp_index + 1) and (index <= temp_to_humidity_index - 2):
        result = list(map(int, line.split(' ')))
        light_to_temp_values.append(result)

    elif (index >= temp_to_humidity_index + 1) and (index <= humidity_to_location_index - 2):
        result = list(map(int, line.split(' ')))
        temp_to_humidity_values.append(result)

    elif (index >= humidity_to_location_index + 1):
        result = list(map(int, line.split(' ')))
        humidity_to_location_values.append(result)

# print(f'Seeds: {seeds}')
# print(f'Seed to Soil: {seed_to_soil_values}')
# print(f'Soil to Fert: {soil_to_fert_values}')
# print(f'Fert to Water: {fert_to_water_values}')
# print(f'Water to Light: {water_to_light_values}')
# print(f'Light to Temp: {light_to_temp_values}')
# print(f'Temp to Hum: {temp_to_humidity_values}')
# print(f'Hum to Loc: {humidity_to_location_values}')
       

def findRange(lookup_value, map_list):
    #print(f'{lookup_value}')
    for current_map in map_list:
        #print(f'{current_map}')
        if lookup_value >= current_map[1]:
            if lookup_value <= current_map[1]+current_map[2] - 1:
                #print(f'Found map within range')
                diff = lookup_value - current_map[1]
                result = current_map[0] + diff
                return result
    return lookup_value


def seedToLoc(seed):
    soil_num = findRange(seed, seed_to_soil_values)
    fert_num = findRange(soil_num, soil_to_fert_values)
    water_num = findRange(fert_num, fert_to_water_values)
    light_num = findRange(water_num, water_to_light_values)
    temp_num = findRange(light_num, light_to_temp_values)
    hum_num = findRange(temp_num, temp_to_humidity_values)
    loc_num = findRange(hum_num, humidity_to_location_values)
    return loc_num

lowest_loc = None

for seed in seeds:
    result = seedToLoc(seed)
    if lowest_loc is None or result < lowest_loc:
        lowest_loc = result

    print(f'Seed {seed} Location is {result}')

print(f'Lowest Location is: {lowest_loc}')
