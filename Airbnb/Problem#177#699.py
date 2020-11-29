"""

Given a linked list and a positive integer k, rotate the list to the right by k places.
For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.
Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.
"""
def rotateRight(head, k):
    if not head:
        return
    l = length(head)
    k = k % l
    if l == 1 or k % l == 0:
        return head
    count = 0
    curr = head
    while count < l-k:
        prev = head
        head = head.next
        count += 1
    prev.next = None
    result = head
    while head.next:
        head = head.next
    head.next = curr
    return result


def length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count
