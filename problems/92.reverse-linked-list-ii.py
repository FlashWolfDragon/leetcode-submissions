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
        prev = rightNode = None
        curr = head
        reversing = False
        count = 1

        if (left >= right):
            return head

        while (curr):
            if count == right:
                rightNode = curr
                afterRightNode = curr.next
            count += 1
            curr = curr.next

        curr = head
        count = 0
        while (curr):
            next_node = curr.next
            count += 1

            if count == left:
                reversing = True
                if (prev):
                    prev.next = rightNode
                else:
                    head = rightNode
                curr.next = afterRightNode
                prev = curr
                curr = next_node
                continue

            if count == right:
                curr.next = prev
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
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# res = Solution().reverseBetween(head, 2, 4)
# print(res)

# [a -> b -> c]
head = ListNode('a', ListNode('b', ListNode('c')))
res = Solution().reverseBetween(head, 1, 3)
print(res)