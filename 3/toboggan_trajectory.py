from functools import reduce


def main():
    # print(calculateTrajectory1("example"))
    # print(calculateTrajectory1("input"))

    print(calculateTrajectory2("example"))
    print(calculateTrajectory2("input"))

def calculateTrajectory1(inputFileName):
    grid = readInput(inputFileName)
    print(grid)

    gridWidth = len(grid[0])
    rightStep = 3

    rightPosition = 0
    treesPassed = 0

    for i in range(len(grid)):
        if grid[i][rightPosition % gridWidth] == "#":
            treesPassed += 1
        rightPosition += rightStep

    return treesPassed


def calculateTrajectory2(inputFileName):
    rightSteps = [1, 3, 5, 7, 0.5]
    grid = readInput(inputFileName)
    trees = [treesEncountered(grid, step) for step in rightSteps]
    return reduce(lambda x, y: x*y, trees)


def treesEncountered(grid, rightStep):
    gridWidth = len(grid[0])

    rightPosition = 0
    treesPassed = 0

    for i in range(len(grid)):
        if rightPosition % 1 == 0:
            if grid[i][int(rightPosition % gridWidth)] == "#":
                treesPassed += 1
        rightPosition += rightStep

    return treesPassed



def readInput(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    unparsedLines = inputFile.read().splitlines()
    return [list(line) for line in unparsedLines]

if __name__ == "__main__":
        main()
