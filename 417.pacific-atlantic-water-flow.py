#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (38.07%)
# Likes:    750
# Dislikes: 135
# Total Accepted:    49.8K
# Total Submissions: 130.5K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and top
# edges of the matrix and the "Atlantic ocean" touches the right and bottom
# edges.
# 
# Water can only flow in four directions (up, down, left, or right) from a cell
# to another one with height equal or lower.
# 
# Find the list of grid coordinates where water can flow to both the Pacific
# and Atlantic ocean.
# 
# Note:
# 
# 
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# 
# 
# 
# 
# Example:
# 
# 
# Given the following 5x5 matrix:
# 
# ⁠ Pacific ~   ~   ~   ~   ~ 
# ⁠      ~  1   2   2   3  (5) *
# ⁠      ~  3   2   3  (4) (4) *
# ⁠      ~  2   4  (5)  3   1  *
# ⁠      ~ (6) (7)  1   4   5  *
# ⁠      ~ (5)  1   1   2   4  *
# ⁠         *   *   *   *   * Atlantic
# 
# Return:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
# parentheses in above matrix).
# 
# 
# 
# 
#

class Solution:
         
    def dfs(self, matrix, i, j, visited, m, n):
        visited[i][j] = True
        for dir in self.directions:
            x, y = i + dir[0], j + dir[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(matrix, x, y, visited, m, n)
            
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return 
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m = len(matrix)
        n = len(matrix[0])
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        result = []
            
        for i in range(m):
            self.dfs(matrix, i, 0, p_visited, m, n)
            self.dfs(matrix, i, n-1, a_visited, m, n)
        for j in range(n):
            self.dfs(matrix, 0, j, p_visited, m, n)
            self.dfs(matrix, m-1, j, a_visited, m, n)
            
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    result.append([i,j])
        return result
    
#         ret= []
#         if not matrix: return None
#         m = len(matrix)
#         n = len(matrix[0])
#         direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
#         def dfs(x, y, visited_p, m, n):
#             for i, j in self.direction:
#                 x, y = x + i, y + j
#                 if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] > matrix[x-i][y-j]:
#                     continue
#                 visited_p[x][y] = True

                    
#         def waterFlowA(i, j):
#             if i == m - 1 or j == n - 1:
#                 return 1
#             else:
#                 if (i+1 < m and matrix[i][j] >= matrix[i+1][j]) or (
#                     j+1 < n and matrix[i][j] >= matrix[i][j+1]):
#                     return waterFlowA(i+1, j) or waterFlowA(i, j+1)
#             return 0
            
#         for i in range(m):
#             for j in range(n):
#                 if waterFlowP(i,j) and waterFlowA(i, j):
#                     ret.append([i,j])
        
#         return ret
        
