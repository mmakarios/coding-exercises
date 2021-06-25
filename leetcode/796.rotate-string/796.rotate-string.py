#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # abcab - ababc
        if len(s) != len(goal):
            return False
        if s == goal:
            return True

        for i in range(len(s)):
            firstChar = s[0]
            s = s[1::] + firstChar

            if s == goal:
                return True

        return False
# @lc code=end
