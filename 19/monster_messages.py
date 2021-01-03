import re
from enum import Enum
from functools import reduce
from numbers import Number

RULES = "rules"
MESSAGES = "messages"

def main():
    example = readInput("example")
    realInput = readInput("input")
    # print(countValidMessages(example))
    print(countValidMessages(realInput))

def countValidMessages(input):
    rules = input[RULES]
    messages = input[MESSAGES]
    possibleValidMessagesForRules = [ getSequencesForRule(ruleNumber, rules) for ruleNumber in rules[0][0]]
    possibleMessages = getCombinations(possibleValidMessagesForRules[0], possibleValidMessagesForRules[1])
    return sum(1 for message in messages if message in possibleMessages)

def getSequencesForRule(ruleNumber, rules):
    rule = rules[ruleNumber]
    if rule in ["a", "b"]:
        return [rule]
    elif len(rule) == 1:
        if len(rule[0]) == 1:
            return getSequencesForRule(rule[0][0], rules)
        else:
            return getCombinations(getSequencesForRule(rule[0][0], rules), getSequencesForRule(rule[0][1], rules))
    else:
        if len(rule[0]) == 1:
            return getSequencesForRule(rule[0][0], rules) + getSequencesForRule(rule[1][0], rules)
        else:
            return (getCombinations(getSequencesForRule(rule[0][0], rules), getSequencesForRule(rule[0][1], rules)) + 
                getCombinations(getSequencesForRule(rule[1][0], rules), getSequencesForRule(rule[1][1], rules)))

def getCombinations(firstStringOptions, secondStringOptions):
    combinations = []
    for firstStringOption in firstStringOptions:
        for secondStringOption in secondStringOptions:
            combinations.append(firstStringOption + secondStringOption)
    return combinations

def getCombinations3(firstStringOptions, secondStringOptions, thirdStringOptions):
    combinations = []
    for firstStringOption in firstStringOptions:
        for secondStringOption in secondStringOptions:
            for thirdStringOption in thirdStringOptions:
                combinations.append(firstStringOption + secondStringOption + thirdStringOption)
    return combinations

def readInput(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    [rules, messages] = inputFile.read().split("\n\n")
    rulesDict = dict()
    for rule in rules.splitlines():
        [ruleNumber, ruleDefinition] = rule.split(": ")
        rulesDict[int(ruleNumber)] = ruleDefinition[1] if ruleDefinition in ['"a"', '"b"'] else [ 
            [ int(ruleNumber) for ruleNumber in sequence.split(" ") ] 
            for sequence in ruleDefinition.split(" | ")
        ]
    return { RULES : rulesDict, MESSAGES: messages.splitlines() }

if __name__ == "__main__":
        main()
