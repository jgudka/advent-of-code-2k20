import math
import re
from functools import reduce

MODULO = "modulo"
REMAINDER = "remainder"

def main():
    print(getEarliestBusTime1("example"))
    print(getEarliestBusTime1("input"))

    print(getEarliestBusTime2("example"))
    print(getEarliestBusTime2("input"))


def getEarliestBusTime1(input):
    notes = readInput1(input)
    arrivalTime = notes["arrivalTime"]
    busTimes = notes["busTimes"]
    waitTimes = { }
    for busTime in busTimes:
        quotient = arrivalTime / busTime
        waitTime = int((math.ceil(quotient) - quotient) * busTime)
        waitTimes[busTime] = waitTime
    sortedWaitTimes = sorted(waitTimes.items(), key=lambda x: x[1])
    return sortedWaitTimes[0][0] * sortedWaitTimes[0][1]

def getEarliestBusTime2(input):
    busTimes = readInput2(input)
    congruences = [ 
        { MODULO: time, REMAINDER: (time - busTimes.index(time)) % time } 
        for time in busTimes 
        if time != 'x' 
    ]
    return applyChineseRemainderTheorem(congruences)

def applyChineseRemainderTheorem(congruences):
    N = reduce(lambda x, y: x * y[MODULO], congruences, 1)
    return sum(calculateAYZ(congruence[MODULO], congruence[REMAINDER], N) for congruence in congruences) % N

def calculateAYZ(modulo, remainder, N):
    a = remainder
    y = int(N / modulo)
    z = getModuloInverse(y, modulo)
    return a * y * z

def getModuloInverse(value, modulo):
    valueInModuloBase = value % modulo
    inverse = 1
    while (inverse * value) % modulo != 1:
        inverse += 1
    return inverse

def readInput1(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    lines = inputFile.read().splitlines()
    return { 
        "arrivalTime": int(lines[0]),
        "busTimes": [int(time) for time in lines[1].split(",") if time != "x"] 
    } 

def readInput2(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    lines = inputFile.read().splitlines()
    return [int(time) if time.isdigit() else time for time in lines[1].split(",")]

if __name__ == "__main__":
        main()
