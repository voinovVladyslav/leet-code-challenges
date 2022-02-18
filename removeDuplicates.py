def removeDuplicates(nums: list[int]) -> int:
    temp = list(set(nums))
    for i in range(len(temp)):
        for j in range(1 ,nums.count(nums[i])):
            nums.remove(nums[i])
            nums.append("_")    
    if "_" in nums:
        return len(set(nums))-1
    else:
        return len(set(nums))

lst = [1,1,1,2,3]
print(removeDuplicates(lst))
print(lst)