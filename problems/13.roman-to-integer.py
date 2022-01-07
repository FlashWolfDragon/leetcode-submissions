#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"M": 1000, "D": 500, "C": 100,
                 "L": 50, "X": 10, "V": 5, "I": 1}

        sum = 0
        for x in range(0, len(s) - 1):
            current = roman[s[x]]
            next = roman[s[x + 1]]
            if (next > current):
                sum -= current 
            else:
                sum += current
        sum += roman[s[-1]]

        return sum
# @lc code=end


s = Solution()
print(s.romanToInt('IV'))
