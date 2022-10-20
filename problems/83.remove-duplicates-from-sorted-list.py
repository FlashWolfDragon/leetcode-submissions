#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if (not head):
            return None
        if (not head.next):
            return head
            
        seen = [head.val]
        prev = head
        curr = head.next
        while (curr):
            if (curr.val not in seen):
                seen.append(curr.val)
                curr = curr.next
                prev = prev.next
                continue
            # remove node
            prev.next = curr.next
            curr = curr.next

        return head


            

# @lc code=end

