
with open("input3") as f:
    row = f.readlines()
row = [x.strip() for x in row]

lineLen = len(row[0])
tree = 0
move = 0
answer1 = 0
answer2 = 1

# Right 3, down 1
for i in range(len(row) - 1):
    move = (move + 3) % lineLen
    if row[i+1][move] == '#':
        tree += 1

answer1 = tree
answer2 = answer2 * tree

tree = 0
move = 0
# Right 1, down 1.
for i in range(len(row) - 1):
    move = (move + 1) % lineLen
    if row[i+1][move] == '#':
        tree += 1

answer2 = answer2 * tree

tree = 0
move = 0
# Right 5, down 1.
for i in range(len(row) - 1):
    move = (move + 5) % lineLen
    if row[i+1][move] == '#':
        tree += 1

answer2 = answer2 * tree

tree = 0
move = 0
# Right 7, down 1.
for i in range(len(row) - 1):
    move = (move + 7) % lineLen
    if row[i+1][move] == '#':
        tree += 1

answer2 = answer2 * tree

tree = 0
move = 0
# Right 1, down 2.
for i in range(int((len(row)-1) / 2)):
    move = (move + 1) % lineLen
    if row[(i+1)*2][move] == '#':
        tree += 1

answer2 = answer2 * tree

print("1 answer : " + str(answer1))
print("2 answer : " + str(answer2))
