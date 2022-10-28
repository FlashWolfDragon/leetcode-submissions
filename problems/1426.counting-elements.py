class Solution:
    def countElements(self, arr) -> int:
        seen = set(arr)
        count = 0
        for i in arr:
            if i + 1 in seen:
                count += 1
        return count

ans = Solution().countElements([1,1,3])
print(ans)
        