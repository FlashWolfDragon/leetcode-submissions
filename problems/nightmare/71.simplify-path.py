#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        if (len(path) == 1):
            return '/'
        
        for i, c in enumerate(path):
            if stack and stack[-1] == '/' and c == '/':
                stack.pop()

            if len(stack) >= 2 and stack[-2] == '/' and stack[-1] == '.' and c == '/':
                stack.pop()
                continue

            if stack and stack[-1] == '.' and c == '.':
                if (stack[-2] == '.' and stack[-1] == '.' and c == '.'):
                    stack.append('.')
                    continue
                if (i < len(path) - 1 and path[i + 1] == '.'):
                    stack.append('.')
                    continue

                if (stack[-2] == '.' and stack[-1] == '.' and c == '/'):
                    stack.pop() # .
                    stack.pop() # /
                    if not stack:
                        stack.append('/')
                        continue

                    while stack[-1] != '/':
                        stack.pop()
                continue

            stack.append(c)
        
        if len(stack) > 1 and stack[-2:] == ['/', '.']: 
            stack.pop()
            stack.pop()

        if (stack[-2] == '.' and stack[-1] == '.'):
            stack.pop() # .
            stack.pop() # .
            stack.pop() # /

            while stack[-1] != '/':
                stack.pop()

        if len(stack) > 1 and stack[-1] == '/': stack.pop()
        res = ''.join(stack)
        if not res: return '/'
        return res


        
# @lc code=end

ans = Solution().simplifyPath('/a/./b/../../c/')
# ans = Solution().simplifyPath('/a/..../b')
# "/a//b////c/d//././/.."
print(ans)

ans = Solution().simplifyPath('/a//b////c/d//././/..')
# ans = Solution().simplifyPath('/..hidden')

print(ans)
# /c
