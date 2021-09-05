from logging import NOTSET


class Node:
    def __init__(self, input) -> None:
        self.data = input
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.count = 0   
    
    def __iter__(self):
        node = self.head
        while not node == None:
            yield node.data
            node = node.next

    def addFront(self, item):
        item = Node(item)
        item.next = self.head
        self.head = item

        self.count += 1
    
    def popFront(self):
        node = self.head
        if not node == None:
            self.head = node.next

        self.count -= 1

        return node.data
    
    def size(self):
        return self.count




class Stack:
    def __init__(self) -> None:
        self.items = LinkedList()
    
    def __iter__(self):
        for item in self.items:
            yield item

    def push(self, item):
        self.items.addFront(item)
    
    def pop(self):
        return self.items.popFront()
    
    def size(self):
        return self.items.size()

if __name__ == '__main__':
    pass
    
