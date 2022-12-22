# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None
#
def solution(a, b):
    """
    new_a = reverse_linked_list(a)
    new_b = reverse_linked_list(b)
    curr_a, curr_b = new_a, new_b
    carry = 0
    new_head = None
    prev = None
    while curr_a is not None or curr_b is not None:
        curr, carry = add_list_elem(curr_a, curr_b, carry)
        if prev:
            prev.next = curr
            prev = curr
        if new_head is None:
            new_head = curr
            prev = curr
        if curr_a:
            curr_a = curr_a.next
        if curr_b:
            curr_b = curr_b.next
    if carry:
        curr = ListNode(carry)
        prev.next = curr
    new_head = reverse_linked_list(new_head)
    # reverse the inputed lists back, try to avoid side effects
    reverse_linked_list(new_a)
    reverse_linked_list(new_b)
    return new_head


def reverse_linked_list(head):
    """  # reverse linked list, tail becomes head and new head is returned
    """
    if head is None:
        return None
    curr, prev = head, None
    while curr is not None:
        tmp = curr
        curr = curr.next
        tmp.next = prev
        prev = tmp
    return prev

def add_list_elem(in1, in2, carry):
    #addition of two nodes with carry_in and carry_out
    in1_val = in1.value if in1 else 0
    in2_val = in2.value if in2 else 0
    tmp = in1_val + in2_val + carry
    return ListNode(tmp % 10000), tmp // 10000
    
    """

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

    result = []

    # Start with a dummy node to hold the result
    dummy = ListNode(0)
    curr = dummy

    # Keep track of the carry over
    carry = 0

    # Loop through both linked lists until we reach the end of both
    while a or b:
        # Get the values at the current nodes of each list
        # If the current node is None, use 0 as the value
        x = a.value if a else 0
        y = b.value if b else 0

        # Add the values and the carry over
        s = x + y + carry

        # Calculate the new carry over
        carry = s // 10000

        # Append the last 4 digits of the sum to the result
        curr.next = ListNode(s % 10000)
        curr = curr.next

        # Move to the next node in both lists
        if a:
            a = a.next
        if b:
            b = b.next

    # Check if there is a final carry over
    if carry:
        curr.next = ListNode(carry)

    # Return the result, skipping the dummy node
    curr = dummy.next
    while curr:
        result.append(curr.value)
        curr = curr.next
    return result
