def lastStoneWeight(stones: list[int]) -> int:
    while len(stones) > 1:
        max1 = max(stones)
        stones.remove(max1)
        max2 = max(stones)
        stones.remove(max2)
        
        if max1 != max2:
            stones.append(max1 - max2)
        elif len(stones) == 0:
            return 0
    return stones[0]

print(lastStoneWeight([1,1]))