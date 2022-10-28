#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
import string


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        for c in sentence:
            seen.add(c)
            
        for c in string.ascii_lowercase:
            if c not in seen:
                return False
                
        return True
        
# @lc code=end

