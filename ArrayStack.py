from exceptions import Empty
class Arraystack():
    def __init__(self):
        self._data=[]
    def __len(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data)==0
    def push(self,element):
         self._data+=[element]
    def pop(self):
        if self.is_empty():
            raise("stack is empty")
        return self._data.pop()
    def top(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data[-1]

stk=Arraystack()
stk.push(10)
stk.push(20)
print("The length:",stk._len())

