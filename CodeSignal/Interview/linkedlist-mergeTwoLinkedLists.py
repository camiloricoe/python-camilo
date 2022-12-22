# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None
#
def solution(l1, l2):
    result = []

    # Start with a dummy node to hold the result
    dummy = ListNode(0)
    curr = dummy

    # Loop through both lists until we reach the end of both
    while l1 and l2:
        # Compare the values at the current nodes of each list
        if l1.value <= l2.value:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    # Append the remaining elements of the non-empty list
    curr.next = l1 if l1 else l2

    # Return the result, skipping the dummy node
    curr = dummy.next
    while curr:
        result.append(curr.value)
        curr = curr.next
    return result
