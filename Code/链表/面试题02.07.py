# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_A = 0
        cur = headA
        while cur:
            len_A += 1
            cur = cur.next
        len_B = 0
        cur = headB
        while cur:
            len_B += 1
            cur = cur.next
        
        
        if len_A > len_B:
            cur_long = headA
            cur_short = headB
        else:
            cur_long = headB
            cur_short = headA

        delta = abs(len_A - len_B)
        while delta:
            cur_long = cur_long.next
            delta -= 1
        while cur_long:
            if cur_long == cur_short:
                return cur_long
            cur_long = cur_long.next
            cur_short = cur_short.next
        return None