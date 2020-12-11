from seatingArrangement import SeatingArrangment
from seatingArrangement2 import SeatingArrangment2


def main():
    example = readInput("example")
    realInput = readInput("input")

    exampleSeatingArrangement = SeatingArrangment(example)
    exampleSeatingArrangement.simulate()
    print(exampleSeatingArrangement.countOccupiedSeats())

    seatingArrangement = SeatingArrangment(realInput)
    seatingArrangement.simulate()
    print(seatingArrangement.countOccupiedSeats())

    exampleSeatingArrangement2 = SeatingArrangment2(example)
    exampleSeatingArrangement2.simulate()
    print(exampleSeatingArrangement2.countOccupiedSeats())

    seatingArrangement2 = SeatingArrangment2(realInput)
    seatingArrangement2.simulate()
    print(seatingArrangement2.countOccupiedSeats())

def readInput(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    return [list(line) for line in inputFile.read().splitlines()]

if __name__ == "__main__":
        main()
