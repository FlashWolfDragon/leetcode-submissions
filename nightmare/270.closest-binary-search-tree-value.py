# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root, target: float) -> int:
        target = round(target)
        currentNode = root
        while currentNode:
            if currentNode.val == target:
                return currentNode.val

            if target < currentNode.val:
                if currentNode.left and (abs(currentNode.val - target) > abs(currentNode.left.val - target)):
                    currentNode = currentNode.left
                else:
                    return currentNode.val

            if target > currentNode.val:
                if currentNode.right and (abs(currentNode.val - target) > abs(currentNode.right.val - target)):
                    currentNode = currentNode.right
                else:
                    return currentNode.val

# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4
root = TreeNode(4, left=TreeNode(2,left=TreeNode(1),right=TreeNode(3)), right=TreeNode(5))
ans = Solution().closestValue(root, 3.714286)
print(ans)
