#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for portion in path.split('/'):
            if (portion == '..'):
                if stack: stack.pop()
                continue
            if (portion == '.' or portion == ''):
                continue
            stack.append(portion)
        return '/' + '/'.join(stack)
        
# @lc code=end
ans = Solution().simplifyPath('/a/b/////c/////d/..')
print(ans)
