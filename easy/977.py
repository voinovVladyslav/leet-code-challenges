def sortedSquares(nums):
    squared = [x*x for x in nums]
    squared.sort()
    return squared

print(sortedSquares([-4,-1,0,3,10]))
