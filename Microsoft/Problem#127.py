"""
Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.
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
def addTwoNumbers(l1, l2):
    newL = ListNode(0)
    cur = newL
    carry = 0
    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        summ = x + y + carry
        carry = summ // 10
        cur.next = ListNode(summ%10)
        cur = cur.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if carry:
        cur.next = ListNode(carry)
    return newL.next