import collections
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        Ls, Lp = len(s), len(p)
        if Ls < Lp: #不存在
            return []
        need = collections.defaultdict(int) #当前窗口下每个字母还需要几个
        needCnt = 0 #当前窗口下一共还需要多少字母
        for c in p:
            need[c] += 1
            needCnt += 1
        res = []
        i = 0
        j = Lp
        for k in range(i, j):
            # 相当于添加最右侧元素进窗口
            if need[s[k]] > 0: #不在p里的字母，其need[s[k]]一定小于0，不会影响needCnt。如果need[s[k]]<=0表示当前窗口下s[k]已经过量了，也无需修改needCnt
                needCnt -= 1
            need[s[k]] -= 1
        if not needCnt:
            res.append(i)
        
        while i < Ls - Lp:
            # 移除最左侧元素出窗口
            need[s[i]] += 1
            if need[s[i]] > 0:
                needCnt += 1
            # 添加最右侧元素进窗口
            if need[s[j]] > 0:
                needCnt -= 1
            need[s[j]] -= 1
            
            i += 1
            j += 1
            if not needCnt:
                res.append(i)
            
        return res

s = "aaaaaaaaaa"
p = "aaaaaaaaaaaaa"
solution = Solution()
res = solution.findAnagrams(s, p)
print(res)