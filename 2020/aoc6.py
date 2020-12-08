with open("input6") as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]

group = []

answer1 = 0
answer2 = 0
for line in lines:
    if line == "" or line == -1:
        answers = []
        count = 0
        for person in group:
            count += 1
            for answer in person:
                answers.append(answer)

        answerString = ''.join(answers)
        myset = set(answers)
        uniqeAnswers = list(myset)
        for a in uniqeAnswers:
            if answerString.count(a) == count:
                answer2 += 1

        answer1 += len(uniqeAnswers)
        group = []

    else:
        group.append(line)

print("1 answer : " + str(answer1))
print("2 answer : " + str(answer2))
