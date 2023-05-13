#滑动窗口，自己写的
#符合条件的s的字串的首尾必然是在t内，所以只需要对s内被t包含的元素滑动窗口
# dic始终记录着当前滑动窗口下，我们还需要的元素数量
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         dic = {}
#         index  = []
#         for c in t:
#             if c in dic:
#                 dic[c] += 1
#             else:
#                 dic[c] = 1
#         for i in range(len(s)):
#             if s[i] in dic:
#                 index.append(i)
#         def check(dic):#判断当前窗口下是否符合要求，如果每次判断滑动窗口是否包含了T的所有元素，都去遍历need看是否所有元素数量都小于等于0，这个会耗费O(k)的时间复杂度，k代表字典长度
#             t1 = list(dic.values())
#             for ti in t1:
#                 if ti > 0:
#                     return False
#             return True

#         L = float("inf")
#         res = [-1,-1]
#         i = 0
#         for j in range(len(index)):
#             dic[s[index[j]]] -= 1
#             tag = 0
#             while check(dic):
#                 if index[j]-index[i]+1 < L:
#                     L = index[j]-index[i]+1
#                     res = [i, j]
#                 tag = 1
#                 dic[s[index[i]]] += 1
#                 i += 1
#             if tag:#如果初始窗口符合条件，则需要把最后放到外面的那个元素补回来
#                 i -= 1
#                 dic[s[index[i]]] -= 1
                
#         return s[index[res[0]]:index[res[1]]+1] if res != [-1,-1] else ""

import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=collections.defaultdict(int)
        for c in t:
            need[c]+=1
        needCnt=len(t)
        i=0
        res=(0,float('inf'))
        for j,c in enumerate(s):
            if need[c]>0:#当c还被需要的时候才让needCnt减1，如果c的数量已经达到要求，即使c在t中也不更改needCnt。并且只有在t内的c才可能大于0
                needCnt-=1
            need[c]-=1
            if needCnt==0:       #步骤一：滑动窗口包含了所有T元素
                while True:      #步骤二：增加i，排除多余元素
                    c=s[i] 
                    if need[c]==0:
                        break
                    need[c]+=1
                    i+=1
                if j-i<res[1]-res[0]:   #记录结果
                    res=(i,j)
                need[s[i]]+=1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt+=1
                i+=1
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]    #如果res始终没被更新过，代表无满足条件的结果
    
solution = Solution()
s = "DEFAABABBCCDEF"
t = "ABC"
res = solution.minWindow(s, t)
print(res)