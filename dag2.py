import re

constraint_red = 12
constraint_green = 13
constraint_blue = 14

constraints = {'red':constraint_red,\
        'green':constraint_green,\
        'blue':constraint_blue}

power_set = {'red':0,'green':0,'blue':0}

patterns = ['red','green', 'blue']

id_pattern = ['Game',':']


with open("./Data/data_dag2.txt") as f:
    content = f.readlines()

game_sum = 0

for line in content:

    violation_flag = False

    game = line.split(':')
    rounds = game[1].split(';')
    cubes = rounds[0].split(',')

    for rnd in rounds:

        cubes = rnd.split(',')
        for draw in cubes:
            val_and_color = draw.split()

            if constraints[val_and_color[1]] < \
                    int(val_and_color[0]):
                violation_flag = True
                break


    if not violation_flag:
        game_id = int(game[0].split()[1])
        game_sum += game_id

print(game_sum)


game_sum = 0

for line in content:

    violation_flag = False

    game = line.split(':')
    rounds = game[1].split(';')
    cubes = rounds[0].split(',')

    power_set['red'] = 1
    power_set['green'] = 1
    power_set['blue'] = 1

    for rnd in rounds:

        cubes = rnd.split(',')
        for draw in cubes:
            val_and_color = draw.split()

            if power_set[val_and_color[1]] < \
                    int(val_and_color[0]):
                power_set[val_and_color[1]] = \
                        int(val_and_color[0])

    print(power_set.values())
    game_sum += power_set['red'] * power_set['blue'] \
            * power_set['green']


print(game_sum)
