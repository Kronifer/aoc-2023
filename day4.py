with open("day4.txt", "r") as f:
    c = f.readlines()

c = [[i.split(":")[1].strip().split(" | ")[0].split(" "), i.split(":")[1].strip().split(" | ")[1].split(" "), int(i.split(":")[0].split(" ")[-1].strip())-1, 1] for i in c]

for i in range(len(c)):
    curr_set = c[i][:2]
    for j in curr_set:
        for k in range(len(j))[::-1]:
            if j[k] == "":
                del j[k]
score = 0

for i in c:
    winning_nums = i[0]
    nums = i[1]
    points = 0
    wins = 1
    for i in winning_nums:
        if i in nums:
            if points == 0:
                points = 1
                continue
            points *= 2
    score += points

for i in range(len(c)):
    winning_nums = c[i][0]
    nums = c[i][1]
    card_num = c[i][2]
    matching = 0
    for j in winning_nums:
        if j in nums:
            matching += 1
    for j in range(card_num+1, card_num+1+matching):
        c[j][3] += (c[i][3])

copies = 0
for i in c:
    copies += i[3]

print(score)
print(copies)