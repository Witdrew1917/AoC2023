import numpy as np
from tqdm import tqdm

with open("./Data/data_dag6.txt") as f:
    content = f.readlines()


competition_results = []
for line in content:

    competition = line.split(':')
    competition_results.append(competition[1].split())

total = 1

for i, val in enumerate(competition_results[0]):

    record_breaking_strategies = 0
    strategy = np.arange(int(val))

    for button_time in strategy:
        speed = button_time
        distance = speed*(int(val)-button_time)

        if distance > int(competition_results[1][i]):
            record_breaking_strategies += 1

    total *= record_breaking_strategies

print(total)


competition_results = []
for line in content:

    competition = line.split(':')
    temp = ""

    for val in competition[1].split():
        temp += val

    competition_results.append(temp)



total = 1


val = competition_results[0]

record_breaking_strategies = 0
strategy = np.arange(int(val))

for button_time in strategy:
    speed = button_time
    distance = speed*(int(val)-button_time)

    if distance > int(competition_results[1]):
        record_breaking_strategies += 1

total *= record_breaking_strategies

print(total)








