#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#

from collections import deque

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root) -> int:
        ans = 0
        queue = deque([root])

        while queue:
            ans = 0
            for node in queue:
                ans += node.val

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans
            
        
# @lc code=end

