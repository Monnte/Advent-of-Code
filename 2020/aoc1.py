
with open("input1") as f:
    array = f.readlines()
array = [int(x.strip()) for x in array]

answer1 = 0
answer2 = 0

for n in range(len(array)):
    for b in range(len(array)):
        if array[n] + array[b] == 2020:
            answer1 = array[n] * array[b]
        for a in array:
            if a + array[n] + array[b] == 2020:
                answer2 = a*array[n]*array[b]


print("1 answer : " + str(answer1))
print("1 answer : " + str(answer2))
