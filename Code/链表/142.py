# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head) :
        slow, fast = head, head
        tag = 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                index1 = slow
                tag = 0
                break
            
        if tag:
            return None
        index2 = head
        while True:
            if index1 == index2:
                return index1
            index1 = index1.next
            index2 = index2.next
            
t = [3, 2, 0, -4]
pos = 1
dummy = ListNode(0)
cur = dummy
for i in range(len(t)):
    cur.next = ListNode(t[i])
    cur = cur.next
    if i == pos:
        tmp = cur
cur.next = tmp

head = dummy.next
solution = Solution()
res = solution.detectCycle(head)
print(res)

    