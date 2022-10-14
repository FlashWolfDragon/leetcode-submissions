class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if (len(s) <= 2):
            return len(s)

        i = maxLength = 0
        j = 1
        seen = [s[0]]
        while (j < len(s)):
            if (len(seen) == 1 and s[j] not in seen):
                seen.insert(0, s[j])

            if (s[j] not in seen):
                while (len(set(s[i:j + 1])) > 2):
                    i += 1
                seen = list(s[i:j + 1])

            maxLength = max(maxLength, (j - i) + 1)
            j += 1

        return maxLength
