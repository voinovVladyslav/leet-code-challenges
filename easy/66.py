def plusOne(nums: list[int]) -> list[int]:
    nums[-1] += 1
    isNeedtoIncrementNext = False
    nums.reverse()
    for i in range(len(nums)):
        if isNeedtoIncrementNext:
            nums[i] += 1
            isNeedtoIncrementNext = False
        if nums[i] == 10:
            nums[i] = 0
            isNeedtoIncrementNext = True
    if nums[-1] == 0:
        nums.append(1)
    nums.reverse()
    return nums

print(plusOne([9,9]))
