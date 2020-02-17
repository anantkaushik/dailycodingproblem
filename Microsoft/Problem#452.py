"""
Let's represent an integer in a linked list format by having each node represent a digit in the number. 
The nodes make up the number in reversed order.

For example, the following linked list:
1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.
For example, given
9 -> 9
5 -> 2
return 124 (99 + 25) as:
4 -> 2 -> 1
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      res = cur = ListNode(0)
      nodes_sum = 0
      while l1 or l2 or nodes_sum:
        if l1:
          nodes_sum += l1.val
          l1 = l1.next
        if l2:
          nodes_sum += l2.val
          l2 = l2.next
        cur.next = ListNode(nodes_sum % 10)
        cur = cur.next
        nodes_sum //= 10
      return res.next
