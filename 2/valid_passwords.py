import re


def main():
    print(validPasswords1("example"))
    print(validPasswords1("input"))

    print(validPasswords2("example"))
    print(validPasswords2("input"))

def validPasswords1(inputFileName):
    passwordsWithPolicies = readInput(inputFileName)
    validCount = 0
    for i in range(len(passwordsWithPolicies)):
        passwordWithPolicy = passwordsWithPolicies[i]
        letterOccurrences = passwordWithPolicy["password"].count(passwordWithPolicy["letter"])
        if (letterOccurrences >= passwordWithPolicy["lower"] and letterOccurrences <= passwordWithPolicy["upper"]):
            validCount += 1
            passwordWithPolicy["valid"] = True
        else:
           passwordWithPolicy["valid"] = False 
    
    return validCount

def validPasswords2(inputFileName):
    passwordsWithPolicies = readInput(inputFileName)
    validCount = 0
    for i in range(len(passwordsWithPolicies)):
        passwordWithPolicy = passwordsWithPolicies[i]
        password = passwordWithPolicy["password"]
        letter = passwordWithPolicy["letter"]
        lowerIndex = passwordWithPolicy["lower"]
        upperIndex = passwordWithPolicy["upper"]
        lowerIndexMatch = password[lowerIndex - 1] == letter
        upperIndexMatch = password[upperIndex - 1] == letter
        if (lowerIndexMatch or upperIndexMatch) and not (lowerIndexMatch and upperIndexMatch):
            validCount += 1
            passwordWithPolicy["valid"] = True
        else:
           passwordWithPolicy["valid"] = False 
    
    print(passwordsWithPolicies)
    return validCount

def readInput(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    unparsedLines = inputFile.read().splitlines()
    lines = [re.split('-| |: ', line) for line in unparsedLines]
    return [{"lower": int(line[0]), "upper": int(line[1]), "letter": line[2], "password": line[3]} for line in lines]

if __name__ == "__main__":
        main()
