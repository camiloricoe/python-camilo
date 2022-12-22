# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l, k):

    if k == 1 or k == 0:
        return l

    primero = l
    alacola = l.next
    head = primero
    a = lenll(l)//k
    print(a)
    for i in range(a):
        for j in range(k-1):
            primero.next = alacola.next
            alacola.next = head
            head = alacola
            alacola = primero.next
        if i == 0:
            root = head
            anterior = primero
        else:
            anterior.next = head
            anterior = primero

        if primero.next != None:
            primero = primero.next
            alacola = primero.next
            head = primero

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
