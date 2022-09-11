def maxSubArray(nums: list[int]) -> int:
    maxSumm = nums[0]
    for i in range(1, len(nums)+1):
        for j in range(i):
            tempSumm = 0
            for k in range(j,i):
                tempSumm += nums[k]
            if tempSumm > maxSumm:
                maxSumm = tempSumm
                
    return maxSumm

print(maxSubArray([-1,4,-1,3,-8,-3,4,-6,7]))