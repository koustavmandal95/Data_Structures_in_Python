class LinkedList:
    class _Node:
        __slots__='_element','_next'

        def __init__(self,element,nxt):
            self._element=element
            self._next=nxt
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def add_first(self,e):
        newest=self._Node(e,None)
        if self.is_empty():
            self._head=newest
            self._tail=newest
        else:
            newest._next=self._head #so the address of the previous head is not lost
        self._head=newest
        self._size=self._size+1
    def add_last(self,e):
        newest=self._Node(e,None)
        if self.is_empty():
            self._head=newest
            self._tail=newest
        else:
            self._tail._next=newest
        self._tail=newest
        self._size = self._size+1
    def add_any(self,e,pos):
        newest=self._Node(e,None)
        thead=self._head
        i=1
        while i<pos-1:
            thead=thead._next
            i+=1
        newest._next=thead._next  #so the address of the previous head is not lost
        thead._next=newest
        self._size+=1
    def remove_first(self):
        if self.is_empty():
            raise Empty("Linked list empty")
        value = self._head._element
        self._head=self._head._next
        self._size=self._size-1
        if self.is_empty():
            self._tail=None
        return value
    def remove_last(self):
        if self.is_empty():
            raise Empty("Linked list empty")
        thead=self._head
        i=0
        while i <len(self)-2:
            thead=thead._next
            i+=1
        self.tail=thead
        thead=thead._next
        value = thead._element
        self._size-=1
        self.tail._next=None
        return value
    def remove_any(self,pos):
        if self.is_empty():
            raise Empty("Linked list empty")
        thead=self._head
        i=0
        while i<pos-2:
            thead=thead._next
            i+=1
        value=thead._next._element
        thead._next=thead._next._next
        self._size-=1
        return value
    def display(self):
        thead=self._head
        while thead:
            print(thead._element,end='--->')
            thead=thead._next
        print()
if __name__=="__main__":
    L=LinkedList()
    L.add_last(10)
    L.add_first(20)
    L.add_last(30)
    L.add_last(40)
    L.add_first(50)
    L.add_last(60)
    L.add_any(100,4)
    L.display()
    print("The deleted item:",L.remove_last())
    L.display()
    print("The deleted item:",L.remove_first())
    L.display()
    print("The deleted item:",L.remove_any(3))
    L.display()
        



 