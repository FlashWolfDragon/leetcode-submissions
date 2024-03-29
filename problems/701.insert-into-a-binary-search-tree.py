#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int):
        newNode = TreeNode(val)
        if not root:
            return newNode

        currentNode = root
        while True:
            if currentNode.val > val:
                if currentNode.left:
                    currentNode = currentNode.left
                else:
                    currentNode.left = newNode
                    return root
            else:
                if currentNode.right:
                    currentNode = currentNode.right
                else:
                    currentNode.right = newNode
                    return root


# @lc code=end
