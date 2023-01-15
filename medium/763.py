class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        L = len(s)
        # hashmap of last position of a letter
        last = {s[i]: i for i in range(len(s))}

        i, res = 0, []
        while i < L:
            # approx end = last occurence of s[i]
            # j starts from next index
            end, j = last[s[i]], i + 1
            while j < end:
                # if last occurence of the end is further, move end
                if last[s[j]] > end:
                    end = last[s[j]]
                j += 1
            # reach till the end of slice, calculate len of slice
            res.append(end - i + 1)
            # beginning of next slice
            i = end + 1
        return res


d = 'aebbedaddc'
b = 'eaaaabaaec'
s = 'ababcbacadefegdehijhklij'

res = Solution().partitionLabels(d)

print(res)
