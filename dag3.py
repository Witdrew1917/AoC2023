import re

answer = ['0','1','2','3','4','5','6',\
        '7','8','9']

numbers = {}

symbol_list = []
filtered_list = []


def make_combinations(x,y):

    left = x - 1
    right = x + 1
    top = y + 1
    bottom = y - 1

    return [(left,top), \
            (x,top), \
            (right,top), \
            (left, y), \
            (right,y), \
            (left, bottom), \
            (x,bottom), \
            (right, bottom)]



def filter_numbers():

    for key in numbers.keys():

        for value in numbers[key]:

            start, end = value
            start_x, start_y = start
            end_x, end_y = end

            starts = make_combinations(start_x, start_y)
            ends = make_combinations(end_x, end_y)

            for point1, point2 in zip(starts,ends):
                if point1 in symbol_list:
                    filtered_list.append(key)
                    break

                if point2 in symbol_list:
                    filtered_list.append(key)
                    break

def filter_numbers_b():

    for key in numbers.keys():

        for value in numbers[key]:

            start, end = value
            start_x, start_y = start
            end_x, end_y = end

            starts = make_combinations(start_x, start_y)
            ends = make_combinations(end_x, end_y)

            for point1, point2 in zip(starts,ends):
                if point1 in symbol_list:

                    if point1 not in filtered_list.keys():
                        filtered_list[point1] = [key]
                    else:
                        filtered_list[point1].append(key)
                    break

                if point2 in symbol_list:
                    if point2 not in filtered_list.keys():
                        filtered_list[point2] = [key]
                    else:
                        filtered_list[point2].append(key)
                    break


with open("./Data/data_dag3.txt") as f:
    content = f.readlines()

for i, line in enumerate(content):

    number = ""
    start = (i,0)
    end = (i,0)

    for j, char in enumerate(line):

        if char in answer:
            if number == "":
                start = (i,j)

            number += char
        elif char == '.':
            if number == "":
                continue
            if number not in numbers.keys():
                numbers[number] = [(start, end)]
            else:
                numbers[number].append((start, end))
            number = ""
        else:
            if number != "":
                if number not in numbers.keys():
                    numbers[number] = [(start, end)]
                else:
                    numbers[number].append((start, end))
                number = ""

            if char == "\n":
                continue

            symbol_list.append((i,j))

        end = (i,j)

filter_numbers()

part_number = 0
for number in filtered_list:
    part_number += int(number)

print(part_number)

numbers = {}

symbol_list = []
filtered_list = {}

for i, line in enumerate(content):

    number = ""
    start = (i,0)
    end = (i,0)
    print(line)

    for j, char in enumerate(line):

        if char in answer:
            if number == "":
                start = (i,j)

            number += char
        elif char == '.':
            if number == "":
                continue
            if number not in numbers.keys():
                numbers[number] = [(start, end)]
            else:
                numbers[number].append((start, end))
            number = ""
        else:
            if number != "":
                if number not in numbers.keys():
                    numbers[number] = [(start, end)]
                else:
                    numbers[number].append((start, end))
                number = ""

            if char == '*':
                symbol_list.append((i,j))

        end = (i,j)

filter_numbers_b()

part_number = 0
print(filtered_list)
for key in filtered_list.keys():

    if len(filtered_list[key]) == 2:
        part_number += int(filtered_list[key][0]) * \
            int(filtered_list[key][1])

print(part_number)









