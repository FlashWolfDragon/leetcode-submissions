#
# @lc app=leetcode id=2225 lang=python3
#
# [2225] Find Players With Zero or One Losses
#

# @lc code=start
from collections import defaultdict


class Solution:
    def findWinners(self, matches):
        losses = defaultdict(int)
        for x in matches:
            losses[x[1]] += 1
        
        no_losses = sorted(set([x[0] for x in matches if x[0] not in losses]))
        single_losses = sorted([x for x in losses if losses[x] == 1])
        
        return [no_losses, single_losses]

        
# @lc code=end

