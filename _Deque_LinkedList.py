from exceptions import Empty
class DequeLinked:
    class _Node:
        __slots__="_element","_next"
        def __init__(self,element,_next):
            self._element=element
            self._next=_next
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def add_first(self,e):
        newNode=self._Node(e,None)
        if self.is_empty():
            self._head=newNode
            self._tail=newNode
        else:
            newNode._next=self._head
        self._head=newNode
        self._size+=1
    def add_last(self,e):
        newNode=self._Node(e,None)
        if self.is_empty():
            self._head=newNode
            self._tail=newNode
        else:
            self._tail._next=newNode
        self._tail=newNode
        self._size+=1
    def remove_first(self):
        if self.is_empty():
            raise Empty("Empty Queue")
        value=self._head._element
        self._head=self._head._next
        if self.is_empty():
            self._tail=None
        self._size-=1
        return value
    def remove_last(self):
        value=0
        if self.is_empty():
            raise Empty("Empty Queue")
        temp=self._head
        if len(self)==1:
            self._tail=None
            self._head=None
        else:
            while temp._next._next:
                temp=temp._next
            value=temp._element
            self._tail=temp
            self._tail._next=None
        self._size-=1
        return value
    def display(self):
        temp=self._head
        if temp==None:
            print("Non items to prints")
        while temp:
            print(temp._element,end ="-->")
            temp=temp._next
        print()
if __name__=="__main__":
    d=DequeLinked()
    d.add_first(10)
    d.add_first(20)
    d.add_first(30)
    d.add_last(50)
    d.add_last(60)
    d.add_first(100)
    d.display()
    d.remove_last()
    d.display()
    d.remove_last()
    d.display()
    d.remove_first()
    d.display()
    d.remove_first()
    d.display()
    d.remove_last()
    d.display()
    d.remove_last()
    d.display()


