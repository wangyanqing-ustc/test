# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0, next = head)
        pre = res
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next

            pre.next = post
            tmp = post.next
            post.next = cur
            cur.next = tmp
            pre = cur

        return res.next