#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        pairs = defaultdict(int)
        for x in nums2:
            while stack and stack[-1] < x:
                pairs[stack.pop()] = x
            stack.append(x)

        res = []
        for y in nums1:
            curr = pairs[y]
            if curr:
                res.append(curr)
            else:
                res.append(-1)

        return res
# @lc code=end
# print(Solution().nextGreaterElement([4,1,2], [1,3,4,2]))
print(Solution().nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7]))

