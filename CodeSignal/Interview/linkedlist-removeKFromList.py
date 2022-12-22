# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def solution(l, k):

    # si es vacia devuleva vacio
    if l == None:
        return l

    # si el primer nodo es igual a k, empiece desde el segundo
    while l != None and l.value == k:
        l = l.next

    n = l
    # para recorrer los nodos hay que tener otro apuntdor, pero seria la misma lista, por eso se necesita n

    while n != None and n.next != None:
        if n.next.value == k:
            n.next = n.next.next
        else:
            n = n.next

    return l


"""
def solution(l, k):
    c = l
    while c: #mientras el apuntador apunte un nodo
        if c.next and c.next.value == k: #si exite un nodo siguiente y si el valor del nodo sigiente es k
            c.next = c.next.next #saltese el siguiente
        else:
            c = c.next #sino vaya al siguiente 
    return l.next if l and l.value == k else l #verifique que el primer valor de l no es k
    
    """
