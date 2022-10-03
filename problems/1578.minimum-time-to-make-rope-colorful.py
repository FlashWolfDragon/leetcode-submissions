def minCost(colors: str, neededTime: list[int]) -> int:
    currentIndex = 0
    nextIndex = 1
    totalTime = 0

    while currentIndex <= len(colors) and nextIndex < len(colors):
        if (colors[currentIndex] == colors[nextIndex]):
            # duplicate colors
            waitTimes = [neededTime[currentIndex]]
            while nextIndex < len(colors) and colors[currentIndex] == colors[nextIndex]:
                # find end of duplicate colors
                waitTimes.append(neededTime[nextIndex])
                nextIndex += 1
                if (nextIndex == len(colors) or colors[currentIndex] != colors[nextIndex]):
                    # count
                    waitTimes.sort()
                    totalTime += sum(waitTimes[:-1])
                    currentIndex = nextIndex - 1
                    waitTimes.clear()
                    
        currentIndex += 1
        nextIndex += 1

    return totalTime


result = minCost("aaabbbabbbb", [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1])
# result = minCost("abaac", [1, 2, 3, 4, 5])
print(result)
