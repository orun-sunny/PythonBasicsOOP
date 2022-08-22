class Node:
    def __init__(self,value):
        self.next =None
        self.prev = None
        self.val = value

class DoubleLinkedList :
    def __init__(self):
        self.head = None
        self.tail =None
        self.size = 0
    def add(self, val):
        node = Node (val)

