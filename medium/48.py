class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        size = len(matrix)
        for i in range(size):
            for j in range(i, size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(size):
            matrix[i].reverse()


m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in m:
    print(i)
print('=' * 9)

s = Solution()
s.rotate(m)

for i in m:
    print(i)
