def main():
    print(repairReport1("example"))
    print(repairReport1("input"))

    print(repairReport2("example"))
    print(repairReport2("input"))

def repairReport1(inputFileName):
    expenses = readInput(inputFileName)

    for i in range(len(expenses)):
        for j in range (i + 1, len(expenses)):
            sum = expenses[i] + expenses[j]
            if sum == 2020:
                return expenses[i] * expenses[j]

def repairReport2(inputFileName):
    expenses = readInput(inputFileName)

    for i in range(len(expenses)):
        for j in range (i + 1, len(expenses)):
            for k in range (j + 1, len(expenses)):
                sum = expenses[i] + expenses[j] + expenses[k]
                if sum == 2020:
                    return expenses[i] * expenses[j] * expenses[k]

def readInput(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    return [int(numeric_string) for numeric_string in inputFile.read().splitlines()]

if __name__ == "__main__":
        main()
