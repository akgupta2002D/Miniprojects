def runningSum(Array):
    for i in range(0, len(Array)-1):
        Array[i+1] = Array[i] + Array[i+1]
    print(Array)
    return Array


runningSum([1, 1, 1, 1])
