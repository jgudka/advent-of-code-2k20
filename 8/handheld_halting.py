import re
from typing import Dict, List, Set

ACCUMULATOR = "acc"
JUMP = "jmp"
NOOP = "nop"


def main():
    print(getAccumulatorValue1("example"))
    print(getAccumulatorValue1("input"))

    print(getAccumulatorValue2("example"))
    print(getAccumulatorValue2("input"))

def getAccumulatorValue1(inputFileName):
    instructions = readInput(inputFileName)
    return runProgram(instructions)[1]

def getAccumulatorValue2(inputFileName):
    instructions = readInput(inputFileName)
    for i in range(len(instructions)):
        operation = instructions[i][0]
        if operation in [NOOP, JUMP]:
            instructions[i][0] = NOOP if operation == JUMP else NOOP
            result = runProgram(instructions)
            if result[0] == len(instructions):
                return result[1]
            else:
                instructions[i][0] = operation
    return "not found"

def runProgram(instructions):
    accumulator = 0
    visitedSet = set()
    instructionIndex = 0

    while instructionIndex not in visitedSet and instructionIndex < len(instructions):
        visitedSet.add(instructionIndex)
        instruction = instructions[instructionIndex]
        operation = instruction[0]
        argument = instruction[1]
        if operation == ACCUMULATOR:
            accumulator += argument
            instructionIndex += 1
        elif operation == JUMP:
            instructionIndex += argument
        else:
            instructionIndex += 1

    return [instructionIndex, accumulator]

def readInput(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    return [
        [operation, int(argument)] for operation, argument 
        in (line.split(" ", 1) for line in inputFile.read().splitlines())
    ]


if __name__ == "__main__":
        main()
