
with open("input2") as f:
    puzzle = f.readlines()
puzzle = [x.strip() for x in puzzle]

answer1 = 0
answer2 = 0

for password in puzzle:
    out = password.split(':')
    r = out[0].split()
    l = r[0].split('-')

    minimum = l[0]
    maximum = l[1]

    key = r[1]
    word = out[1]

    contain = 0
    if word[int(minimum)] == key:
        contain += 1
    if word[int(maximum)] == key:
        contain += 1
    if contain == 1:
        answer2 += 1

    count = 0
    for i in word:
        if i == key:
            count = count + 1
    if count >= int(minimum) and count <= int(maximum):
        answer1 += 1

print("1 answer : " + str(answer1))
print("2 answer : " + str(answer2))
