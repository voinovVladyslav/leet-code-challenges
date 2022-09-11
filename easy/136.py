def singleNumber(n: list[int]) -> int:
    n.sort()
    if len(n) > 1:
        if n[0] != n[1]:
            return n[0]

    for i in range(1, len(n)-1):
        if n[i] != n[i + 1] and n[i] != n[i - 1]:
            return n[i]
    return n[-1]

print(singleNumber([1]))
