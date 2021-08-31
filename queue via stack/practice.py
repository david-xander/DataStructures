from logging import NOTSET


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.items = None
        self.head = None
    
    def __iter__(self):
        current_now = self.head
        while not current_now == None:
            yield current_now.data
            current_now = current_now.next        
    
    def add(self, item):
        new = Node(item)
        new.next = self.head
        self.head = new

    def pop(self):
        node = self.head
        self.head = None
        if not node.next == None:
            self.head = node.next

        return node.data

    def size(self):
        count = 0
        node = self.head
        while not node == None:
            count += 1
            node = node.next   
        return count

class Stack:
    def __init__(self) -> None:
        self.items = LinkedList()
    
    def __iter__(self):
        for item in self.items:
            yield item
    
    def push(self, item):
        self.items.add(item)
    
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return self.items.size()

class Queue:
    def __init__(self) -> None:
        self.items = Stack()
        self.items_copy = Stack()
    
    def enqueue(self, item):
        self.items_copy = self.items
        self.items = Stack()
        self.items.push(item)
        while self.items_copy.size() > 0:
            self.items.push( self.items_copy.pop() )
    
    def dequeue(self):
        return self.items.pop()
        
    
    def printQueue(self):
        return ','.join(self.items)

