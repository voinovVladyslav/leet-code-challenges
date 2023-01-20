class Solution:
    def sortColors(self, nums: list[int]) -> None:
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]


n = [2, 0, 2, 1, 1, 0]
s = Solution()
s.sortColors(n)
print(n)
