"""
Given the head of a singly linked list, swap every two nodes and return its head.
For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
"""
def swapPairs(head):
    
    ### Iterative Method
    # if not head:
    #     return None
    # cur = head.next if head.next else head
    # prev = None
    # while head and head.next:
    #     temp = head.next
    #     head.next = head.next.next
    #     temp.next = head
    #     head = head.next
    #     if prev:
    #         prev.next = temp
    #     prev = temp.next
    # return cur

    # Recursive Method
    if head is None or head.next is None:
        return head
    nextHead = head.next.next
    newHead = head.next
    head.next.next = head
    head.next = swapPairs(nextHead)
    return newHead
