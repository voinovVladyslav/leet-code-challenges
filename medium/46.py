from itertools import permutations


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return permutations(nums)


s = Solution().permute

test = [1, 2, 3]
print(s(test))
print(list(permutations(test)))
