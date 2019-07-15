class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class LinkedList():
	def __init__(self):
		self.head=None
	def traversal(self):
		temp=self.head
		while temp!=None:
			print(temp.data,end=' ')
			temp=temp.next
	def inbeg(self,new_data):
		new_node=Node(new_data)
		new_node.next=self.head
		self.head=new_node
	def inend(self,new_data):
		new_node=Node(new_data)
		temp=self.head
		if temp==None:
			temp=new_node
			return
		last=self.head
		while last.next:
			last=last.next
		last.next=new_node
	def inmiddle(self,prev_node,new_data):
		new_node=Node(new_data)
		temp=self.head
		if temp==None:
			temp=new_node
			return
		new_node.next=prev_node.next
		prev_node.next=new_node
	def search(self,data):
		temp=self.head
		count=0
		while temp:
			if temp.data==data:
				print("The number {} is found-->".format(temp.data))
				count=count+1
				
			temp=temp.next
		if count==0:
			print("The element-- {}-- is not found".format(data))
	def del_in_beg(self,data):
		temp=self.head
		if temp==None:
			print("Empty linked list Nothing to delete")
		while temp:
			if temp.data==data:
				self.head=temp.next
			temp=temp.next
	def del_in_end(self,data):
		temp=self.head
		second_last=self.head
		while temp.next:
			second_last=temp
			temp=temp.next
		print("the temp data is",temp.data)
		print("the second last data is",second_last.data)
		if temp.data==data:
			second_last.next=None



if __name__=="__main__":
		llist=LinkedList()
		first=Node(10)
		llist.head=first
		second=Node(20)
		first.next=second
		third=Node(30)
		second.next=third
		#llist.inbeg(5)s
		#llist.inend(80)
		#llist.inend(90)
		llist.inmiddle(second,56)
		llist.inmiddle(second,76)
		llist.inmiddle(second,34)
		llist.search(56)
		llist.search(100)
		llist.del_in_beg(llist.head.data)
		llist.del_in_end(third.data)
		print(llist.head.data)
		llist.traversal()
