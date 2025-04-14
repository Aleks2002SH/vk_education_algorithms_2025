class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
   
    dummy = ListNode()
    dummy.next = head
    prev = dummy
    cur = head

    while cur!= None:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next

    return dummy.next
    