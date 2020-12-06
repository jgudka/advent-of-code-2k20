from typing import List, Set


def main():
    print(questionsAnswered1("example"))
    print(questionsAnswered1("input"))

    print(questionsAnswered2("example"))
    print(questionsAnswered2("input"))

def questionsAnswered1(inputFileName):
    answersByGroup = readInput(inputFileName)
    answerSetsByGroup = list(map(getAnswerSetForGroup, answersByGroup))
    return sum(len(answerSet) for answerSet in answerSetsByGroup)

def questionsAnswered2(inputFileName):
    answersByGroup = readInput(inputFileName)
    answerSetsByGroup = list(map(getAnswerSetForGroup, answersByGroup))
    return sum(map(getCountQuestionsAnsweredByEveryone, answersByGroup, answerSetsByGroup))

def getCountQuestionsAnsweredByEveryone(rawAnswers, answerSet):
    groupSize = len(rawAnswers)
    count = 0
    for answer in answerSet:
        if ''.join(rawAnswers).count(answer) == groupSize:
            count +=1

    return count

def getAnswerSetForGroup(group: List[str]) -> Set[str]:
    answerSet = set()
    for member in group:
        answerSet.update(list(member))
    return answerSet

def readInput(inputFileName):
    inputFile = open(f"{inputFileName}.txt", "r")
    unparsedGroups = inputFile.read().split("\n\n")
    return [group.split() for group in unparsedGroups]

if __name__ == "__main__":
        main()
