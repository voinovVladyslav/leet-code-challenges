class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping_s = {i: s.count(i) for i in set(s)}
        mapping_t = {i: t.count(i) for i in set(t)}
        return mapping_s == mapping_t


a = "anagram"
t = "nagaran"
s = Solution()
print(s.isAnagram(a, t))
