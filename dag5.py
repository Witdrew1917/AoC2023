import numpy as np
from tqdm import tqdm

seed_to_soil = {}
soil_to_fertilizer = {}
fertilizer_to_water = {}
water_to_light = {}
light_to_temperature = {}
temperature_to_humidity = {}
humidity_to_location = {}

maps = [ seed_to_soil, \
    soil_to_fertilizer, \
    fertilizer_to_water, \
    water_to_light, \
    light_to_temperature, \
    temperature_to_humidity, \
    humidity_to_location]


with open("./Data/data_dag5.txt") as f:
    content = f.readlines()

seed_list = []
map_index = -1
for line in tqdm(content):

    if len(seed_list) == 0:
        seeds = line.split(':')

        for seed in seeds[1].split():
            seed_list.append(int(seed))

        continue

    if line == "\n":
        continue

    if ':' in line:
        map_index += 1
        continue

    val, key, nums = line.split()

    maps[map_index][int(key)] = (int(val), int(nums))

loc = []
for seed in tqdm(seed_list):

    for mp in maps:

        for key in mp.keys():

            val, nums = mp[key]

            if key <= seed and seed <= key + nums -1:
                seed = (seed - key) + val
                break




    loc.append(seed)


loc = np.array(loc)
print(np.min(loc))


seed_list = []
map_index = -1
for line in tqdm(content):

    if len(seed_list) == 0:
        seeds_temp = line.split(':')
        seeds = seeds_temp.split()

        for i in range(0,len(seeds),2):
            seed = seeds[i]
            nums = seeds[i+1]
            seed_list.append((seed, nums))

        continue

    if line == "\n":
        continue

    if ':' in line:
        map_index += 1
        continue

    val, key, nums = line.split()

    maps[map_index][int(key)] = (int(val), int(nums))

loc = []
while len(seed_list) > 0:

    seed, length = seed_list.pop()

    for mp in maps:

        for key in mp.keys():

            val, nums = mp[key]

            if key <= seed and seed <= key + nums -1:
                seed = (seed - key) + val
                break




    loc.append(seed)


loc = np.array(loc)
print(np.min(loc))


