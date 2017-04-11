import bisect

def isTidy(tempnum):
    prevDigit=1

    for digit in list(str(tempnum)):
        if int(digit) < prevDigit:
            return False
        prevDigit = int(digit)
    return True


def appendIfNotZero(list, value):
    if value > 0:
        bisect.insort(list, value)
        # list.append(value)


def solveForT(n, k):
    # if n/k < 1.5:
    #     return(1,0)
    # if n/k % 1 < 0.00001:
    #     return (n/(k+1), (n/(k+1))-1)
    # elif n/k < 4.1:
    #     return (1,1)
    spaces = [n]
    peopleCounter = k
    while peopleCounter > 0:
        peopleCounter -= 1
        spaceToBeOccupied = spaces.pop(-1)
        appendIfNotZero(spaces, spaceToBeOccupied//2)
        appendIfNotZero(spaces, (spaceToBeOccupied//2) - ((spaceToBeOccupied+1) % 2))

    farest = spaceToBeOccupied//2
    closest = max((spaceToBeOccupied//2) - (((spaceToBeOccupied)+1)%2), -999)
    return (farest, closest)


def calcnOfLifts(number):
    nOfLifts = 0
    while number%2 == 1:
        nOfLifts += 1
        number = number//2
    return nOfLifts

def recursiveSolve(n, k, alreadyLifted):
    if n%2 == 0:
        alreadyLifted=False
    spaceLeft = n//2
    spaceRight = n//2 - (((n)+1)%2)

    if len(k) <= 0:
        return (spaceLeft, spaceRight)
        # if k[0] == '1':
        #     return spaceLeft
        # else:
        #     return spaceRight

    if len(k) > 1 and spaceLeft == spaceRight and not alreadyLifted:
        lifts = calcnOfLifts(spaceLeft)
        spaceLeft = spaceLeft + 2**lifts
        spaceRight = spaceRight - 2**lifts
        alreadyLifted=True

    if k[0] == '1':
        return recursiveSolve(spaceRight, k[1:], alreadyLifted)
    else:
        return recursiveSolve(spaceLeft, k[1:], alreadyLifted)

def fasterSolveForT(n, k):
    k = bin(k)[3:]
    solution = recursiveSolve(n, k, False)
    return solution

def takeInputAndSolveEach():
    outputFile = open('q3_out.py', 'w')
    f = open('q3_in.py', 'r')
    nOfCases = int(f.readline())
    # nOfCases = 100000
    caseCounter = 0
    lastSolution = [-1,-1]
    while caseCounter < nOfCases:
        caseCounter += 1
        inp = f.readline().split()
        n = int(inp[0])
        k = int(inp[1])

        caseSolution = solveForT(n,k) # works but slow
        # caseSolution = fasterSolveForT(n,k) # doesn't work but fast

        printCaseSolution(caseSolution, caseCounter, outputFile)
        if caseSolution != lastSolution:
            lastSolution = caseSolution


def printCaseSolution(solution, caseNumber, outputFile):
    solutionForCase = "Case #" + str(caseNumber) + ": " + str(solution) + " " + str("")
    outputFile.write(solutionForCase + "\n")

if __name__ == "__main__":
    takeInputAndSolveEach()
