class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        t = list(s)
        n = len(s)
        i, j = 0, k - 1
        while i < n:
            t[i:j+1] = t[i:j+1][::-1]
            i += 2*k
            j += 2*k
        return "".join(t)
    
s = "abcdefgh"
k = 3
solution = Solution()
res = solution.reverseStr(s, k)
print(res)