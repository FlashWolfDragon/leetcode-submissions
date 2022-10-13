#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums, k: int) -> int:
        i = j = zeros = maxSize = 0

        while (j < len(nums)):
            if (nums[j] == 0):
                zeros += 1

            while (zeros > k):
                i += 1
                if (nums[i - 1] == 0):
                    zeros -= 1

            maxSize = max(maxSize, (j - i) + 1)
            j += 1

        return maxSize


# @lc code=end
s = Solution()
print(s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
