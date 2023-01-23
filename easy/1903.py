class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd = ['9', '7', '5', '3', '1']
        s = num[::-1]
        for i, char in enumerate(s):
            if char in odd:
                res = num[:len(num) - i]
                return res
        return ''


s = Solution()
print(s.largestOddNumber("3542"))
