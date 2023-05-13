class Solution:
    def replaceSpace(self, s: str) -> str:
        while " " in s:
            i = s.index(" ")
            s = s[:i] + "%20" +s[i+1:]
        return s
    
solution = Solution()
s = "We are happy."
res = solution.replaceSpace(s)
print(res)