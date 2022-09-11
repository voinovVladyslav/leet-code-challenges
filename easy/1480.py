def runningSum(nums):
    n = []
    for i in range(len(nums)):
        n.append(sum(nums[:i+1]))
    return n


print(runningSum([3,1,2,10,1]))
