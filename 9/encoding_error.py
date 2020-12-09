import re
from typing import Dict, List, Set


def main():
    example = readInput("example")
    realInput = readInput("input")

    print(getFirstInvalidNumber(example, 5))
    print(getFirstInvalidNumber(realInput, 25))

    print(getEncryptionWeakness(example, 5))
    print(getEncryptionWeakness(realInput, 25))

def getEncryptionWeakness(numbers: List[int], previousGroupSize: int):
    invalidNumber = getFirstInvalidNumber(numbers, previousGroupSize)
    group = findContiguousGroupWhichMakeSum(invalidNumber, numbers)
    return max(group) + min(group)

def findContiguousGroupWhichMakeSum(total: int, numberList: List[int]) -> List[int]:
    totalIndex = numberList.index(total)
    for i in range(totalIndex):
        runningTotal = numberList[i]
        for j in range (i + 1, totalIndex):
            runningTotal += numberList[j]
            if (runningTotal == total):
                return numberList[i:j]

    return []

def getFirstInvalidNumber(numbers: List[int], previousGroupSize: int):
    for i in range(previousGroupSize, len(numbers)):
        if not canMakeSumFromNumbers(numbers[i], numbers[i - previousGroupSize:i]):
            return numbers[i]

def canMakeSumFromNumbers(sum: int, numberList: List[int]) -> bool:
    for i in range(len(numberList)):
        for j in range (i + 1, len(numberList)):
            if (numberList[i] + numberList[j] == sum):
                return True
    return False

def readInput(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    return [int(line) for line in inputFile.read().splitlines()]


if __name__ == "__main__":
        main()
