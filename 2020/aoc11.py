with open("input11") as f:
    puzzle = f.readlines()
puzzle = [x.strip() for x in puzzle]

currentSeats = puzzle[:]
nextSeats = []
width = len(currentSeats[0])
height = len(currentSeats)
answer = 0


# for answer 1
def getAdjeccentCount(x, y):
    result = 0
    for i in range(3):
        sx = i-1
        for j in range(3):
            sy = j-1
            v = 1
            if sx == 0 and sy == 0:
                continue
            point = [x+sx*v, y+sy*v]
            if point[0] >= 0 and point[0] < width and point[1] >= 0 and point[1] < height:
                if(currentSeats[point[1]][point[0]] == "#"):
                    result += 1

    return result


# for answer 2
def getAdjeccentCountFarVision(x, y):
    result = 0
    for i in range(3):
        sx = i-1
        for j in range(3):
            sy = j-1
            v = 1
            while sx != 0 or sy != 0:
                point = [x+sx*v, y+sy*v]
                if point[0] < 0 or point[0] >= width or point[1] < 0 or point[1] >= height:
                    break
                if(currentSeats[point[1]][point[0]] == "L"):
                    break
                if(currentSeats[point[1]][point[0]] == "#"):
                    result += 1
                    break
                v += 1

    return result


def Change():
    global nextSeats
    global currentSeats
    nextSeats = []
    wasChange = 0
    for row in range(height):
        rowStr = ""
        for seat in range(width):
            if currentSeats[row][seat] == ".":
                rowStr += "."
                continue
            # RULE 1
            if currentSeats[row][seat] == "L":
                if getAdjeccentCountFarVision(seat, row) == 0:
                    rowStr += "#"
                    wasChange = 1
                    continue
                # if getAdjeccentCount(seat, row) == 0:
                #     rowStr += "#"
                #     wasChange = 1
                #     continue

            # RULE 2
            if currentSeats[row][seat] == "#":
                if getAdjeccentCountFarVision(seat, row) >= 5:
                    rowStr += "L"
                    wasChange = 1
                    continue
                # if getAdjeccentCount(seat, row) >= 5:
                #     rowStr += "L"
                #     wasChange = 1
                #     continue

            rowStr += currentSeats[row][seat]
        nextSeats.append(rowStr)

    currentSeats = nextSeats[:]
    return wasChange


while(Change()):
    pass

for row in range(height):
    for seat in range(width):
        if currentSeats[row][seat] == "#":
            answer += 1

print("answer : " + str(answer))
