
with open("input9") as f:
    puzzle = f.readlines()
puzzle = [int(x.strip()) for x in puzzle]

puzzle.reverse()
answer1 = 0
answer2 = 0
correct = []
top_max = 25

for i in range(len(puzzle)-top_max):
    for a in range(i + 1, min(i + top_max + 1, len(puzzle))):
        for b in range(i + 1, a):
            if puzzle[a] + puzzle[b] == puzzle[i]:
                correct.append(puzzle[i])
                break
        else:
            continue
        break


list_difference = []
for item in range(len(puzzle)-top_max):
    if puzzle[item] not in correct:
        list_difference.append(puzzle[item])

answer1 = list_difference[0]


puzzle.reverse()
for b in range(len(puzzle)):
    accumulator = 0
    for a in range(b, len(puzzle)):
        if puzzle[a] == answer1:
            break
        accumulator += puzzle[a]
        if(accumulator == answer1):
            answer2 = puzzle[b] + puzzle[a-1]
            break
        elif(accumulator > answer1):
            break

print("1 answer : " + str(answer1))
print("2 answer : " + str(answer2))
