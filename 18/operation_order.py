import re
from enum import Enum
from functools import reduce
from numbers import Number

OPEN_BRACKET = "("
CLOSE_BRACKET = ")"
ADD = "+"
MULTIPLY = "*"

def main():
    example = readInput("example")
    realInput = readInput("input")
    print(getSumOfCalculations(example))
    print(getSumOfCalculations(realInput))

def getSumOfCalculations(calculations):    
    return sum(map(performCalculation, calculations))

def performCalculation(calculation):
    previousOperand = 0
    calcIndex = 0
    operation = ADD
    valuesToMultiply = []
    
    while calcIndex < len(calculation):
        nextItem = calculation[calcIndex]
        if nextItem == OPEN_BRACKET:
            closingBracketIndex = calcIndex + findClosingBracketIndex(calculation[calcIndex:])
            previousOperand += performCalculation(calculation[calcIndex + 1 : closingBracketIndex])
            calcIndex = closingBracketIndex + 1
        elif nextItem == MULTIPLY:
            valuesToMultiply.append(previousOperand)
            previousOperand = 0
            calcIndex += 1
        elif nextItem == ADD:
            calcIndex += 1
        else:
            previousOperand += calculation[calcIndex]
            calcIndex += 1
    
    valuesToMultiply.append(previousOperand)

    return reduce(lambda x, y: x * y, valuesToMultiply)

def performOperation(leftOperand, rightOperand, operation):
    return leftOperand + rightOperand if operation == ADD else leftOperand * rightOperand

def findClosingBracketIndex(calculation):
    openBracketAccumulator = 1
    for i in range(1, len(calculation)):
        if calculation[i] == OPEN_BRACKET:
            openBracketAccumulator += 1
        elif calculation[i] == CLOSE_BRACKET:
            openBracketAccumulator -= 1
        
        if openBracketAccumulator == 0:
            return i

def readInput(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    return [
        [int(x) if x.isdigit() else x for x in list(re.sub('[\s]', '', line))]
        for line in inputFile.read().splitlines()
    ]

if __name__ == "__main__":
        main()
