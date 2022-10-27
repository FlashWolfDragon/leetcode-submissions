#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left: int, right: int):
        count = 0
        prev = None
        curr = head
        while (curr and count <= left):
            count += 1
            curr = curr.next
            prev = curr

        while (curr and count >= left and count <= right):
            count += 1
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        while (curr):
            count += 1
            curr = curr.next
            prev = curr

        return head


# @lc code=end

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        curr = self
        values = []
        while(curr):
            values.append(curr.val)
            curr = curr.next
        return str(values)

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
res = Solution().reverseBetween(head, 2, 4)
print(res)
