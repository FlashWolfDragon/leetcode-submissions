#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteCount = defaultdict(int)
        for c in ransomNote:
            noteCount[c] += 1
            
        magazineCount = defaultdict(int)
        for c in magazine:
            magazineCount[c] += 1
            
        for k in noteCount:
            if (noteCount[k] > magazineCount[k]):
                return False
            
        return True
               
# @lc code=end

