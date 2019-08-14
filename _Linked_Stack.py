from exceptions import Empty
class LinkedStack:
    class _Node:
        __slots__="_element","_next"

        def __init__(self,element,_next):
            self._element=element
            self._next=_next
    def __init__(self):
        self.size=0
        self.head=None
    def __len__(self):
        print(self._size)
    def is_empty(self):
        return self.size==0
    def push(self,e):
        self.head=self._Node(e,self.head)
        self.size+=1
    def pop(self):
        if self.is_empty():
            raise Empty("The stack is empty")
        else:
            value=self.head
            self.head=self.head._next
        self.size-=1
        return value._element
    def display(self):
        thead=self.head
        while thead!=None:
            print(thead._element,end='-->')
            thead=thead._next
        print()
if __name__=="__main__":
    s=LinkedStack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)
    s.display()
    s.pop()
    s.pop()
    print(s.pop())
    s.display()


