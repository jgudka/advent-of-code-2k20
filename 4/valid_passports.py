import re


def main():
    print(validPassports1("example"))
    print(validPassports1("input"))

    print(validPassports2("example"))
    print(validPassports2("input"))

def validPassports1(inputFileName):
    passports = readInput(inputFileName)
    validCount = 0
    requiredFields = [ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for passport in passports:
        if all([field in passport for field in requiredFields]):
            validCount += 1
    
    return validCount

def validPassports2(inputFileName):
    passports = readInput(inputFileName)
    validCount = 0
    
    for passport in passports:
        if passportHasRequiredFields(passport):
            if all([
                isValidBirthYear(passport),
                isValidIssueYear(passport),
                isValidExpirationYear(passport),
                isValidHeight(passport),
                isValidHairColour(passport),
                isValidEyeColour(passport),
                isValidPassportId(passport),
            ]):
                validCount += 1
    
    return validCount

def isValidBirthYear(passport):
    birthYear = int(passport["byr"])
    return birthYear >= 1920 and birthYear <= 2002

def isValidIssueYear(passport):
    issueYear = int(passport["iyr"])
    return issueYear >= 2010 and issueYear <= 2020

def isValidExpirationYear(passport):
    expirationYear = int(passport["eyr"])
    return expirationYear >= 2020 and expirationYear <= 2030

def isValidHeight(passport):
    height = passport["hgt"]
    units = height[-2:]
    valueString = height[:-2]
    if not valueString.isdigit():
        return False
    
    value = int(valueString)
    return (units == "cm" and value >= 150 and value <= 193) or (units == "in" and value >= 59 and value <= 76)

def isValidHairColour(passport):
    hairColour = passport["hcl"]
    return re.search("#{1}[0-9a-f]{6}", hairColour) is not None

def isValidEyeColour(passport):
    return passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def isValidPassportId(passport):
    id = list(passport["pid"])
    return len(id) == 9 and all([digit.isdigit() for digit in id])

def passportHasRequiredFields(passport):
    requiredFields = [ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all([field in passport for field in requiredFields])

def readInput(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    unparsedPassports = inputFile.read().split("\n\n")
    moreParsedPassports = [re.split(' |\n', line) for line in unparsedPassports]
    passports = []
    for line in moreParsedPassports:
        passport = {}
        for entry in line:
            keyValue = entry.split(":")
            passport[keyValue[0]] = keyValue[1]
        passports.append(passport)

    return passports

if __name__ == "__main__":
        main()
