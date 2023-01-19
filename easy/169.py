class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        elements = set(nums)
        max_occurences = 0
        res = 0
        for element in elements:
            count = nums.count(element)
            if count > max_occurences:
                max_occurences = count
                res = element
        return res


nums = [2, 2, 1, 1, 1, 2, 2]
s = Solution()
print(s.majorityElement(nums))
