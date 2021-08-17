#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Dict = self.addToDict(s1)

        # wasLastValid = True
        currentPermutation = ""

        for i, char in enumerate(s2):
            if s1Dict.get(char, 0) > 0:
                # character from s1 can be used
                currentPermutation += char
                s1Dict[char] -= 1
            elif len(s2[i::] > len(s1)):
                break
            else:
                s1Dict = self.addToDict(currentPermutation)
                currentPermutation = ""

                # needs to reset s1Dict if combo break
                # abc, aczzbzzazzbac
                # abc, ababc
                # abc, abbac
        for value in s1Dict.values():
            if value > 0:
                return False

        return True

    def addToDict(self, string: str, existingDict: dict = {}) -> dict:
        for char in string:
            existingDict[char] = existingDict.get(char, 0) + 1

        return existingDict

# @lc code=end
