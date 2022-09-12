def rotate(nums, k) -> None:
    for _ in range(k):
        n = nums.pop()
        nums.insert(0, n)

x = [1,2,3,4,5,6,7]
rotate(x, 3)
print(x)
