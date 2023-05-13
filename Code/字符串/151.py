class Solution:
    #1.去除多余的空格
    def trim_spaces(self, s):  
        left, right = 0, len(s) - 1
        while s[left] == " ":#去除开头的空格
            left += 1
        while s[right] == " ":#去除结尾的空格
            right -= 1
        tmp = []
        while left <= right:
            if s[left] != " ":
                tmp.append(s[left])
            elif s[left - 1] != " ":#当前位置是空格，但是相邻的上一个位置不是空格，则该空格是合理的
                tmp.append(s[left])
            left += 1
        return tmp
    
    #2.翻转字符数组
    def reverse_string(self, nums, left, right):# 对列表中nums中left:right的切片做反转，其他元素不变
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -=1
        return None
    
    #3.翻转每个单词       
    def reverse_each_word(self, nums):
        start, end = 0, 0
        n = len(nums)
        while start < n:
            while end < n and nums[end] != " ":
                end += 1
            self.reverse_string(nums, start, end - 1)# 类内函数调用
            start = end + 1
            end += 1
        return None
            
    #4.翻转字符串里的单词
    def reverseWords(self, s: str) -> str:
        l = self.trim_spaces(s)
        self.reverse_string(l, 0, len(l) - 1)# 列表是随时变的，在其他函数中对其更改则其在全局都是变的
        self.reverse_each_word(l)
        return "".join(l)
        



s = "  hello world  "
solution = Solution()
res = solution.reverseWords(s)
print(res)