from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums) -> int:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1

        single_nums = [x for x in counts if counts[x] == 1]
        if (len(single_nums) == 0):
            return -1
        return max(single_nums)
        

ans = Solution().largestUniqueNumber([1, 1, 2])
print(ans)