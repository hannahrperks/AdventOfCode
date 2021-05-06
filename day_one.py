import itertools

f = open(r'C:\Users\perkshan\Learning\Python\AdventOfCode\day_one_input.txt', 'r')
day_one_input = f.readlines()
f.close()

in_data = []
for i in day_one_input:
        i = int(i.replace('\n', ''))
        in_data.append(i)

def day_one_part_one(in_data):
    combi_list = list(itertools.combinations(in_data,2))
    idx = 0
    for idx in range(len(combi_list)):
        x = combi_list[idx][0]
        y = combi_list[idx][1]
        if x + y == 2020:
            return f'The two entries are {x} and {y}, the solution is {x*y}'
        else:
            idx += 1


def day_one_part_two(in_data):
    combi_list = list(itertools.combinations(in_data,3))
    idx = 0
    for idx in range(len(combi_list)):
        x = combi_list[idx][0]
        y = combi_list[idx][1]
        z = combi_list[idx][2]
        if x + y + z == 2020:
            return f'The three entries are {x}, {y} and {z}, the solution is {x*y*z}'
        else:
            idx += 1


print(day_one_part_one(in_data))
print(day_one_part_two(in_data))
