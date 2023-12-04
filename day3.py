from string import digits, punctuation

punctuation = punctuation.replace(".", "")

with open("day3.txt", "r") as f:
    c = f.readlines()

s = 0

for i in range(len(c)):
    current_line = c[i]
    current_nums = []
    current_num = {}
    found_num = False
    for j in range(len(current_line)):
        if current_line[j] not in digits:
            found_num = False
            current_nums.append(current_num)
            current_num = {}
            continue
        if current_line[j] in digits:
            found_num = True
        current_num[j] = current_line[j]
    while True:
        try:
            current_nums.remove({})
        except:
            break
    for k in current_nums:
        valid = False
        for l in k.keys():
            if i != 0:
                if c[i-1][l] in punctuation:
                    valid = True
                    break
            if i != len(c) - 1:
                if c[i+1][l] in punctuation:
                    valid = True
                    break
            if l != 0:
                if c[i][l-1] in punctuation:
                    valid = True
                    break
            if l != len(current_line) - 1:
                if c[i][l+1] in punctuation:
                    valid = True
                    break
            if i != 0 and l != len(current_line) - 1:
                if c[i-1][l+1] in punctuation:
                    valid = True
                    break
            if i != 0 and l != 0:
                if c[i-1][l-1] in punctuation:
                    valid = True
                    break
            if i != len(c) - 1 and l != 0:
                if c[i+1][l-1] in punctuation:
                    valid = True
                    break
            if i != len(c) - 1 and l != len(current_line) - 1:
                if c[i+1][l+1] in punctuation:
                    valid = True
                    break
        if valid:
            s += int("".join(list(k.values())))

gear_rat = 0
numstar = 0
for i in range(len(c)):
    current_line = c[i]
    for j in range(len(current_line)):
        if current_line[j] == "*":
            numstar += 1
            nums = []
            if i != 0:
                break_l = False
                if c[i-1][j] in digits:
                    break_l = True
                    num = {}
                    num[j] = c[i-1][j]
                    for k in range(j-1, -1, -1):
                        if c[i-1][k] in digits:
                            num[k] = c[i-1][k]
                        else:
                            break
                    for k in range(j+1, len(current_line)):
                        if c[i-1][k] in digits:
                            num[k] = c[i-1][k]
                        else:
                            break
                    a = list(num.keys())
                    a.sort()
                    nums.append(int("".join([num[i] for i in a])))
                elif j != len(current_line) - 1 and c[i-1][j+1] in digits and not break_l:
                    num = {}
                    num[j+1] = c[i-1][j+1]
                    for k in range(j, -1, -1):
                        if c[i-1][k] in digits:
                            num[k] = c[i-1][k]
                        else:
                            break
                    for k in range(j+2, len(current_line)):
                        if c[i-1][k] in digits:
                            num[k] = c[i-1][k]
                        else:
                            break
                    a = list(num.keys())
                    a.sort()
                    nums.append(int("".join([num[i] for i in a])))
                if j != 0 and c[i-1][j-1] in digits and not break_l:
                    num = {}
                    num[j-1] = c[i-1][j-1]
                    for k in range(j-2, -1, -1):
                        if c[i-1][k] in digits:
                            num[k] = c[i-1][k]
                        else:
                            break
                    for k in range(j, len(current_line)):
                        if c[i-1][k] in digits:
                            num[k] = c[i-1][k]
                        else:
                            break
                    a = list(num.keys())
                    a.sort()
                    nums.append(int("".join([num[i] for i in a])))
            if i != len(c) - 1:
                break_l = False
                if c[i+1][j] in digits:
                    break_l = True
                    num = {}
                    num[j] = c[i+1][j]
                    for k in range(j-1, -1, -1):
                        if c[i+1][k] in digits:
                            num[k] = c[i+1][k]
                        else:
                            break
                    for k in range(j+1, len(current_line)):
                        if c[i+1][k] in digits:
                            num[k] = c[i+1][k]
                        else:
                            break
                    a = list(num.keys())
                    a.sort()
                    nums.append(int("".join([num[i] for i in a])))
                if j != len(current_line) - 1 and c[i+1][j+1] in digits and not break_l:
                    num = {}
                    num[j+1] = c[i+1][j+1]
                    for k in range(j, -1, -1):
                        if c[i+1][k] in digits:
                            num[k] = c[i+1][k]
                        else:
                            break
                    for k in range(j+2, len(current_line)):
                        if c[i+1][k] in digits:
                            num[k] = c[i+1][k]
                        else:
                            break
                    a = list(num.keys())
                    a.sort()
                    nums.append(int("".join([num[i] for i in a])))
                if j != 0 and c[i+1][j-1] in digits and not break_l:
                    num = {}
                    num[j-1] = c[i+1][j-1]
                    for k in range(j-2, -1, -1):
                        if c[i+1][k] in digits:
                            num[k] = c[i+1][k]
                        else:
                            break
                    for k in range(j, len(current_line)):
                        if c[i+1][k] in digits:
                            num[k] = c[i+1][k]
                        else:
                            break
                    a = list(num.keys())
                    a.sort()
                    nums.append(int("".join([num[i] for i in a])))
            if j != 0:
                if current_line[j-1] in digits:
                    num = {}
                    num[j-1] = current_line[j-1]
                    for k in range(j-2, -1, -1):
                        if current_line[k] in digits:
                            num[k] = current_line[k]
                        else:
                            break
                    a = list(num.keys())
                    a.sort()
                    nums.append(int("".join([num[i] for i in a])))
            if j != len(current_line) - 1:
                if current_line[j+1] in digits:
                    num = {}
                    num[j+1] = current_line[j+1]
                    for k in range(j+2, len(current_line)):
                        if current_line[k] in digits:
                            num[k] = current_line[k]
                        else:
                            break
                    a = list(num.keys())
                    a.sort()
                    nums.append(int("".join([num[i] for i in a])))
            print(nums)
            if len(nums) == 2:
                gear_rat += nums[0] * nums[1]


print(s)
print(gear_rat)
print(numstar)