I_POSITION = "I Position"
J_POSITION = "J Position"

NORTH = "N"
EAST = "E"
SOUTH = "S"
WEST = "W"
FORWARD = "F"
LEFT = "L"
RIGHT = "R"

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

DIRECTION_VECTORS = {
    NORTH: [0, 1],
    EAST: [1, 0],
    SOUTH: [0, -1],
    WEST: [-1, 0]
}

def main():
    example = readInput("example")
    realInput = readInput("input")
    print(calculateManhattanDistance(example))
    print(calculateManhattanDistance(realInput))

def calculateManhattanDistance(instructions):
    shipPosition = {
        I_POSITION: 0,
        J_POSITION: 0,
    }
    waypointPosition = {
        I_POSITION: 10,
        J_POSITION: 1,
    }
    for instruction in instructions:
        applyInstruction(shipPosition, waypointPosition, instruction)
    
    return abs(shipPosition[I_POSITION]) + abs(shipPosition[J_POSITION])

def applyInstruction(shipPosition, waypointPosition, instruction):
    action = instruction[0]
    value = instruction[1]
    if action in DIRECTIONS:
        moveWaypoint(waypointPosition, action, value)
    elif action == FORWARD:
        moveShip(shipPosition, waypointPosition, value)
    elif action in [LEFT, RIGHT]:
        rotateWaypoint(waypointPosition, action, value)

def moveWaypoint(waypointPosition, direction, value):
    directionVector = DIRECTION_VECTORS[direction]
    waypointPosition[I_POSITION] += directionVector[0] * value
    waypointPosition[J_POSITION] += directionVector[1] * value

def moveShip(shipPosition, waypointPosition, value):
    shipPosition[I_POSITION] += waypointPosition[I_POSITION] * value
    shipPosition[J_POSITION] += waypointPosition[J_POSITION] * value

def rotateWaypoint(waypointPosition, direction, value):
    initialIPosition = waypointPosition[I_POSITION]
    initialJPosition = waypointPosition[J_POSITION]

    oldIDirection = EAST if initialIPosition > 0 else WEST
    oldJDirection = NORTH if initialJPosition > 0 else SOUTH

    turningDirection = 1 if direction == RIGHT else -1

    newIDirection = DIRECTIONS[int((DIRECTIONS.index(oldIDirection) + (turningDirection * value/90)) % 4)]
    newJDirection = DIRECTIONS[int((DIRECTIONS.index(oldJDirection) + (turningDirection * value/90)) % 4)]


    if newIDirection in [EAST, WEST]:
        waypointPosition[I_POSITION] = abs(initialIPosition) if newIDirection == EAST else -abs(initialIPosition)
        waypointPosition[J_POSITION] = abs(initialJPosition) if newJDirection == NORTH else -abs(initialJPosition)
    else:
        waypointPosition[I_POSITION] = abs(initialJPosition) if newJDirection == EAST else -abs(initialJPosition)
        waypointPosition[J_POSITION] = abs(initialIPosition) if newIDirection == NORTH else -abs(initialIPosition)


def readInput(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    return [[line[0], int(line[1:])] for line in inputFile.read().splitlines()]

if __name__ == "__main__":
        main()
