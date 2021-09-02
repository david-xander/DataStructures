class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0
    
    def __iter__(self):
        current_node = self.head
        while not current_node == None:
            yield current_node.data
            current_node = current_node.next
    
    def addFront(self, item):
        new_item = Node(item)
        if self.head == None:
            self.head = new_item
        else:
            new_item.next = self.head
            self.head.prev = new_item
            self.head = new_item

        if self.tail == None:
            self.tail = self.head

        self.count += 1

    def addBack(self, item):
        new_item = Node(item)
        if self.tail == None:
            self.tail = new_item
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item

        if self.head == None:
            self.head = self.tail

        self.count += 1

    def popFront(self):
        if not self.head == None:
            item = self.head
            
            if not self.head.next == None:
                self.head.next.prev = None

            self.head = self.head.next

            if self.head == None:
                self.tail = None

            self.count -= 1
            return item.data
        else:
            raise Exception('No item to pop')
    
    def popBack(self):
        if not self.tail == None:
            item = self.tail
            
            if not self.tail.prev == None:
                self.tail.prev.next = None

            self.tail = self.tail.prev

            if self.tail == None:
                self.head = None

            self.count -= 1 
            return item.data     
        else:
            raise Exception('No item to pop')
    
    def append(self, item):
        self.addBack(item)

    def pop(self):
        return self.popBack()

    def isEmpty(self):
        return self.count == 0
    
    def length(self) -> int:
        return self.count
    

    
if __name__ == '__main__':
    pass
    
