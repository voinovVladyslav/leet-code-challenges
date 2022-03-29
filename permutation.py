def buildArray(n: list[int]) -> list[int]:
    m = []
    for i in range(len(n)):
        m.append(n[n[i]])
    return m

print(buildArray([0,2,1,5,3,4]))