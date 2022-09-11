def topKFrequent(nums: list[int], k: int) -> list[int]:
    if k == len(set(nums)):
        return list(set(nums))

    t = list(set(nums))
    frequency = []
    for i in t:
        frequency.append(nums.count(i))

    res = []
    for i in range(k):
        res.append(t[frequency.index(max(frequency))])
        t.pop(frequency.index(max(frequency)))
        frequency.pop(frequency.index(max(frequency)))

    return res

print(topKFrequent([1,1,1,2,2,3,3,4], 3))