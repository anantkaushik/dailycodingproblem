"""
Given a linked list and an integer k, remove the k-th node from the end of the list and return the head of the list.
k is guaranteed to be smaller than the length of the list.
Do this in one pass.
"""
def removeNthFromEnd(head, k):
    fast = head
    for i in range(k):
        fast = fast.next
    
    if not fast:
        return head.next
    
    slow = head
    while fast and fast.next:
        fast = fast.next
        slow = slow.next 
    
    slow.next = slow.next.next
    
    return head
