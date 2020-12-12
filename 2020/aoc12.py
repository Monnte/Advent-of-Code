import math
with open("input12") as f:
    puzzle = f.readlines()
puzzle = [x.strip() for x in puzzle]

direction = "E"

x = 0
y = 0
waypoint_x = x + 10
waypoint_y = y + 1
instructions = []

for a in puzzle:
    action = a[0]
    number = int(a[1:])
    instructions.append([action, number])


def moveShip(number):
    global x
    global y
    global waypoint_x
    global waypoint_y
    x += number * waypoint_x
    y += number * waypoint_y


def moveWaypoint(direction, num):
    global waypoint_x
    global waypoint_y
    if direction == "N":
        waypoint_y += num
    elif direction == "S":
        waypoint_y -= num
    elif direction == "W":
        waypoint_x -= num
    elif direction == "E":
        waypoint_x += num


def changeDirectionShip(angle, where):
    global direction
    directions = ["E", "S", "W", "N"]
    currentDirection = 0
    for i in range(len(directions)):
        if directions[i] == direction:
            currentDirection = i
    if where == "R":
        direction = directions[(currentDirection + math.floor(angle / 90)) % 4]
    elif where == "L":
        direction = directions[(currentDirection - math.floor(angle / 90)) % 4]


def rotate(x, y, xo, yo, angle):
    xr = math.cos(angle)*(x-xo)-math.sin(angle)*(y-yo) + xo
    yr = math.sin(angle)*(x-xo)+math.cos(angle)*(y-yo) + yo
    return int(round(xr)), int(round(yr))


def changeDirectionWaypoint(angle, where):
    global waypoint_x
    global waypoint_y
    global x
    global y
    if where == "R":
        angle = -angle
    angle = math.radians(angle)

    waypoint_x, waypoint_y = rotate(waypoint_x, waypoint_y, 0, 0, angle)


for i in instructions:
    if i[0] != "L" and i[0] != "R" and i[0] != "F":
        moveWaypoint(i[0], i[1])
    elif i[0] == "R":
        changeDirectionWaypoint(i[1], "R")
    elif i[0] == "L":
        changeDirectionWaypoint(i[1], "L")
    else:
        moveShip(i[1])
    # print("wayX: ", waypoint_x, " wayY: ", waypoint_y)
    # print("shipX: ", x, " shipY: ", y)
    # print("---------------------------")

answer = abs(x) + abs(y)
print("answer : " + str(answer))
