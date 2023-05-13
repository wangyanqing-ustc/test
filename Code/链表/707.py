class LinkList():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

#可以加一个size属性，实时维护链表的长度，便于index范围判断
class MyLinkedList:

    def __init__(self):
        self.dummy = LinkList()

    def get(self, index: int) -> int:
        cur = self.dummy.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        return -1


    def addAtHead(self, val: int) -> None:
        new_node = LinkList(val, self.dummy.next)
        self.dummy.next = new_node

    def addAtTail(self, val: int) -> None:
        new_node = LinkList(val)
        cur = self.dummy
        while cur.next:
            cur = cur.next
        cur.next = new_node
    
    def addAtIndex(self, index: int, val: int) -> None:
        new_node = LinkList(val)
        cur = self.dummy
        i = -1
        while cur:
            if i == index - 1:
                tmp = cur.next
                cur.next = new_node
                new_node.next = tmp
                return
            i += 1
            cur = cur.next
    

    def deleteAtIndex(self, index: int) -> None:
        cur = self.dummy
        i = -1
        while cur and cur.next:
            if i == index - 1:
                cur.next = cur.next.next
                return
            i += 1
            cur = cur.next
            
obj = MyLinkedList()
obj.addAtTail(1)
print(obj.get(0))
