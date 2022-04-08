def reverseStr(s: str, k: int) -> str:
    t = []
    for i in range(0, len(s), k):
        t.append(s[i:i + k])

    for i in range(0, len(t), 2):
        t[i] = t[i][::-1]

    return ''.join(t)

print(reverseStr("abcd", 3))