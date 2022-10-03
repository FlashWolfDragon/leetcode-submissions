def minCost(colors: str, neededTime: list[int]) -> int:
    currentIndex = 0
    nextIndex = 1
    totalTime = 0

    while nextIndex < len(colors):
        if (colors[currentIndex] == colors[nextIndex]):
            totalTime += min(neededTime[currentIndex], neededTime[nextIndex])

        currentIndex += 1
        nextIndex += 1

    return totalTime


result = minCost("aaabbbabbbb", [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1])
# result = minCost("abaac", [1, 2, 3, 4, 5])
print(result)
