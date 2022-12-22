# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l, n):

    ptr = l
    lenl = 0
    while ptr:
        if ptr.next == None:
            last = ptr

        ptr = ptr.next
        lenl += 1
    ptr = l

    if n == 0 or n == lenl:
        return l

    for i in range(lenl-n-1):
        ptr = ptr.next
        print(ptr.value)

    root = ptr.next
    print(root.value, ptr.value, last.value, "----", lenl, n)
    ptr.next = None
    last.next = l

    return root


def printList(head):
    ptr = head
    while ptr:
        print(ptr.value, end=' —> ')
        ptr = ptr.next
    print('None')


def lenll(head):
    ptr = head
    lenl = 0
    while ptr:
        ptr = ptr.next
        lenl += 1
    return lenl
