class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = {}
        i = 0
        res = 0
        for j in range(len(fruits)):
            if fruits[j] not in dic:
                dic[fruits[j]] = 1
            else:
                dic[fruits[j]] += 1
            while len(dic) > 2:
                dic[fruits[i]] -= 1
                if dic[fruits[i]] == 0:
                    del dic[fruits[i]]
                i += 1
            res = max(res, j-i+1)
        return res