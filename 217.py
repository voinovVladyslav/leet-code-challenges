def withDublicate(nums: list[int]) -> bool:
    return len(set(nums)) < len(nums)
        
print(withDublicate([1,1,1,3,3,4,3,2,4,2]))