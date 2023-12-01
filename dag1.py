import re

answer = ['0','1','2','3','4','5','6',\
        '7','8','9']

expressions = ['0','1','2','3','4','5','6',\
        '7','8','9', 'zero', 'one','two','three', 'four', \
        'five','six','seven','eight','nine']

translator = {'zero':'0', 'one':'1', 'two':'2',\
        'three':'3','four':'4','five':'5','six':'6',\
        'seven':'7','eight':'8','nine':'9'}

calibration_code = 0

with open("./Data/data_dag1b.txt") as f:
    content = f.readlines()

for line in content:
    decoding = [char for char in line if \
            char in answer]
    if len(decoding) == 0:
        continue
    calibration_number = decoding[0] + decoding[-1]
    calibration_code += int(calibration_number)

#print(calibration_code)

calibration_code = 0

for line in content:
    print(line)
    search_result = []
    for i in range(len(line)):

        subline = line[i:len(line)]
        print(subline)

        for exp in expressions:
            search = re.search(exp,subline)
            if search == None:
                continue
            span_start, span_end = search.span()
            search_result.append((span_start+i, span_end+i))


    search_result.sort()
    print(search_result)
    decoded_result = []

    for result in search_result:
        span_start, span_end = result
        decoded_result.append(line[span_start:span_end])

    print(decoded_result)

    first_digit = decoded_result[0]
    second_digit = decoded_result[-1]
    if first_digit in translator.keys():
        first_digit = translator[first_digit]

    if second_digit in translator.keys():
        second_digit = translator[second_digit]

    calibration_number = first_digit + second_digit
    print(calibration_number)
    calibration_code += int(calibration_number)

print(calibration_code)






