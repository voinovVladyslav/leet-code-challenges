def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    for i in nums2:
        nums1.append(i)
        nums1.remove(0)
    nums1.sort()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)