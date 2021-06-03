# @before-stub-for-debug-begin
from python3problem48 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        row = 0
        while row <= (n/2)-1:
            for column in range(row, n-1-row):
                temp = matrix[column][n-1-row]
                matrix[column][n-1-row] = matrix[row][column]
                matrix[row][column] = matrix[n-1-column][row]
                matrix[n-1-column][row] = matrix[n-1-row][n-1-column]
                matrix[n-1-row][n-1-column] = temp
            row += 1
# @lc code=end
