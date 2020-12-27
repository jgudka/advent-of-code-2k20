import re
from enum import Enum
from functools import reduce

RULES = "rules"
MY_TICKET = "myTicket"
NEARBY_TICKETS = "nearbyTickets"
LOWER_RANGE = "lowerRange"
UPPER_RANGE = "upperRange"
FIELD_VALUES = "fieldValues"
VALID = "valid"

class VALIDITY(Enum):
    NOT_CHECKED = 0
    VALID = 1
    INVALID = 2

def main():
    example = readInput("example")
    realInput = readInput("input")
    print(getErrorRate(example))
    print(getErrorRate(realInput))

    print(getTicketProduct(realInput))

def getErrorRate(notes):
    ranges = reduce(lambda x, y: x + [ y[LOWER_RANGE], y[UPPER_RANGE] ], notes[RULES].values(), [])
    fieldValues = reduce(lambda x, y: x + y[FIELD_VALUES], notes[NEARBY_TICKETS], [])
    for ticket in notes[NEARBY_TICKETS]:
        ticket[VALID] = VALIDITY.VALID if all([any([ bounds[0] <= value <= bounds[1] for bounds in ranges ]) for value in ticket[FIELD_VALUES]]) else VALIDITY.INVALID
    return sum(value for value in fieldValues if not any([ bounds[0] <= value <= bounds[1] for bounds in ranges ]))

def getTicketProduct(notes):
    validNearbyTickets = [ticket[FIELD_VALUES] for ticket in notes[NEARBY_TICKETS] if ticket[VALID] == VALIDITY.VALID]
    fieldToOptionsDict = { 
        field: set((i for i in range(len(notes[RULES])) if allFieldsInRange(rule, i, validNearbyTickets))) 
        for field, rule in notes[RULES].items() 
    }
    fieldToKnownPositionDict = dict()
    while len(fieldToKnownPositionDict) != len(notes[RULES]):
        for field in notes[RULES]:
            if len(fieldToOptionsDict[field]) == 1:
                knownPosition = list(fieldToOptionsDict[field])[0]
                fieldToKnownPositionDict[field] = knownPosition
                for field in notes[RULES]:
                    fieldToOptionsDict[field].discard(knownPosition)
                break

    positionsToMultiply = [ position for field, position in fieldToKnownPositionDict.items() if "departure" in field ]
    return reduce(lambda x, y: x * notes[MY_TICKET][y], positionsToMultiply, 1)

def allFieldsInRange(rule, fieldIndex, validTickets):
    return all([
        rule[LOWER_RANGE][0] <= ticket[fieldIndex] <= rule[LOWER_RANGE][1] 
        or rule[UPPER_RANGE][0] <= ticket[fieldIndex] <= rule[UPPER_RANGE][1] 
        for ticket in validTickets
    ])

def readInput(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    unparsedSections = inputFile.read().split("\n\n")

    rules = dict()
    for rule in unparsedSections[0].splitlines():
        ruleFields = re.split(": | or ", rule)
        lowerRange = [int(x) for x in ruleFields[1].split("-")]
        upperRange = [int(x) for x in ruleFields[2].split("-")]
        rules[ruleFields[0]] = { LOWER_RANGE: lowerRange, UPPER_RANGE: upperRange}
    
    myTicket = [int(x) for x in unparsedSections[1].splitlines()[1].split(",")]

    nearbyTickets = [
        { FIELD_VALUES: [int(x) for x in ticket.split(",")], VALID: VALIDITY.NOT_CHECKED } 
        for ticket in unparsedSections[2].splitlines()[1:]
    ]

    return { RULES: rules, MY_TICKET: myTicket, NEARBY_TICKETS: nearbyTickets }

if __name__ == "__main__":
        main()
