def isPowerOfTwo(n: int) -> bool:
    if n == 1:
        return True
    t = 1
    while(t <= n):
        if t*2 == n:
            return True
        t *= 2
    return False

print(isPowerOfTwo(256))