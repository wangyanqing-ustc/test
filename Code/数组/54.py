from typing import List
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         m, n = len(matrix), len(matrix[0])
#         loop = min(m, n) // 2
#         S = m*n
#         res = []
#         count = 0
#         startx, starty = -1, -1
#         offset = 0
#         while True:#应该可以有另一种写法，准确给出循环圈数，从而避免下面不停地判断count是否到达终点
#             offset += 1
#             startx += 1
#             starty += 1
#             if count == S - 1:
#                 res.append(matrix[startx][starty])
#                 return res
#             for j in range(starty, n - offset):
#                 res.append(matrix[startx][j])
#                 count += 1
#                 if count == S:
#                     return res
#             for i in range(startx, m - offset):
#                 res.append(matrix[i][n - offset])
#                 count += 1
#                 if count == S:
#                     return res
#             for j in range(n - offset, starty, -1):
#                 res.append(matrix[m - offset][j])
#                 count += 1
#                 if count == S:
#                     return res
#             for i in range(m - offset, startx, -1):
#                 res.append(matrix[i][starty])
#                 count += 1
#                 if count == S:
#                     return res

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        loop = min(m, n) // 2#完整的循环次数
        res = []
        startx, starty = -1, -1
        offset = 0
        for _ in range(loop):
            offset += 1
            startx += 1
            starty += 1
            for j in range(starty, n - offset):
                res.append(matrix[startx][j])
            for i in range(startx, m - offset):
                res.append(matrix[i][n - offset])
            for j in range(n - offset, starty, -1):
                res.append(matrix[m - offset][j])
            for i in range(m - offset, startx, -1):
                res.append(matrix[i][starty])
        min_ = min(m, n)
        if min_ % 2 == 0:#判断是否有残存的不完整循环
            return res
        else:
            startx += 1
            starty += 1
            if min_ == m:#只剩下一行
                for j in range(starty, n - offset):
                    res.append(matrix[startx][j])
                return res
            else:#只剩下一列
                for i in range(startx, m - offset):
                    res.append(matrix[i][starty])
                return res
                
                
                
        
    
solution = Solution()
matrix = matrix = [[1]]
res = solution.spiralOrder(matrix)
print(res)
            
            