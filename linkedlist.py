class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new
    def add_start(self, data):
        new = Node(data)                
        if self.head is None:
            self.head = new
            return
        new.next = self.head
        self.head = new   
    def add_after(self,prev,data):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        new = Node(data)
        while itr:
            if itr.data == prev:
                new.next = itr.next
                itr.next = new 
                return
            itr = itr.next
        print("previous node not found")
    def mid(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
    def del_start(self):
        if self.head is None:
            print("Linked list is empty")
            return    
        if self.head.next is None:
            self.head = None
            return  
        self.head = self.head.next
    def del_last(self):
        if self.head is None:
            print("Linked list is empty")
            return    
        if self.head.next is None:
            self.head = None
            return
        itr = self.head
        while itr.next:
            prev = itr
            itr = itr.next
        prev.next = None
    def del_mid(self,data):
        if self.head is None:
            print("linked list is empty ")  
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        prev = self.head
        while itr:
             if itr.data == data:
                 prev.next = itr.next
                 return
             prev = itr
             itr = itr.next
        print("Node not found")
    def reverse(self):
        stack=[]
        itr = self.head
        while itr:
            stack.append(itr.data)
            itr = itr.next
        while(len(stack)>1):
            x = stack.pop()
            print(x,end="-->")
        print(stack.pop())           
    def display(self):
        itr = self.head
        while itr:
            print(itr.data,end ="-->")
            itr = itr.next
    
ll = LinkedList()
ll.add_end(50)
ll.add_end(150)
ll.add_end(250)
ll.add_end(350)
ll.add_end(450)
ll.add_end(550)
ll.add_start(25)
ll.add_after(150,125)
ll.mid()
print("Before deletion:\n")
ll.display()
ll.del_last()
print("\nAfter deletion:\n")
ll.display()
print("Before deletion:\n")
ll.display()
ll.del_start()
print("\nAfter deletion:\n")
ll.display()
print("\nBefore deletion:\n")
ll.display()
ll.del_mid(125)
print("\nAfter deletion:\n")
ll.display()
