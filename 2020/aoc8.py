import copy
with open("input8") as f:
    codeIns = f.readlines()
codeIns = [x.strip() for x in codeIns]

codeArray = []
for code in codeIns:
    name = code[:3]
    value = code[4:]
    codeArray.append([name, value])


# part 1
i = 0
instrcutionUsed = {"", ""}
acumulator = 0
while i < len(codeArray):
    if i in instrcutionUsed:
        print("1 answer : " + str(acumulator))
        break
    instrcutionUsed.add(i)
    if codeArray[i][0] == "acc":
        acumulator += int(codeArray[i][1])
    if codeArray[i][0] == "jmp":
        i += int(codeArray[i][1])
    else:
        i += 1


# part 2
for index in range(len(codeArray)):
    codeArrayTry = copy.deepcopy(codeArray)
    instrcutionUsed = {"", ""}
    i = 0
    err = 1
    if codeArray[index][0] == "nop":
        codeArrayTry[index][0] = "jmp"
    elif codeArray[index][0] == "jmp":
        codeArrayTry[index][0] = "nop"

    acumulator = 0

    while i < len(codeArrayTry):
        if i in instrcutionUsed:
            err = 0
            break
        instrcutionUsed.add(i)
        if codeArrayTry[i][0] == "acc":
            acumulator += int(codeArrayTry[i][1])
        if codeArrayTry[i][0] == "jmp":
            i += int(codeArrayTry[i][1])
        else:
            i += 1

    if err:
        print("2 answer : " + str(acumulator))
