nums = [3, 7, 23, 12]

target = 10

def twoSum(nums: list[int], target: int):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if (nums[i] + nums[j]) == target:
                    return [i, j] # indexes of this numbers

print(twoSum(nums, target))