#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)  # rows
        n = len(matrix[0])  # columns

        for row in range(m):
            foundZeroInRow = False
            for column in range(n):
                # if 0 found, apply changes to row and column
                if matrix[row][column] == 0:
                    # if this is the first 0 found in this row, apply 0 to previous elements visited in this row
                    if not foundZeroInRow:
                        for i in range(column+1):
                            matrix[row][i] = 0
                        foundZeroInRow = True

                    # apply 0 to previous elements visited in column
                    for i in range(row+1):
                        matrix[i][column] = 0

                    # change value of next elements in column different than 0 to "replace"
                    for i in range(row, m):
                        if matrix[i][column] != 0:
                            matrix[i][column] = "replace"

                elif matrix[row][column] == "replace" or foundZeroInRow:
                    matrix[row][column] = 0

# @lc code=end
