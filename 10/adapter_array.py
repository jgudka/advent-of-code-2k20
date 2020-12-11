import re
from typing import Dict, List, Set


def main():
    print(getJoltageDifferenceProduct("example"))
    print(getJoltageDifferenceProduct("input"))

    print(getJoltageCombinations("example"))
    print(getJoltageCombinations("input"))

def getJoltageDifferenceProduct(inputFileName):
    joltages = readInput(inputFileName)
    differences = getJoltageDifferences(joltages)

    return differences.count(1) * differences.count(3)

def getJoltageCombinations(inputFileName):
    joltages = readInput(inputFileName)
    differences = getJoltageDifferences(joltages)
    consecutiveOnes = 0
    combinations = 1
    for i in range(len(differences)):
        if differences[i] == 1:
            consecutiveOnes += 1
        else:
            if consecutiveOnes > 1:
                combinations = combinations * getCombinationsForConsecutiveDifferenceOfOne(consecutiveOnes)
            consecutiveOnes = 0

    return combinations

def getCombinationsForConsecutiveDifferenceOfOne(consecutiveOnes):
    if consecutiveOnes == 1:
        return 1
    elif consecutiveOnes == 2:
        return 2
    elif consecutiveOnes == 3:
        return 4
    else:
        return sum([
            getCombinationsForConsecutiveDifferenceOfOne(consecutiveOnes - 1),
            getCombinationsForConsecutiveDifferenceOfOne(consecutiveOnes - 2),
            getCombinationsForConsecutiveDifferenceOfOne(consecutiveOnes - 3)
        ])

def getJoltageDifferences(joltages):
    joltages.sort()
    joltages.insert(0, 0)
    joltages.append(joltages[-1] + 3)

    differences = list()

    for i in range(1, len(joltages)):
        difference = joltages[i] - joltages[i -1]
        differences.append(difference)

    return differences

def readInput(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    return [int(line) for line in inputFile.read().splitlines()]

if __name__ == "__main__":
        main()
