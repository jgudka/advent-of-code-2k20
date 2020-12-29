from pocketDimension import PocketDimension


def main():
    example = readInput("example")
    realInput = readInput("input")

    examplePocketDimension = PocketDimension(example)
    examplePocketDimension.simulateCycles(6)
    print(examplePocketDimension.countActiveCubes())

    pocketDimension = PocketDimension(realInput)
    pocketDimension.simulateCycles(6)
    print(pocketDimension.countActiveCubes())

def readInput(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    return [list(line) for line in inputFile.read().splitlines()]

if __name__ == "__main__":
        main()
