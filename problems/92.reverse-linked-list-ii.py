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
        prev = None
        curr = head
        reversing = False
        leftNode = None
        rightNode = None

        while (curr):
            if curr.val == left:
                leftNode = curr
            elif curr.val == right:
                rightNode = curr
                afterRightNode = curr.next
            
            curr = curr.next

        curr = head

        while (curr):
            next_node = curr.next
            if curr.val == left:
                reversing = True
                prev.next = rightNode
                curr.next = afterRightNode
                prev = curr
                curr = next_node
                continue

            if curr.val == right:
                return head

            if reversing:
                curr.next = next_node
                curr.next = prev
                prev = curr
                curr = next_node
                continue

            prev = curr
            curr = next_node




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

# [1 -> 2 -> 3 -> 4 -> 5]
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
res = Solution().reverseBetween(head, 2, 4)
print(res)
