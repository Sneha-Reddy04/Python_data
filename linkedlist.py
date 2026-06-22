class Node:
    def __init__(self, data):
        self.data = None
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new