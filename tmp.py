def findMaxAverage(nums, k: int) -> float:
    # k == window size
    currSum = sum(nums[:k])
    maxAvg = currSum / k
    i = 0
    j = k
    if (len(nums) <= k):
        return sum(nums) / len(nums)

    while (j < len(nums)):
        currSum += nums[j] - nums[i - 1]
        maxAvg = max(currSum / k, maxAvg)
        i += 1
        j += 1

    return maxAvg
        
a = findMaxAverage([])
print(a)