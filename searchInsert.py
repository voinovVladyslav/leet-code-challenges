def searchInsert(nums : list[int], target : int) -> int:
    for i in range(len(nums)):
        if target <= nums[i]:
            return i
    return len(nums)

nums = [1,2,3,5,6]

print(searchInsert(nums, 8))