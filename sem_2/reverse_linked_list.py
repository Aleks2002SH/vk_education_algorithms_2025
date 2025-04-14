class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):

    prev = None
    cur = head

    while cur!=None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    head = prev

    return head


        