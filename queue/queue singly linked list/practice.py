class Node:
    def __init__(self, input) -> None:
        self.data = input
        self.next = None
        self.count = 0

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.count = 0
    
    def __iter__(self):
        node = self.head
        while not node == None:
            yield node.data
            node = node.next

    def addFront(self, new):
        item = Node(new)
        item.next = self.head
        self.head = item

        self.count += 1

    def popBack(self):
        node = self.head
        previous = node
        item = None

        while not node == None:
            if node.next == None:
                previous.next = None
                item = node
            
            previous = node
            node = node.next
        
        self.count -= 1
        return item.data

    def size(self):
        return self.count

class Queue:
    def __init__(self) -> None:
        self.items = LinkedList()
    
    def __iter__(self):
        for item in self.items:
            yield item
        
    def enqueue(self, item):
        self.items.addFront(item)

    def dequeue(self):
        return self.items.popBack()

    def size(self):
        return self.items.size()

if __name__ == '__main__':
    pass
    
