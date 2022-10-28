#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums) -> int:
        seen = set(nums)

        for i in range(0, len(nums) + 1):
            if i not in seen:
                return i
        return None

        
# @lc code=end

Solution().missingNumber([0,1])