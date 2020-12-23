def main():
    example = readInput("example")
    realInput = readInput("input")
    print(getNthInSeries(example, 2020))
    print(getNthInSeries(realInput, 2020))

    print(getNthInSeries(example, 30000000))
    print(getNthInSeries(realInput, 30000000))

def getNthInSeries(startingNumbers, n):
    lastIndexSeenDict = dict(zip(startingNumbers, range(len(startingNumbers))))
    lastNumber = startingNumbers[-1]
    for i in range(len(startingNumbers), n):
        if lastNumber not in lastIndexSeenDict:
            lastIndexSeenDict[lastNumber] = i - 1
            lastNumber = 0
        else:
            previousSeenIndex = lastIndexSeenDict[lastNumber]
            lastIndexSeenDict[lastNumber] = i - 1
            lastNumber = i - 1 - previousSeenIndex

    return lastNumber


def readInput(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    return [int(x) for x in inputFile.read().split(",")]

if __name__ == "__main__":
        main()
