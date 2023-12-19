import re
import sys
file_path = './day_05/input.txt'
file1 = open(file_path, 'r')
Lines = file1.readlines()

line_zero = Lines[0]
matches = re.finditer(r"\d+", line_zero)
seeds = []


#this solution I'm not particularly proud of, it relies on a lot of repeated code.
#essentially it just travels through the input and pulls all the numbers. Then it brute forces
#which range the location falls into and converts each int through all of the conversions
for match in matches:
    seeds.append(line_zero[match.start():match.end()])

seed_to_soil = []
for i in range(3, 50):
    matches = re.finditer(r"\d+", Lines[i])
    seed_to_soil.append([])
    for match in matches:
        seed_to_soil[len(seed_to_soil) - 1].append(int(Lines[i][match.start():match.end()]))

soil_to_fertilizer = []
for i in range(52, 70):
    matches = re.finditer(r"\d+", Lines[i])
    soil_to_fertilizer.append([])
    for match in matches:
        soil_to_fertilizer[len(soil_to_fertilizer) - 1].append(int(Lines[i][match.start():match.end()]))

fertilizer_to_water = []
for i in range(72, 84):
    matches = re.finditer(r"\d+", Lines[i])
    fertilizer_to_water.append([])
    for match in matches:
        fertilizer_to_water[len(fertilizer_to_water) - 1].append(int(Lines[i][match.start():match.end()]))

water_to_light = []
for i in range(86, 135):
    matches = re.finditer(r"\d+", Lines[i])
    water_to_light.append([])
    for match in matches:
        water_to_light[len(water_to_light) - 1].append(int(Lines[i][match.start():match.end()]))

light_to_temperature = []
for i in range(137, 167):
    matches = re.finditer(r"\d+", Lines[i])
    light_to_temperature.append([])
    for match in matches:
        light_to_temperature[len(light_to_temperature) - 1].append(int(Lines[i][match.start():match.end()]))

temperature_to_humidity = []
for i in range(169, 192):
    matches = re.finditer(r"\d+", Lines[i])
    temperature_to_humidity.append([])
    for match in matches:
        temperature_to_humidity[len(temperature_to_humidity) - 1].append(int(Lines[i][match.start():match.end()]))

humidity_to_location = []
for i in range(194, 237):
    matches = re.finditer(r"\d+", Lines[i])
    humidity_to_location.append([])
    for match in matches:
        humidity_to_location[len(humidity_to_location) - 1].append(int(Lines[i][match.start():match.end()]))

print(seed_to_soil)
locations = []

for seed in seeds:
    curr_loc = int(seed)
    for i in range(len(seed_to_soil)):
        if curr_loc >= seed_to_soil[i][1] and curr_loc < seed_to_soil[i][1] + seed_to_soil[i][2]:
            curr_loc =  seed_to_soil[i][0] + curr_loc - seed_to_soil[i][1]
            break

    for i in range(len(soil_to_fertilizer)):
        if curr_loc >= soil_to_fertilizer[i][1] and curr_loc < soil_to_fertilizer[i][1] + soil_to_fertilizer[i][2]:
            curr_loc =  soil_to_fertilizer[i][0] + curr_loc - soil_to_fertilizer[i][1]
            break

    for i in range(len(fertilizer_to_water)):
        if curr_loc >= fertilizer_to_water[i][1] and curr_loc < fertilizer_to_water[i][1] + fertilizer_to_water[i][2]:
            curr_loc =  fertilizer_to_water[i][0] + curr_loc - fertilizer_to_water[i][1]
            break

    for i in range(len(water_to_light)):
        if curr_loc >= water_to_light[i][1] and curr_loc < water_to_light[i][1] + water_to_light[i][2]:
            curr_loc =  water_to_light[i][0] + curr_loc - water_to_light[i][1]
            break

    for i in range(len(light_to_temperature)):
        if curr_loc >= light_to_temperature[i][1] and curr_loc < light_to_temperature[i][1] + light_to_temperature[i][2]:
            curr_loc =  light_to_temperature[i][0] + curr_loc - light_to_temperature[i][1]
            break
    
    for i in range(len(temperature_to_humidity)):
        if curr_loc >= temperature_to_humidity[i][1] and curr_loc < temperature_to_humidity[i][1] + temperature_to_humidity[i][2]:
            curr_loc =  temperature_to_humidity[i][0] + curr_loc - temperature_to_humidity[i][1]
            break

    for i in range(len(humidity_to_location)):
        if curr_loc >= humidity_to_location[i][1] and curr_loc < humidity_to_location[i][1] + humidity_to_location[i][2]:
            curr_loc =  humidity_to_location[i][0] + curr_loc - humidity_to_location[i][1]
            break

    locations.append(curr_loc)

print(locations)
print(min(locations))
    
