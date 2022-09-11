def search(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    
    while(low <= high):
        mid = low + (high - low)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
    
nums = [1,2,3,4,5,6,7,8,9]

print(search(nums, 8))