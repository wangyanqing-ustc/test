# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val: int) :
        dummy = ListNode(next = head)#添加一个虚拟节点
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next#删除cur.next节点
            else:
                cur = cur.next
        return dummy.next
    
solution  = Solution()
t = [6,2,6,3,4,5,6]
val = 6
head = ListNode(t[0])
cur = head
for i in range(1,len(t)):
    cur.next = ListNode(t[i])
    cur = cur.next

res = solution.removeElements(head, val)
print(res)