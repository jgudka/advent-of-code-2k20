import re
from typing import Dict, List, Set


def main():
    print(bagColour1("example"))
    print(bagColour1("input"))

    print(bagColour2("example"))
    print(bagColour2("input"))

def bagColour1(inputFileName):
    rulesDict = readInput(inputFileName)
    return sum(1 for colour, rule in rulesDict.items() if bagCanContain(rulesDict, rule, 'shiny gold'))

def bagColour2(inputFileName):
    rulesDict = readInput(inputFileName)
    return countBagsInside(rulesDict, "shiny gold")

def bagCanContain(rulesDict, bagRule, bagToContain):
    if (bagToContain in bagRule):
        return True
    elif (not bagRule):
        return False
    else:
        return any(bagCanContain(rulesDict, rulesDict[bag], bagToContain) for bag in bagRule)

def countBagsInside(rulesDict, bag):
    rules = rulesDict[bag]
    if not (rules):
        return 0
    else:
        return sum(number + number * countBagsInside(rulesDict, colour) for colour, number in rules.items())

def readInput(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    unparsedLines = inputFile.read().splitlines()
    bagDict = {}
    for line in unparsedLines:
        components = re.split(' bags contain | bags?[,.] ?', line)
        components.pop()
        bagDict[components.pop(0)] = dict((colour, int(number)) 
                for number, colour 
                in (component.split(" ", 1) for component in components) 
                if number.isdigit())
    return bagDict


if __name__ == "__main__":
        main()
