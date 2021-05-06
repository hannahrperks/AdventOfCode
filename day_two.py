f = open(r'C:\Users\perkshan\Learning\Python\AdventOfCode\day_two_input.txt', 'r')
day_two_input = f.readlines()
f.close()

in_data = []
for i in day_two_input:
        i = i.replace('\n', '')
        in_data.append(i)

def day_two_part_one(in_data):
    password_lst = []
    ans = 0
    for i in in_data:
        x = i.split(': ', 1)
        password_lst.append(x)
    for pswd in password_lst:
        cnt = 0
        policy = pswd[0].split()
        min_cnt = int((policy[0].split('-'))[0])
        max_cnt = int((policy[0].split('-'))[1])
        for l in pswd[1]:
            if l == policy[1]:
                cnt += 1
        if min_cnt <= cnt <= max_cnt:
            ans += 1
    return ans


def day_two_part_two(in_data):
    password_lst = []
    ans = 0
    for i in in_data:
        x = i.split(': ', 1)
        password_lst.append(x)
    for pswd in password_lst:
        cnt = 0
        policy = pswd[0].split()
        indxs = (policy[0].split('-'))
        for n in indxs:
            idx = int(n)-1
            if pswd[1][idx] == policy[1]:
                cnt += 1
        if cnt == 1:
            ans += 1
    return ans


print(day_two_part_one(in_data))
print(day_two_part_two(in_data))