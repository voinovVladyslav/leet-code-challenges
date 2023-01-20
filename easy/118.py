class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        for i in range(1, numRows + 1):
            temp = [1 for _ in range(i)]
            for j in range(1, len(temp) - 1):
                temp[j] = res[-1][j - 1] + res[-1][j]
            res.append(temp)
        return res


s = Solution()
triangle = s.generate(10)

for row in triangle:
    print(row)
