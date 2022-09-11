def isBadVersion(n):
    return n >= 1

def firstBadVersion(n: int):
    left = 1
    right = n
    while left <= right:
        mid = (left + right) // 2
        if isBadVersion(mid) and isBadVersion(mid - 1) is False:
            return mid
        if isBadVersion(mid):
            right = mid - 1
        else:
            left = mid + 1


print(firstBadVersion(1))
