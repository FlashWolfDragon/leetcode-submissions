#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, target, curr, found):
        curr += root.val
        if (curr == target and not root.left and not root.right):
            found[0] = True
            return

        if (root.left):
            self.traverse(root.left, target, curr, found)

        if (root.right):
            self.traverse(root.right, target, curr, found)

        return found[0]

    def hasPathSum(self, root, targetSum: int) -> bool:
        print(root)
        if (not root): return False
        if (not root.left and not root.right):
            return root.val == targetSum

        return self.traverse(root, targetSum, 0, [False])

# @lc code=end
