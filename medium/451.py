class Solution:
    def frequencySort(self, s: str) -> str:
        symbols = set(s)
        hashmap = {}
        for symbol in symbols:
            n = s.count(symbol)
            hashmap[symbol] = n
        res = list(hashmap.items())
        res.sort(key=lambda x: x[1], reverse=True)
        ans = ''
        for symbol, n in res:
            ans += symbol*n
        return ans


a = "Aabb"
s = Solution()
print(s.frequencySort(a))
