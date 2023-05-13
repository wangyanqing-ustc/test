from collections import Counter
s = "123"
nums = [1,2,3]
nums2 = [2,3,4,2]
dic = {"A":1,"B":2,"C":3}
cnt = Counter(dic)

res = [nums[i]**2 for i in range(len(nums)-1, -1, -1) ]
print(res)
