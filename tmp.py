
def substrings(s: str) -> int:
    if (len(s) <= 2):
        return len(s)

    i = maxLength = 0
    j = 1
    seen = [s[0]]
    while (j < len(s)):
        if (len(seen) == 1 and s[j] not in seen):
            seen.insert(0, s[j])

        if (s[j] not in seen):
            seen.pop()
            seen.insert(0, s[j])
            while (s[i] not in seen):
                i += 1

        maxLength = max(maxLength, (j - i) + 1)
        j += 1

    return maxLength


print(substrings("abaccc"))
