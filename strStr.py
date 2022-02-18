def strStr(haystack: str, needle: str) -> int:
    if needle not in haystack:
        return -1
    if needle == haystack:
        return 0
    for i in range(len(haystack)):
        if needle == haystack[i:i+len(needle)]:
            return i


print(strStr("qwerty","q2e"))