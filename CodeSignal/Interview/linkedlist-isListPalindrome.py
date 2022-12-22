# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l):
    a = []
    while l != None:
        a.append(l.value)
        l = l.next
    return a == a[::-1]


"""

def solution(l):
    if l is None:
        return True
        
    ll = len_linked_list(l)
    if ll == 1:
        return True
    breakup, curr = None, l
    breakupIdx = (ll + 1) // 2 - 1
    idx = 0
    while idx < breakupIdx:
        curr = curr.next
        idx += 1
    breakup = curr
    target = breakup.next
    breakup.next = None
    newHead = reverse_linked_list(target)
    curr, newCurr = l, newHead
    palindrome = True
    while curr is not None and newCurr is not None:
        if curr.value != newCurr.value:
            palindrome = False
            break
        curr = curr.next
        newCurr = newCurr.next
    if curr is not None and ll % 2 == 0:
        palindrome = False
    reverse_linked_list(newHead)
    breakup.next = target
    return palindrome    
        
def reverse_linked_list(l):
    if l is None:
        return l
    curr, prev = l, None
    while curr is not None:
        tmp = curr
        curr = curr.next
        tmp.next = prev
        prev = tmp
    return prev

def len_linked_list(l):
    if l is None:
        return 0
    ll = 0
    curr = l
    while curr is not None:
        curr = curr.next
        ll += 1
    return ll

"""
