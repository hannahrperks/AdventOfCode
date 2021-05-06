f = open(r'C:\Users\perkshan\Learning\Python\AdventOfCode\day_four_input.txt', 'r')
day_four_input = f.readlines()
f.close()

in_data = []
for i in day_four_input:
        i = i.replace('\n', '')
        in_data.append(i)

print(in_data)
print('------------------------------------------')

def day_four_part_one(in_data):
    pass


def day_four_part_two(in_data):
    pass


print(day_four_part_one(in_data))