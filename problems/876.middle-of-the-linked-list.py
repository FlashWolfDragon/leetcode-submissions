#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        fast = head
        slow = head
        while (fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next
        if (fast.next):
            return slow.next
        return slow

# @lc code=end
