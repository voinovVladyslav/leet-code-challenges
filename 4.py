def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        nums3 = []
        nums3.extend(nums1)
        nums3.extend(nums2)
        nums3.sort()
        
        if len(nums3) // 2 < len(nums3) / 2:
            return nums3[len(nums3) // 2] 
        else:
            return (nums3[len(nums3) // 2 - 1] + nums3[len(nums3) // 2]) / 2

print(findMedianSortedArrays([1,3], [2]))