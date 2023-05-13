class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)
        for c in s:
            dict_s[c] += 1
        for c in t:
            dict_t[c] += 1
        return dict_s == dict_t
    
class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        a_count = Counter(s)
        b_count = Counter(t)
        return a_count == b_count
    
s = "anagram"
t = "nagaram"
solution = Solution()
res = solution.isAnagram(s, t)