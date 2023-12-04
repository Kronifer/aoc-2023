with open("day2.txt", "r") as f:
    inp = f.readlines()
    inp = [i.split(":") for i in inp]
    inp = [[int(i[0].split(" ")[1]), i[1].strip().split(";")] for i in inp]
    for i in range(len(inp)):
        nums = []
        for j in range(len(inp[i][1])):
            nums_in_current_set = [0, 0, 0]
            curr = inp[i][1][j]
            curr = [i.strip().split(" ") for i in curr.split(",")]
            for l in curr:
                if l[1] == "red":
                    nums_in_current_set[0] = int(l[0])
                elif l[1] == "green":
                    nums_in_current_set[1] = int(l[0])
                else:
                    nums_in_current_set[2] = int(l[0])
            nums.append(nums_in_current_set)
        inp[i][1] = nums
    
SUM = 0

R = 12
G = 13
B = 14

POWERS = 0

for i in inp:
    valid = True
    for j in i[1]:
        if j[0] > R:
            valid = False
            break
        if j[1] > G:
            valid = False
            break
        if j[2] > B:
            valid = False
            break
    if valid:
        SUM += i[0]

for i in inp:
    min_n = [0, 0, 0]
    for j in i[1]:
        if j[0] > min_n[0]:
            min_n[0] = j[0]
        if j[1] > min_n[1]:
            min_n[1] = j[1]
        if j[2] > min_n[2]:
            min_n[2] = j[2]
    POWERS += min_n[0] * min_n[1] * min_n[2]
print(SUM)
print(POWERS)


