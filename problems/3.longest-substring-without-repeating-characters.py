#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = right = 0
        longest = 0
        
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest = max(len(seen), longest)
            right += 1

        return longest

# @lc code=end

s = Solution()
ans = s.lengthOfLongestSubstring('pwwkew')
print(ans)