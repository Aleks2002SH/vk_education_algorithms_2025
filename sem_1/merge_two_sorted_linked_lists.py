class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy =  ListNode()
        prev = dummy
        cur_1 = list1
        cur_2 = list2
        while (cur_1 != None) and (cur_2 != None):
            if cur_1.val <= cur_2.val:
                prev.next = cur_1
                cur_1 = cur_1.next
            else:
                prev.next = cur_2
                cur_2 = cur_2.next
            prev = prev.next
        if cur_1 == None:
            prev.next = cur_2
        elif cur_2 == None:
            prev.next = cur_1
        return dummy.next
        