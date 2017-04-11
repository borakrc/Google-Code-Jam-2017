
def takeInput():
    nOfCases = int(input())
    cases = []
    for counter in range(nOfCases):
        pancakes, flipperSize = input().split()
        cases.append([list(pancakes), int(flipperSize)])
    return cases


def flipPancakes(pancakeOrder, flipperSize, flipStartPosition):
    for c in range(flipperSize):
        if pancakeOrder[c+flipStartPosition] == '-':
            pancakeOrder[c+flipStartPosition] = "+"
        else:
            pancakeOrder[c+flipStartPosition] = "-"


def checkRemainingPancakes(pancakeOrder, counter):
    for char in pancakeOrder[counter-1:]:
        if char == '-':
            return False
    return True


def calculateAndPrint(pancakeOrder, flipperSize, caseNumber):
    counter = 0
    numberOfFlips = 0
    while counter < len(pancakeOrder)-flipperSize+1:
        if pancakeOrder[counter] == "-":
            flipPancakes(pancakeOrder, flipperSize, counter)
            numberOfFlips += 1
        counter += 1
    isSolution = checkRemainingPancakes(pancakeOrder, counter)
    if isSolution:
        print ("Case #" + str(caseNumber) + ": " + str(numberOfFlips))
    else:
        print ("Case #" + str(caseNumber) + ": IMPOSSIBLE")
    # return numberOfFlips


if __name__ == "__main__":
    inputData = takeInput()

    caseCounter = 1
    for eachinput in inputData:
        calculateAndPrint(pancakeOrder = eachinput[0], flipperSize = eachinput[1], caseNumber= caseCounter)
        caseCounter += 1
