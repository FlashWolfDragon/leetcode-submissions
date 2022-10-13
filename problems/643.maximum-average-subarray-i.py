#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        # k == window size
        if (len(nums) <= k):
            return sum(nums) / len(nums)

        currSum = sum(nums[:k])
        maxAvg = currSum / k
        # next case
        i = 0
        j = k

        while (j < len(nums)):
            # update sum
            currSum += nums[j] - nums[i] 
            maxAvg = max(currSum / k, maxAvg)
            i += 1
            j += 1

        return maxAvg
# @lc code=end

s = Solution()
a = s.findMaxAverage([1,12,-5,-6,50,3], 4)
print(a)

