from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return right + 1#考虑了三种target不在nums中的情况
        
solution = Solution()
nums = [1,3,5,6]
target = 7
res = solution.searchInsert(nums, target)
print(res)