def maxProfit(prices: list[int]) -> int:
    max = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[j] - prices[i] > max:
                max = prices[j] - prices[i]
    return max

print(maxProfit([7,6,4,3,1]))