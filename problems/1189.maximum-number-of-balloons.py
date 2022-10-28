#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = defaultdict(int)
        for c in text:
            counts[c] += 1

        return int(min([
            counts['b'] / 1,
            counts['a'] / 1,
            counts['l'] / 2,
            counts['o'] / 2,
            counts['n'] / 1
        ]))
        
# @lc code=end

