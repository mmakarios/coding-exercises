#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        strDict = {}

        for char in t:
            strDict[char] = strDict.get(char, 0) + 1

        for char in s:
            if strDict.get(char, 0) < 1:
                return False
            else:
                strDict[char] -= 1

        return True
# @lc code=end
