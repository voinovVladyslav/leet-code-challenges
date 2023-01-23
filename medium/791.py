class Solution:
    def customSortString(self, order: str, s: str) -> str:
        letters = set(s)
        w = {i: s.count(i) for i in letters}
        res = ''
        for i in order:
            n = w.pop(i, None)
            if n is None:
                continue
            res += i * n

        for k, v in w.items():
            res += k * v
        return res
