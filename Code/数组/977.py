#题解，找到正负分界线，然后双指针，
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        negative = -1
        for i, num in enumerate(nums):
            if num < 0:
                negative = i
            else:
                break

        ans = list()
        i, j = negative, negative + 1
        while i >= 0 or j < n:
            if i < 0:
                ans.append(nums[j] * nums[j])
                j += 1
            elif j == n:
                ans.append(nums[i] * nums[i])
                i -= 1
            elif nums[i] * nums[i] < nums[j] * nums[j]:
                ans.append(nums[i] * nums[i])
                i -= 1
            else:
                ans.append(nums[j] * nums[j])
                j += 1

        return ans

#优化的双指针，从两边向中间
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j, k = 0, n-1, n-1
        ans = [0]*n
        while i <= j:
            x = nums[i]**2
            y = nums[j]**2
            if x > y:
                ans[k] = x
                i += 1
                k -= 1
            else:
                ans[k] = y
                j -= 1
                k -= 1
        return ans

