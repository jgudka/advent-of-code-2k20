I_POSITION = "I Position"
J_POSITION = "J Position"
DIRECTION = "Direction"

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
        DIRECTION: EAST
    }
    for instruction in instructions:
        applyInstruction(shipPosition, instruction)
    print(shipPosition)
    return abs(shipPosition[I_POSITION]) + abs(shipPosition[J_POSITION])

def applyInstruction(shipPosition, instruction):
    action = instruction[0]
    value = instruction[1]
    if action in DIRECTIONS:
        moveShip(shipPosition, action, value)
    elif action == FORWARD:
        moveShip(shipPosition, shipPosition[DIRECTION], value)
    elif action in [LEFT, RIGHT]:
        rotateShip(shipPosition, action, value)

def moveShip(shipPosition, direction, value):
    directionVector = DIRECTION_VECTORS[direction]
    shipPosition[I_POSITION] += directionVector[0] * value
    shipPosition[J_POSITION] += directionVector[1] * value

def rotateShip(shipPosition, direction, value):
    turningIndex = 1 if direction == RIGHT else -1
    directionIndex = (DIRECTIONS.index(shipPosition[DIRECTION]) + (turningIndex * value/90)) % 4
    shipPosition[DIRECTION] = DIRECTIONS[int(directionIndex)]

def readInput(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    return [[line[0], int(line[1:])] for line in inputFile.read().splitlines()]

if __name__ == "__main__":
        main()
