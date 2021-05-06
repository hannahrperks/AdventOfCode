f = open(r'C:\Users\perkshan\Learning\Python\AdventOfCode\day_three_input.txt', 'r')
day_three_input = f.readlines()
f.close()

in_data = []
for i in day_three_input:
        i = i.replace('\n', '')
        in_data.append(i)

def day_three_part_one(in_data):
    col_idx = 0
    row_idx = 0
    max_col_idx = len(in_data[0])
    ans = 0
    while row_idx < len(in_data):
        pos = in_data[row_idx][col_idx]
        if pos == '#':
            ans += 1
        col_idx += 3
        row_idx += 1
        if col_idx >= max_col_idx:
            col_idx = col_idx - max_col_idx
    return ans


def day_three_part_two(in_data):
    ans = 1
    moves = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    n = 0
    while n < len(moves):
        col_idx = 0
        row_idx = 0
        max_col_idx = len(in_data[0])
        cnt = 0
        while row_idx < len(in_data):
            pos = in_data[row_idx][col_idx]
            if pos == '#':
                cnt += 1
            col_idx += moves[n][0]
            row_idx += moves[n][1]
            if col_idx >= max_col_idx:
                col_idx = col_idx - max_col_idx
        ans *= cnt
        n += 1
    return ans

print(day_three_part_one(in_data))
print(day_three_part_two(in_data))