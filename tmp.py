def maxArea(height: list[int]) -> int:
    i = 0
    j = 1
    area = -1
    # area = length * width

    while i < len(height) - 1:
        width = (j - i)
        currentArea = min(height[i], height[j]) * width
        if (currentArea > area):
            area = currentArea

        j += 1
        if (j >= len(height)):
            i += 1
            j = i + 1

    return area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
