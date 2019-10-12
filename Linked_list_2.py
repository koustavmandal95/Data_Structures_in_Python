class SinglyLinkedList:
    def __init__(self):
        self.head=None
class SinglyLinkedListNode:
    __slots__="data","next"
    def __init__(self,data):
        self.data=data
        self.next=None
def insertNodeAtHead(head, data):
    node = SinglyLinkedListNode(data)
    if head!=None: # head has some previous element
        node.next = head
    head=node.next
    return node
def printLinkedList(head):
    temp=head
    while temp:
        print(temp.data,end=' ')
        temp=temp.next
if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    printLinkedList(llist.head)
