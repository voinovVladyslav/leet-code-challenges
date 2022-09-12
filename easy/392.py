def isSubsequence(s, t):
    if len(s) == 0:
        return True

    j = 0
    for i in range(len(t)):
        if s[j] == t[i]:
            if j >= len(s) - 1:
                return True
            j += 1
        print(f'j: {j}, i: {i}')
    return False

s = 'b'
t = 'abc'
print(isSubsequence(s, t))
