def revomeElement(nums: list[int], val: int) -> int:
    if not val in nums:
        return len(nums)
    
    for i in range(nums.count(val)):
        nums.remove(val)
        nums.append("_")
        
    for i in range(len(nums)):
        if nums[i] == "_":
            return i

x = [1,2,3,1,3,6,4]

print(revomeElement(x, 2))
print(x)
