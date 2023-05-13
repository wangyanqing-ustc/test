from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                p, q = j + 1, n - 1
                while p < q:
                    total = nums[i] + nums[j] +nums[p] + nums[q]
                    if total > target:
                        q -= 1
                    elif total < target:
                        p += 1
                    else:
                        res.append([nums[i], nums[j], nums[p], nums[q]])
                        while p < q and nums[p] == nums[p + 1]:
                            p += 1
                        while p < q and nums[q] == nums[q - 1]:
                            q -= 1
                        p += 1
                        q -= 1
        return res

nums = [2,2,2,2,2]
target = 8
solution = Solution()
res = solution.fourSum(nums, target)
print(res)