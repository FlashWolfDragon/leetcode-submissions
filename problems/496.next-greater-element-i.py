#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res = []
        for x in nums1:
            after = found = False
            for y in nums2:
                if (not after and x == y):
                    # find next largest element
                    after = True
                    pass
                if (after and not found and y > x):
                    res.append(y)
                    found = True
            if not found:    
                res.append(-1)
        return res
        
# @lc code=end

