import math
with open("input10") as f:
    puzzle = f.readlines()
puzzle = [int(x.strip()) for x in puzzle]

answer1 = 0
answer2 = 0

puzzle.append(0)
puzzle.sort()
puzzle_length = len(puzzle)
diff_array = []


differenc_count = [1, 1, 1, 1]
for i in range(1, puzzle_length-1):
    differenc_count[abs(puzzle[i] - puzzle[i+1])] += 1

for i in range(0, puzzle_length-1):
    diff_array.append(abs(puzzle[i] - puzzle[i+1]))


answer1 = differenc_count[1] * differenc_count[3]


def getValueJump(array, f):
    result = 0
    for i in range(f+1):
        result += array[i]
    return result


def getValue(array):
    if(len(array) < 2):
        return 1
    result = 1
    for i in range(1, 4):
        if(i < len(array)):
            if(getValueJump(array, i) <= 3):
                result += getValue(array[i:])
    return result


# from internet
size = len(diff_array)
idx_list = [idx + 1 for idx, val in
            enumerate(diff_array) if val == 3]


res = [diff_array[i: j] for i, j in
       zip([0] + idx_list, idx_list +
           ([size] if idx_list[-1] != size else []))]
# ------------------

for i in res:
    for a in range(len(i)):
        if i[a] == 3:
            i.pop(a)

answer2 = 1
for i in res:
    answer2 *= getValue(i)

print("1 answer : " + str(answer1))
print("2 answer : " + str(answer2))
