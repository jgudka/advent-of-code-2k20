import re
from typing import List


def main():
    print(checkBoardingPass1("example"))
    print(checkBoardingPass1("input"))

    print(checkBoardingPass2("input"))

def checkBoardingPass1(inputFileName):
    boardingPasses = readInput(inputFileName)
    scores = list(map(calculateScore, boardingPasses))
    return max(scores)

def checkBoardingPass2(inputFileName):
    boardingPasses = readInput(inputFileName)
    scores = sorted(map(calculateScore, boardingPasses))
    missingSeat = 0
    for i in range(1, len(scores)):
        if scores[i] != scores[i-1] + 1:
            missingSeat = scores[i] - 1

    return missingSeat

def calculateScore(boardingPass: str) -> int:
    binaryBoardingPass = convertToBinaryString(boardingPass)
    row = int(binaryBoardingPass[:7], 2)
    column = int(binaryBoardingPass[-3:], 2)
    return (row * 8) + column

def convertToBinaryString(boardingPass: str) -> str:
    return ''.join(map(lambda x: '0' if x in ['F', 'L'] else '1', list(boardingPass)))

def readInput(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    return inputFile.read().splitlines()

if __name__ == "__main__":
        main()
