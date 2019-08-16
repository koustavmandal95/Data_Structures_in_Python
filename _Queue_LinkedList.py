class LinkedQueue:
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
    def enqueue(self,e):
        new=self._Node(e,None)
        if self.is_empty():
            self._head=new
        else:
            self._tail._next=new
        self._tail=new
        self._size+=1
    def dequeue(self):
        if self.is_empty():
            raise Empty("The queue is empty")
        value=self._head._element
        self._head=self._head._next
        self._size+-1
        if self.is_empty():
            self._tail=None
        return value
    def first(self):
        if self.is_empty():
            raise Empty("Queue is element")
        return self._head._element
    def display(self):
        temp=self._head
        while temp:
            print(temp._element,end="-->")
            temp=temp._next
        print()

if __name__=="__main__":
    q=LinkedQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.display()
    q.dequeue()
    q.dequeue()
    q.display()


