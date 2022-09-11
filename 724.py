def pivotIndes(nums):
    right = sum(nums[1:])
    left = 0
    for i in range(len(nums) - 1):
        print(i, left, right)
        if left == right:
            return i
        left += nums[i]
        right -= nums[i + 1]
    if left == right:
        return len(nums) - 1
    return -1

print(pivotIndes([-1,-1,0,1,1,0]))
