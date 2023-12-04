import numpy as np

with open("./Data/data_dag4.txt") as f:
    content = f.readlines()


total_score = 0

for line in content:

    card = line.split(':')
    numbers = card[1].split('|')

    score = 0
    for num in numbers[1].split():

        if num in numbers[0].split():

            if score == 0:
                score = 1
            else:
                score *= 2

    total_score += score

print(total_score)


def copies(cards, start_index, stop_index):

    total_counts = 0

    for i in range(start_index, stop_index):

        card = cards[i].split(':')
        numbers = card[1].split('|')

        counts = 0
        for num in numbers[1].split():

            if num in numbers[0].split():
                counts += 1

        copy_counts = copies(cards, i+1, i + counts+1)

        total_counts += counts + copy_counts

    return total_counts

print(copies(content,0,len(content))+len(content))



