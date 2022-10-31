#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        validStones = set([x for x in jewels])
        count = 0
        
        for x in stones:
            if x in validStones:
                count += 1

        return count

# @lc code=end

