"""
Given a singly linked list and an integer k, remove the kth last element from the list. 
k is guaranteed to be smaller than the length of the list.
The list is very long, so making more than one pass is prohibitively expensive.
Do this in constant space and in one pass.
"""
def removeKthFromEnd(head, k):
    p1 = p2 = head
    for i in range(k):
        p1 = p1.next
    if not p1:
        return p2.next
    while p1.next != None:
        p1 = p1.next
        p2 = p2.next
    p2.next = p2.next.next
    return head