def findDuplicate(nums: list[int]) -> int:
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i-1] == nums[i]:
            return nums[i]

print(findDuplicate([1,2,3,4,4,5,56,6,7]))