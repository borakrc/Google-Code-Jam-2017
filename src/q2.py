def isTidy(tempnum):
    prevDigit=1

    for digit in list(str(tempnum)):
        if int(digit) < prevDigit:
            return False
        prevDigit = int(digit)
    return True

def solveForT(t):
    tempnum = t
    nOf9s = 0
    while not isTidy(tempnum) and tempnum > 0:
        nOf9s += 1
        tempnum = tempnum//10
        tempnum -= 1
    return int(str(tempnum)+("9"*nOf9s))

def takeInputAndSolveEach():
    outputFile = open('q2_o.py', 'w')
    f = open('q2_input.py', 'r')
    nOfCases = int(f.readline())
    caseCounter = 0
    while caseCounter < nOfCases:
        caseCounter += 1
        t = int(f.readline())
        caseSolution = solveForT(t)
        printCaseSolution(caseSolution, caseCounter, outputFile)


def printCaseSolution(solution, caseNumber, outputFile):
    solutionForCase = "Case #" + str(caseNumber) + ": " + str(solution)
    # print (solutionForCase)
    outputFile.write(solutionForCase + "\n")



if __name__ == "__main__":
    takeInputAndSolveEach()
