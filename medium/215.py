class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort()
        return nums[-k]


n = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

s = Solution()
print(s.findKthLargest(n, k))
