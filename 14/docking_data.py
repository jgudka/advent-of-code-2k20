import math
import re
from enum import Enum
from functools import reduce

INSTRUCTION_TYPE = "instructionType"
ZERO_MASK = "zeroMask"
ONE_MASK = "oneMask"
FLOATING_BIT_LOCATIONS = "floatingBitLocations"
ADDRESS = "address"
VALUE = "value"

class InstructionType(Enum):
    BITMASK = 0
    ALLOCATION = 1

def main():
    # print(getSumOfValuesInMemory1("example"))
    # print(getSumOfValuesInMemory1("input"))

    print(getSumOfValuesInMemory2("example"))
    print(getSumOfValuesInMemory2("input"))

def getSumOfValuesInMemory1(input):
    program = readInput1(input)
    memory = dict()
    zeroMask = 0
    oneMask = 0
    for line in program:
        if line[INSTRUCTION_TYPE] == InstructionType.BITMASK:
            zeroMask = line[ZERO_MASK]
            oneMask = line[ONE_MASK]
        else:
            memory[line[ADDRESS]] = line[VALUE] & zeroMask | oneMask

    return sum(memory.values())

def getSumOfValuesInMemory2(input):
    program = readInput2(input)
    memory = dict()
    oneMask = 0
    floatingBitLocations = []
    for line in program:
        if line[INSTRUCTION_TYPE] == InstructionType.BITMASK:
            oneMask = line[ONE_MASK]
            floatingBitLocations = line[FLOATING_BIT_LOCATIONS]
        else:
            baseAddress = convertToBinaryString(line[ADDRESS] | oneMask, 36)
            for i in range(2**len(floatingBitLocations)):
                address = list(baseAddress[::])
                floatingNumberBinaryString = convertToBinaryString(i, len(floatingBitLocations))
                for j in range(len(floatingNumberBinaryString)):
                    address[floatingBitLocations[j]] = floatingNumberBinaryString[j]

                memory[int("".join(address), 2)] = line[VALUE]

    return sum(memory.values())

def convertToBinaryString(number, bitLength):
    return bin(number)[2:].zfill(bitLength)

def readInput1(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    lines = inputFile.read().splitlines()
    program = []
    maskPrefix = "mask = "
    for line in lines:
        if maskPrefix in line:
            mask = line[len(maskPrefix):]
            program.append({ 
                INSTRUCTION_TYPE: InstructionType.BITMASK,
                ZERO_MASK: int(''.join(map(lambda x: '0' if x == '0' else '1', list(mask))), 2),
                ONE_MASK: int(''.join(map(lambda x: '1' if x == "1" else '0', list(mask))), 2),
            })
        else :
            parsedAllocation = re.split("mem\[|\] = ", line)
            program.append({ 
                INSTRUCTION_TYPE: InstructionType.ALLOCATION,
                ADDRESS: int(parsedAllocation[1]),
                VALUE: int(parsedAllocation[2])
            })

    return program

def readInput2(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    lines = inputFile.read().splitlines()
    program = []
    maskPrefix = "mask = "
    for line in lines:
        if maskPrefix in line:
            mask = line[len(maskPrefix):]
            program.append({ 
                INSTRUCTION_TYPE: InstructionType.BITMASK,
                ONE_MASK: int(''.join(map(lambda x: '1' if x == "1" else '0', list(mask))), 2),
                FLOATING_BIT_LOCATIONS: [i for i, x in enumerate(mask) if x == "X"]
            })
        else :
            parsedAllocation = re.split("mem\[|\] = ", line)
            program.append({ 
                INSTRUCTION_TYPE: InstructionType.ALLOCATION,
                ADDRESS: int(parsedAllocation[1]),
                VALUE: int(parsedAllocation[2])
            })

    return program

if __name__ == "__main__":
        main()
