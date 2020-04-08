"""
Given the head of a singly linked list, reverse it in-place.
"""
def reverseList(head):
        cur, prev = head, None
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        return prev
