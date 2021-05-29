# @before-stub-for-debug-begin
from python3problem443 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        s = ""
        count = 1

        for i, currentChar in enumerate(chars[1::], start=1):
            if currentChar == chars[i-1]:
                count += 1
            else:
                s += chars[i-1] + str(count) if count > 1 else chars[i-1]
                count = 1

        s += currentChar + str(count) if count > 1 else currentChar
        chars[:] = list(s)
        return len(chars)
# @lc code=end
